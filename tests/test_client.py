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

"""Test that the Client class is working properly."""

import pytest
import requests
from requests import Session
from datetime import date, datetime, timedelta
from requests import HTTPError

from landtransportsg.client import __Client
from landtransportsg.exceptions import APIError

from . import TEST_ACCOUNT_KEY
from .mocks.api_response_fault import APIResponseFault

# constants for testing date as date object
GOOD_DATE = date(2019, 7, 13)

# constants for testing date as string object
BAD_DATE = '2019-07-13'
TWO_MONTHS_AGO_DATE_STR = (date.today() + timedelta(-40)).strftime('%Y%m')

@pytest.fixture
def mock_requests_fault_response(monkeypatch):
    """Requests.Session().get() mocked to return sample Fault response."""
    def mock_requests_get(*args, **kwargs):
        return APIResponseFault()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture(scope='module')
def client():
    return __Client(TEST_ACCOUNT_KEY)

def test_repr(client):
    assert repr(client) == str(client.__class__)

@pytest.mark.parametrize(
    ('dt'),
    [
        (None),
        (GOOD_DATE),
    ],
)
def test_validate_kwargs_with_good_datetime_date(client, dt):
    try:
        _ = client.validate_kwargs(Date=dt)
    except Exception as e:
        pytest.fail('Unexpected error occurred: {}'.format(e))

def test_validate_kwargs_with_bad_datetime_date(client):
    with pytest.raises(ValueError):
        _ = client.validate_kwargs(Date=BAD_DATE)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'http://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2?Lat=1.364897&Long=103.766094',
            {},
        ),
        (
            'http://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2',
            {'Lat': 1.364897, 'Long': 103.766094},
        ),
    ],
)
def test_send_request_with_list_response(
    client,
    mock_requests_value_list_response,
    url,
    kwargs,
):
    response_content = client.send_request(url, **kwargs)
    assert isinstance(response_content, list)
    assert len(response_content) >= 0

    for v in response_content:
        assert isinstance(v, dict)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'http://datamall2.mytransport.sg/ltaodataservice/PV/Bus',
            {'Date': TWO_MONTHS_AGO_DATE_STR},
        ),
    ],
)
def test_send_request_with_str_response(
    client,
    mock_requests_value_str_response,
    url,
    kwargs,
):
    response_content = client.send_request(url, **kwargs)
    assert isinstance(response_content, list)

@pytest.mark.parametrize(
    ('url', 'kwargs'),
    [
        (
            'http://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2?Lat=foo&Long=bar',
            {},
        ),
        (
            'http://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2',
            {'Lat': 'foo', 'Long': 'bar'},
        ),
    ],
)
def test_send_request_with_bad_arguments(client, url, kwargs):
    response_content = client.send_request(url, **kwargs)
    assert len(response_content) == 0

def test_send_request_with_invalid_endpoint(client):
    with pytest.raises(HTTPError):
        _ = client.send_request(
            'http://datamall2.mytransport.sg/ltaodataservice/',
        )

def test_send_request_with_fault_response(
    client,
    mock_requests_fault_response,
):
    with pytest.raises(APIError) as excinfo:
        def send_fault_request():
            _ = client.send_request(
                'http://datamall2.mytransport.sg/ltaodataservice/',
            )

        send_fault_request()

    assert 'Rate limit quota violation' in str(excinfo.value)

def test_send_download_request_with_bad_value(
    client,
    mock_requests_value_str_bad_value_response,
):
    with pytest.raises(APIError):
        _ = client.send_download_request(
            'http://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsland',
            ID='ArrowMarking',
        )

def test_send_download_request_with_missing_link(
    client,
    mock_requests_value_str_missing_link_response,
):
    with pytest.raises(APIError):
        _ = client.send_download_request(
            'http://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsland',
            ID='ArrowMarking',
        )

def test_send_download_request_with_bad_link(
    client,
    mock_requests_value_str_bad_link_response,
):
    with pytest.raises(APIError):
        _ = client.send_download_request(
            'http://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsland',
            ID='ArrowMarking',
        )
