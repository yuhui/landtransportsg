# Copyright 2019 Yuhui
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

import backoff
import requests
import time
from datetime import date, datetime
from requests import Session

from . import timezone
from .exceptions import APIError

class __Client(object):
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
        return '{}'.format(self.__class__)

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
                if k is 'Date' and not isinstance(v, date):
                    raise ValueError('"Date" value is not a date object.')

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

        response_json = self.__send_request(url, params=params)

        response_content = self.__sanitise_timestamps(response_json)
        if 'value' in response_content:
            # the real data is in key 'value', so return that instead
            response_content = response_content['value']

        return response_content

    # private

    def __sanitise_timestamps(self, dictionary):
        """Convert timestamp strings to datetime objects and
        return the dictionary.
        """
        for key in dictionary:
            val = dictionary[key]
            if isinstance(val, str):
                try:
                    dictionary[key] = timezone.datetime_from_string(val)
                except Exception:
                    pass
            elif isinstance(val, dict):
                dictionary[key] = self.__sanitise_timestamps(val)
            elif isinstance(val, list):
                dictionary[key] = [
                    self.__sanitise_timestamps(v) \
                        if isinstance(v, dict) else v for v in val
                ]

        return dictionary

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
        response = self.session.get(url, params=params, headers=headers)

        try:
            response_json = response.json()
        except ValueError:
            pass

        if response.status_code == requests.codes['server_error'] and \
            'fault' in response_json:
            fault = response_json['fault']
            faultstring = fault['faultstring']
            faultdetail = [
                '{}: {}'.format(k, v) for k, v in fault['detail'].items()
            ]

            raise APIError(
                faultstring,
                errors=faultdetail,
            )
        elif response.status_code != requests.codes['ok']:
            response.raise_for_status()

        # it is possible to paginate "forever" by skipping by 500 records
        # so check if there are any records in the current results first
        response_json_value = response_json.get('value')
        if isinstance(response_json_value, list) and \
            len(response_json_value) == 500:
            # get the next page of results
            current_skip = params.pop('$skip', 0)
            skip = current_skip + 500
            params['$skip'] = skip

            # wait a while so as not to flood the endpoint
            if skip % 1000 is 0:
                time.sleep(1)

            next_response_json = self.__send_request(
                url,
                params,
                headers,
            )
            response_json['value'] += next_response_json['value']

        return response_json
