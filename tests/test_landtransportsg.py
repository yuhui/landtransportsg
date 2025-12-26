# Copyright 2020-2025 Yuhui
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

# pylint: disable=invalid-name,missing-function-docstring,redefined-outer-name,unused-argument

"""Test that the LandTransportSg class is working properly."""

from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import pytest
from requests import HTTPError
from requests_cache import CachedSession

from landtransportsg.landtransportsg import LandTransportSg
from landtransportsg.constants import USER_AGENT
from landtransportsg.exceptions import APIError

from . import TEST_ACCOUNT_KEY

from .mocks.types_args import MockArgsDict
from .mocks.api_response_public_transport import APIResponseBusArrival
from .mocks.api_response_landtransportsg import (
    APIResponseBadLink,
    APIResponseFault,
    APIResponseMissingLink,
    APIResponseValueList,
)

SANITISE_DATA_DICT = {
    'value_str': 'foo bar',
    'value_ignore': '37',
    'value_int': 42,
    'value_bool': True,
    'value_date': '1/7/2019',
    'value_blank': '',
    'value_list': [1, '2', {
        'key1': '205',
        'date_time': '2024-12-01T09:57:45+08:00',
    }],
    'value_dict': {
        'key1': '316',
        'date_time': '2024-12-01 09:57:45.789',
    },
}

# constants for testing date as date object
GOOD_DATE = date(2019, 7, 13)
GOOD_DATE_STR = '201907'
GOOD_DATETIME = datetime(2019, 7, 13, 4, 56, 8)
GOOD_DATETIME_STR = '2019-07-13T04:56:08'

# constants for testing date as string object
TWO_MONTHS_AGO_DATE_STR = (date.today() + timedelta(-40)).strftime('%Y%m')

@pytest.fixture
def mock_requests_value_bus_arrival_response(monkeypatch):
    """Requests.get() mocked to return sample Bus Arrival API response."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseBusArrival()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

@pytest.fixture
def mock_requests_fault_response(monkeypatch):
    """Requests.Session().get() mocked to return sample Fault response."""
    def mock_requests_get(*args, **kwargs):
        return APIResponseFault()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

@pytest.fixture(scope='module')
def client():
    return LandTransportSg(TEST_ACCOUNT_KEY)

def test_repr(client):
    assert repr(client).startswith(str(client.__class__))
    assert USER_AGENT in repr(client)

@pytest.mark.parametrize(
    ('original_params', 'default_params', 'key_map', 'expected_params'),
    [
        (
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE,
                'datetime': GOOD_DATETIME,
            },
            {
                'foobar': 'foo and bar',
                'meaning_of_universe': 42,
            },
            {
                'datetime': 'DATE_TIME',
                'meaning_of_universe': 'meaningOfUniverse',
            },
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE_STR,
                'DATE_TIME': GOOD_DATETIME_STR,
                'meaningOfUniverse': 42,
            },
        ),
        (
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE,
                'datetime': GOOD_DATETIME,
            },
            None,
            None,
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE_STR,
                'datetime': GOOD_DATETIME_STR,
            },
        ),
    ],
)
def test_build_params(
    client,
    original_params,
    default_params,
    key_map,
    expected_params,
):
    params = client.build_params(MockArgsDict, original_params, default_params, key_map)
    assert params == expected_params

@pytest.mark.parametrize(
    ('kwargs', 'expected_result'),
    [
        (
            {},
            {
                'value_str': 'foo bar',
                'value_ignore': 37,
                'value_int': 42,
                'value_bool': True,
                'value_date': '1/7/2019',
                'value_blank': None,
                'value_list': [1, 2, {
                    'key1': 205,
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, tzinfo=ZoneInfo(key='Asia/Singapore')),
                }],
                'value_dict': {
                    'key1': 316,
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, 789000, tzinfo=ZoneInfo(key='Asia/Singapore')),
                },
            },
        ),
        (
            {'iterate': False},
            SANITISE_DATA_DICT,
        ),
        (
            {
                'ignore_keys': [
                    'value_ignore',
                    'value_dict.date_time',
                    'value_list[].key1',
                ]
            },
            {
                'value_str': 'foo bar',
                'value_ignore': '37',
                'value_int': 42,
                'value_bool': True,
                'value_date': '1/7/2019',
                'value_blank': None,
                'value_list': [1, 2, {
                    'key1': '205',
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, tzinfo=ZoneInfo(key='Asia/Singapore')),
                }],
                'value_dict': {
                    'key1': 316,
                    'date_time': '2024-12-01 09:57:45.789',
                },
            },
        ),
    ],
)
def test_sanitise_data(
    client,
    kwargs,
    expected_result,
):
    result = client.sanitise_data(value=SANITISE_DATA_DICT, **kwargs)
    assert result == expected_result

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'https://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2?Lat=1.364897&Long=103.766094', # pylint: disable:line-too-long
            {},
        ),
        (
            'https://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2',
            {
                'params': {
                    'Lat': 1.364897,
                    'Long': 103.766094,
                },
            },
        ),
    ],
)
def test_send_request_with_list_response(
    client,
    monkeypatch,
    url,
    kwargs,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseValueList()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    response_content = client.send_request(url, **kwargs)
    assert isinstance(response_content, list)
    assert len(response_content) >= 0

    for v in response_content:
        assert isinstance(v, dict)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'https://datamall2.mytransport.sg/ltaodataservice/PV/Bus',
            {
                'params': {'Date': TWO_MONTHS_AGO_DATE_STR},
            },
        ),
    ],
)
def test_send_request_with_str_response(
    client,
    mock_requests_link_response,
    url,
    kwargs,
):
    response_content = client.send_request(url, **kwargs)
    assert isinstance(response_content, list)

@pytest.mark.parametrize(
    'url',
    [
        'https://datamall2.mytransport.sg/ltaodataservice/BusStops',
    ],
)
def test_send_request_with_more_than_500_records(
    client,
    url,
):
    response_content = client.send_request(url)
    assert isinstance(response_content, list)
    assert len(response_content) > 500

    bus_stops = [r['BusStopCode'] for r in response_content]
    assert len(bus_stops) == len(set(bus_stops))

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival',
            {
                'params': {
                    'BusStopCode': '83139',
                    'ServiceNo': '15',
                },
                'sanitise_ignore_keys': [
                    'BusStopCode',
                    'Services[].ServiceNo',
                ],
            },
        ),
    ],
)
def test_send_request_with_sanitise_ignored_keys(
    client,
    mock_requests_value_bus_arrival_response,
    url,
    kwargs,
):
    response_content = client.send_request(url, **kwargs)

    print(response_content)
    bus_stop_code = response_content.get('BusStopCode', None)
    assert isinstance (bus_stop_code, str)

    service_no = response_content['Services'][0].get('ServiceNo', None)
    assert isinstance (service_no, str)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'https://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2',
            {
                'params': {
                    'Lat': 'foo',
                    'Long': 'bar',
                },
            },
        ),
    ],
)
def test_send_request_with_bad_arguments(client, url, kwargs):
    response_content = client.send_request(url, **kwargs)
    assert len(response_content) == 0

def test_send_request_with_invalid_endpoint(client):
    with pytest.raises(HTTPError):
        _ = client.send_request(
            'https://datamall2.mytransport.sg/ltaodataservice/',
        )

def test_send_request_with_fault_response(
    client,
    mock_requests_fault_response,
):
    with pytest.raises(APIError) as excinfo:
        def send_fault_request():
            _ = client.send_request(
                'https://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2?Lat=foo&Long=bar',
            )

        send_fault_request()

    assert 'Rate limit quota violation' in str(excinfo.value)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'https://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsland',
            {
                'params': {'ID': 'ArrowMarking'},
            },
        ),
    ],
)
def test_send_download_request_with_missing_link(
    client,
    monkeypatch,
    url,
    kwargs,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseMissingLink()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    with pytest.raises(APIError):
        _ = client.send_download_request(url, **kwargs)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'https://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsland',
            {
                'params': {'ID': 'ArrowMarking'},
            },
        ),
    ],
)
def test_send_download_request_with_bad_link(
    client,
    monkeypatch,
    url,
    kwargs,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseBadLink()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    with pytest.raises(APIError):
        _ = client.send_download_request(url, **kwargs)
