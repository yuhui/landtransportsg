# Copyright 2020-2025 Yuhui. All rights reserved.
#
# Licensed under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Client mixin for interacting with all of the API endpoints."""

import time
from datetime import date, datetime
from typing import Any, Optional

from requests import codes as requests_codes
from requests.adapters import HTTPAdapter, Retry
from requests_cache import BaseCache, CachedSession
from typeguard import check_type, typechecked

from .constants import CACHE_NAME, USER_AGENT
from .exceptions import APIError
from .timezone import datetime_from_string
from .types import Url

class LandTransportSg:
    """Client mixin for other API Clients.

    Normally, it does not need to be created by applications. But \
        applications may use the public methods provided here.

    The constructor sets the following:

    - Connection retries using exponential backoff. \
        (Reference: https://stackoverflow.com/a/35504626.)
    - Cache (cache duration/expiry is set in ``send_request()``).
    - Account key. An account key is required to use the LTA DataMall API. \
        Request for one from \
        https://www.mytransport.sg/content/mytransport/home/dataMall/request-for-api.html.
    - User-agent header.

    :param cache_backend: Cache backend name or instance to use. Refer to \
        https://requests-cache.readthedocs.io/en/stable/user_guide/backends.html \
        for more information and allowed values. Defaults to "sqlite".
    :type cache_backend: str | BaseCache

    :param account_key: The LTA DataMall-assigned API key.
    :type account_key: str
    """

    @typechecked
    def __init__(
        self,
        account_key: str,
        cache_backend: str | BaseCache='sqlite',
    ) -> None:
        """Constructor method"""
        retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504]
        )

        self.session = CachedSession(
            CACHE_NAME,
            backend=cache_backend,
            stale_if_error=False,
        )
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.headers.update({
            'AccountKey': account_key,
            'Accept': 'application/json',
            'User-Agent': USER_AGENT,
        })

    @typechecked
    def __repr__(self) -> str:
        """String representation"""
        return f'{self.__class__} ({USER_AGENT})'

    @typechecked
    def build_params(
        self,
        params_expected_type: Any,
        original_params: Any,
        default_params: Optional[dict]=None,
        key_map: Optional[dict[str, str]]=None,
    ) -> dict:
        """Build the list of parameters that are compatible for use with the \
            endpoint URLs, e.g. camelCase parameter names instead of Python's \
            snake_case, datetime objects to strings.

        :param params_expected_type: The expected type of \
            ``original_params``. Should be one of the importable types from \
            the client's ``types_args``.
        :type params_expected_type: Any

        :param original_params: The set of parameters to use for building.
        :type original_params: Any but should really be dict

        :param default_params: The set of parameters' default values. Should \
            be of the same type as what is specified in \
            ``params_expected_type``. Defaults to None.
        :type default_params: dict

        :param key_map: Mapping of keys used in ``params_expected_types`` to \
            keys expected by the endpoint. Defaults to None.
        :type key_map: dict[str, str]

        :return: The set of parameters that can be used with the API endpoints.
        :rtype: dict
        """
        if default_params is None:
            default_params = {}
        if key_map is None:
            key_map = {}

        joined_params = default_params | original_params

        # Ensure that the parameters match the expected input parameter types.
        _ = check_type(joined_params, params_expected_type)

        params: dict = {}
        for key, value in joined_params.items():
            param_key = key_map[key] if key in key_map else key

            # Convert date and datetime to ISO format strings
            # Leave all other types as-is
            # IMPORTANT! Test for `datetime` before `date`!
            if isinstance(value, datetime):
                params[param_key] = value.strftime('%Y-%m-%dT%H:%M:%S')
            elif isinstance(value, date):
                params[param_key] = value.strftime('%Y%m')
            else:
                params[param_key] = value

        return params

    @typechecked
    def sanitise_data(
        self,
        value: Any,
        iterate: Optional[bool]=True,
        ignore_keys: Optional[list[str]]=None,
        key_path: Optional[str]=None,
    ) -> Any:
        """Convert the following:

        - If ``iterate`` is True and value is a ``dict`` or ``list``: \
            sanitise the value's contents.
        - Blank string: convert to None.
        - String that is like date or datetime: convert to ``datetime.date`` \
            or ``datetime.datetime`` object respectively.
        - String that is number-like: convert to ``int`` or ``float`` \
            appropriately.
        - Finally: Leave the value as-is.

        :param value: Value to sanitise.
        :type value: Any

        :param iterate: If True, then ``list`` and ``dict`` objects are \
            sanitised recursively. Defaults to True.
        :type iterate: bool

        :param ignore_keys: List of dict keys to ignore when sanitising, if \
            value is a ``dict``. Defaults to None.
        :type ignore_keys: list[str]

        :param key_path: Current path of key in the dict. Defaults to None.
        :type key_path: str

        :return: The sanitised value.
        :rtype: Any
        """
        if ignore_keys is None:
            ignore_keys = []

        if key_path is None:
            key_path = ''

        sanitised_value: Any = value

        if isinstance(value, list) and iterate:
            sanitised_value = [
                self.sanitise_data(
                    v,
                    iterate=iterate,
                    ignore_keys=ignore_keys,
                    key_path=f'{key_path}[]'
                ) for v in value
            ]
        elif isinstance(value, dict) and iterate:
            sanitised_value = {}
            for k, v in value.items():
                current_key_path = '.'.join([key_path, k]) if key_path else k
                if isinstance(v, str) and v == '':
                    sanitised_value[k] = self.sanitise_data(v)
                elif current_key_path in ignore_keys:
                    sanitised_value[k] = v
                else:
                    sanitised_value[k] = self.sanitise_data(
                        v,
                        iterate=iterate,
                        ignore_keys=ignore_keys,
                        key_path=current_key_path,
                    )
        elif isinstance(value, str):
            if value == '':
                sanitised_value = None
            else:
                try:
                    # pylint: disable=broad-exception-caught

                    # Convert to a date/datetime.
                    sanitised_value = datetime_from_string(value)
                except Exception:
                    try:
                        # Convert to an integer
                        sanitised_value = int(value)
                    except Exception:
                        try:
                            # Convert to a float
                            sanitised_value = float(value)
                        except Exception:
                            pass

        return sanitised_value

    @typechecked
    def send_download_request(
        self,
        url: Url,
        params: Optional[dict]=None,
        cache_duration: Optional[int]=0,
    ) -> Url:
        """Send a request to an endpoint that expects a response with a \
        download link.

        Normally, this method does not need to be called directly. However, \
            if LTA Datamall were to change their API specification but this \
            package has not yet been updated to support that change, then \
            applications may use this method to call the changed endpoints.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL. \
            Parameter names **must** match the names required by the \
            endpoints, particularly with typecase (e.g. camelCase). Defaults \
            to None.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires. \
            Defaults to 0, i.e. do not cache.
        :type cache_duration: int

        :raises HTTPError: Error occurred during the request process.

        :return: Link for downloading the requested file.
        :rtype: Url
        """
        download_link: Url

        download: list[dict] = self.send_request(
            url,
            params=params,
            cache_duration=cache_duration,
        )

        if len(download) == 0:
            raise APIError('No download link returned.')

        download_link = download[0].get('Link', '')

        if download_link == '':
            raise APIError('No download link returned.')

        return download_link

    @typechecked
    def send_request(
        self,
        url: Url,
        params: Optional[dict]=None,
        cache_duration: Optional[int]=0,
        sanitise_ignore_keys: Optional[list[str]]=None,
    ) -> Any:
        """Send a request to an endpoint and return its response.

        Normally, this method does not need to be called directly. However, \
            if LTA Datamall were to change their API specification but this \
            package has not yet been updated to support that change, then \
            applications may use this method to call the changed endpoints.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL. \
            Parameter names **must** match the names required by the \
            endpoints, particularly with typecase (e.g. camelCase). Defaults \
            to {}.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires. \
            Defaults to 0, i.e. do not cache.
        :type cache_duration: int

        :param sanitise_ignore_keys: List of keys to ignore in the response \
            value during sanitising when that response value is a ``dict``. \
            Defaults to [], i.e. empty list.
        :type sanitise_options: list[str]

        :raises HTTPError: Error occurred during the request process.

        :return: Results from the response.
        :rtype: Any
        """
        data: Any

        if params is None:
            params = {}

        if sanitise_ignore_keys is None:
            sanitise_ignore_keys = []

        response_val = self._collect_response_value(
            url,
            params=params,
            cache_duration=cache_duration,
        )

        if isinstance(response_val, dict) and 'odata.metadata' in response_val:
            # this isn't documented in LTA Datamall's API guide
            del response_val['odata.metadata']

        data = self.sanitise_data(
            response_val,
            ignore_keys=sanitise_ignore_keys,
        )

        return data

# private

    @typechecked
    def _collect_response_value(
        self,
        url: Url,
        params: dict,
        cache_duration: int,
    ) -> Any:
        """Collect response value from an endpoint. If the response returns a \
        list of 500 records, then keep calling itself recursively to collect \
        more records.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires.
        :type cache_duration: int

        :raises HTTPError: Error occurred during the request process.

        :return: Results from the response.
        :rtype: Any
        """
        response_value: Any

        if '$skip' not in params:
            params['$skip'] = 0

        response = self.session.get(
            url,
            params=params,
            expire_after=cache_duration,
        )

        response_json = {}
        try:
            response_json = response.json()
        except ValueError:
            pass

        if response.status_code == requests_codes['server_error'] \
            and 'fault' in response_json:
            fault = response_json['fault']
            faultstring = fault['faultstring']
            faultdetail = [
                f'{k}: {v}' for k, v in fault['detail'].items()
            ]

            raise APIError(
                faultstring,
                errors=faultdetail,
            )

        if response.status_code != requests_codes['ok']:
            response.raise_for_status()

        response_value = response_json.get('value') \
            if 'value' in response_json else response_json

        # it is possible to paginate "forever" by skipping by 500 records
        # so check if there are any records in the current results first
        if isinstance(response_value, list) and len(response_value) == 500:
            # get the next page of results
            current_skip = params.pop('$skip', 0)
            skip = current_skip + 500
            params['$skip'] = skip

            # wait a while so as not to flood the endpoint
            if skip % 1000 == 0:
                time.sleep(1)

            next_response_value = self._collect_response_value(
                url,
                params=params,
                cache_duration=cache_duration,
            )
            # next_data should be a list too
            response_value += next_response_value

        return response_value

__all__ = [
    'LandTransportSg',
]
