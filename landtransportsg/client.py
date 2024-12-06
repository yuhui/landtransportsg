# Copyright 2020 Yuhui
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

import backoff
import requests
from requests import Session

from . import timezone
from .exceptions import APIError

class Lta:
    """Client mixin for other API Clients.

    Attributes:
        account_key (str):
            The LTA DataMall-assigned API key.
            Request for one from https://www.mytransport.sg/content/mytransport/home/dataMall/request-for-api.html.

    """

    def __init__(self, account_key):
        self.session = Session()
        self.session.headers.update({
            'AccountKey': account_key,
            'accept': 'application/json',
        })

    def __repr__(self):
        return f'{self.__class__}'

    def validate_kwargs(self, **kwargs):
        """Verify that the kwargs are specified properly.

        Arguments:
            kwargs (dict):
                (optional) Attribute-value arguments to validate.
                If an attribute is date-related, then its value is expected to
                be of `date` instance.

        Raises:
            ValueError:
                Raised if Date is specified but isn't a date object.
        """
        for k, v in kwargs.items():
            if v is not None:
                if k == 'Date' and not isinstance(v, date):
                    raise ValueError('"Date" value is not a date object.')

    def send_download_request(self, url, **kwargs):
        """Send a request to an endpoint that expects a response with a
        download link.

        Arguments:
            url (str):
                The endpoint URL to send the request to.
            kwargs (dict):
                (optional) Attribute-value arguments to be passed as parameters
                to the endpoint URL.
                If an attribute is date-related, then its value is expected to
                be of `date` instance and will be standardised to the format
                required by the endpoint.

        Returns:
            (str) Link for downloading the requested file.

        Raises:
            APIError:
                Raised if the API responds with an unexpected response.
        """
        download = self.send_request(url, **kwargs)

        if not isinstance(download, list):
            raise APIError(
                "Download link not returned unexpectedly.",
            )

        if len(download) == 0:
            raise APIError("No download link returned.")

        download_link = download[0].get('Link')
        if not isinstance(download_link, str):
            raise APIError(
                "Download link not returned, got a non-string unexpectedly.",
            )

        return download_link

    def send_request(self, url, **kwargs):
        """Send a request to an endpoint.

        Arguments:
            url (str):
                The endpoint URL to send the request to.
            kwargs (dict):
                (optional) Attribute-value arguments to be passed as parameters
                to the endpoint URL.
                If an attribute is date-related, then its value is expected to
                be of `date` instance and will be standardised to the format
                required by the endpoint.

        Returns:
            (list or object) Response JSON content of the request.
        """
        params = {}
        for attribute, value in kwargs.items():
            if value is None:
                pass
            elif isinstance(value, date):
                params[attribute] = value.strftime('%Y%m')
            else:
                params[attribute] = value

        response = self.__send_request(url, params=params)

        return response

    # private

    def __sanitise_timestamps(self, dictionary):
        """Convert timestamp strings to datetime objects and
        return the dictionary.
        """
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
    def __send_request(self, url, params=None, headers={}):
        """Send a request to an endpoint, using backoff with a maximum of 2
        tries.

        Arguments:
            url (str):
                The endpoint URL to send the request to.
            params (dict):
                (optional) Parameters to send with the URL.
            headers (dict:
                (optional) HTTP headers to send with the request.
                `AccountKey` and `accept` are set automatically, so these
                headers don't need to be specified here.

        Returns:
            (Response) response of the request.

        Raises:
            HTTPError:
                Raised if there is a network error.
            APIError:
                Raised if the API responds with an error.
        """

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
