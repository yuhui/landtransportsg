# Copyright 2020-2024 Yuhui. All rights reserved.
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

"""Mixin for Clients that interact with LTA DataMall's APIs."""

import time
from datetime import date
from typing import Any, Optional

import backoff
import requests
from requests import Session
from typeguard import typechecked

from . import timezone
from .exceptions import APIError
from .types import Url

class Lta:
    """Client mixin for other API Clients.

    An account key is required to use the LTA DataMall API. Request for one \
    from \
    https://www.mytransport.sg/content/mytransport/home/dataMall/request-for-api.html.
    """

    @typechecked
    def __init__(self, account_key: str) -> None:
        """Constructor method

        :param account_key: The LTA DataMall-assigned API key.
        :type account_key: str
        """
        self.session = Session()
        self.session.headers.update({
            'AccountKey': account_key,
            'accept': 'application/json',
        })

    @typechecked
    def __repr__(self) -> str:
        """String representation"""
        return f'{self.__class__}'

    @typechecked
    def validate_kwargs(self, **kwargs: Any) -> None:
        """Verify that the kwargs are specified properly.

        :param kwargs: Attribute-value arguments to validate. If an attribute \
            is date-related, then its value is expected to be of `date` \
            instance.
        :type kwargs: Any

        :raises ValueError: Raised if Date is specified but isn't a date \
            object.
        """
        for k, v in kwargs.items():
            if v is not None:
                if k == 'Date' and not isinstance(v, date):
                    raise ValueError('"Date" value is not a date object.')

    @typechecked
    def send_download_request(self, url: Url, **kwargs: Any) -> Url:
        """Send a request to an endpoint that expects a response with a \
        download link.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param kwargs: Attribute-value arguments to be passed as parameters \
            to the endpoint URL. If an attribute is date-related, then its \
            value is expected to be of `date` instance and will be \
            standardised to the format required by the endpoint. Optional.
        :type kwargs: Any

        :raises APIError: List of download links is empty.

        :return: Link for downloading the requested file.
        :rtype: Url
        """
        download_link: Url

        download = self.send_request(url, **kwargs)

        if not isinstance(download, list):
            raise APIError('Download link not returned unexpectedly.')

        if len(download) == 0:
            raise APIError('No download link returned.')

        download_link = download[0].get('Link')

        return download_link

    @typechecked
    def send_request(self, url: Url, **kwargs: Any) -> Any:
        """Send a request to an endpoint and get its response's list of \
        results.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param kwargs: Attribute-value arguments to be passed as parameters \
            to the endpoint URL. If an attribute is date-related, then its \
            value is expected to be of `date` instance and will be \
            standardised to the format required by the endpoint. Optional.
        :type kwargs: Any

        :return: Results from the response.
        :rtype: Any
        """
        response: Any

        attrs = {}
        for attribute, value in kwargs.items():
            if value is None:
                pass
            elif isinstance(value, date):
                attrs[attribute] = value.strftime('%Y%m')
            else:
                attrs[attribute] = value

        params = attrs if len(attrs) > 0 else None

        response = self.__send_request(url, params=params)

        return response

    # private

    @typechecked
    def __sanitise_data(self, value: Any) -> Any:
        """Convert a value to a native object (e.g. timestamp string to \
        datetime) and return the value. If value is a list or dict, then \
        iterate through its items.

        :param value: Value to sanitise.
        :type value: Any

        :return:  The sanitised value.
        :rtype: Any
        """
        sanitised_value: Any

        sanitised_value = value
        if isinstance(value, list):
            sanitised_value = list(map(self.__sanitise_data, value))
        elif isinstance(value, dict):
            sanitised_value = {
                k: self.__sanitise_data(v) for k, v in value.items()
            }
        elif isinstance(value, str):
            try:
                sanitised_value = timezone.datetime_from_string(value)
            except Exception: # pylint: disable=broad-exception-caught
                pass

        return sanitised_value

    @backoff.on_exception(backoff.expo, APIError, max_tries=2)
    @typechecked
    def __send_request(
        self,
        url: Url,
        params: Optional[dict[str, Any]]=None,
        headers: Optional[dict[str, Any]]=None,
    ) -> Any:
        """Send a request to an endpoint and get the response's list of \
        results, using backoff with a maximum of 2 tries. If pagination is \
        required, then get responses from all pages in one final list.

        `AccountKey` and `accept` headers are set automatically, so they \
        don't need to be specified here.

        :param url: The endpoint URL to send the request to.
        :type url: str

        :param params: Parameters to send with the URL. Defaults to None.
        :type params: dict[str, Any]

        :param headers: HTTP headers to send with the request. Defaults to \
            None.
        :type headers: dict[str, Any]

        :raises APIError: The endpoint responds with an error.

        :return: Results from the response's 'value' key.
        :rtype: Any
        """
        response_value: Any

        response = self.session.get(
            url,
            params=params,
            headers=headers,
        )

        response_json = {}
        try:
            response_json = response.json()
        except ValueError:
            pass

        if response.status_code == requests.codes['server_error'] and \
            'fault' in response_json:
            fault = response_json['fault']
            faultstring = fault['faultstring']
            faultdetail = [
                f'{k}: {v}' for k, v in fault['detail'].items()
            ]

            raise APIError(
                faultstring,
                errors=faultdetail,
            )

        if response.status_code != requests.codes['ok']:
            response.raise_for_status()

        # it is possible to paginate "forever" by skipping by 500 records
        # so check if there are any records in the current results first
        response_value = response_json.get('value') \
            if 'value' in response_json else response_json
        if isinstance(response_value, list) and len(response_value) == 500:
            # get the next page of results
            if params is None:
                params = {
                    '$skip': 0
                }
            current_skip = params.pop('$skip', 0)
            skip = current_skip + 500
            params['$skip'] = skip

            # wait a while so as not to flood the endpoint
            if skip % 1000 == 0:
                time.sleep(1)

            next_response_value = self.__send_request(
                url,
                params,
                headers,
            )
            # next_response_value should be a list too
            response_value += next_response_value

        response_value = self.__sanitise_data(response_value)

        return response_value

__all__ = [
    'Lta',
]
