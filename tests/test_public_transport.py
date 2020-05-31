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

"""Test that the Public Transport class is working properly."""

import pytest
from datetime import date, timedelta
from requests import Session
from requests.exceptions import HTTPError

from landtransportsg import PublicTransport
from landtransportsg.exceptions import APIError

from . import TEST_ACCOUNT_KEY
from .mocks.api_response_bus_arrival import APIResponseBusArrival
from .mocks.api_response_train_service_alerts \
    import APIResponseTrainServiceAlerts

# constants for testing valid bus_stop_code and service_number
GOOD_BUS_STOP_CODE = '83139'
GOOD_SERVICE_NUMBER = '15'
GOOD_DATE = date.today() - timedelta(50)

# constants for testing bad dates
BAD_DATE_STR = '2019-09-15'
VERY_OLD_DATE = date.today() - timedelta(200)

@pytest.fixture
def mock_requests_bus_arrival_response(monkeypatch):
    """Requests.Session().get() mocked to return sample BusArrival API
    response.
    """
    def mock_requests_get(*args, **kwargs):
        return APIResponseBusArrival()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def mock_requests_train_service_alerts_response(monkeypatch):
    """Requests.Session().get() mocked to return sample TrainServiceAlerts
    API response.
    """
    def mock_requests_get(*args, **kwargs):
        return APIResponseTrainServiceAlerts()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def client():
    return PublicTransport(TEST_ACCOUNT_KEY)

def test_bus_arrival(client, mock_requests_bus_arrival_response):
    bus_arrival = client.bus_arrival(
        GOOD_BUS_STOP_CODE,
        GOOD_SERVICE_NUMBER,
    )

    assert isinstance(bus_arrival, dict)

    assert 'BusStopCode' in bus_arrival
    assert bus_arrival['BusStopCode'] == GOOD_BUS_STOP_CODE

    assert 'Services' in bus_arrival
    services = bus_arrival['Services']
    assert isinstance(services, list)

    found_service_number_in_services = False
    for s in services:
        assert isinstance(s, dict)
        assert 'ServiceNo' in s
        if s['ServiceNo'] == GOOD_SERVICE_NUMBER:
            found_service_number_in_services = True
    assert found_service_number_in_services is True

@pytest.mark.parametrize(
    ('bus_stop_code', 'service_number'),
    [
        (None, GOOD_SERVICE_NUMBER), # None bus_stop_code
        (83139, GOOD_SERVICE_NUMBER), # int bus_stop_code
        ('8313', GOOD_SERVICE_NUMBER), # 4-character bus_stop_code
        ('foobr', GOOD_SERVICE_NUMBER), # non-number bus_stop_code
        (GOOD_BUS_STOP_CODE, 15), # int service_number
    ],
)
def test_bus_arrival_with_bad_inputs(client, bus_stop_code, service_number):
    with pytest.raises(ValueError):
        _ = client.bus_arrival(bus_stop_code, service_number)

def test_train_service_alerts(
    client,
    mock_requests_train_service_alerts_response,
):
    train_service_alerts = client.train_service_alerts()

    assert isinstance(train_service_alerts, dict)

    assert 'Status' in train_service_alerts
    assert isinstance(train_service_alerts['Status'], int)
    assert 'AffectedSegments' in train_service_alerts
    assert isinstance(train_service_alerts['AffectedSegments'], list)
    assert 'Message' in train_service_alerts
    assert isinstance(train_service_alerts['Message'], list)

@pytest.mark.parametrize(
    ('function', 'dt'),
    [
        ('passenger_volume_by_bus_stops', None),
        ('passenger_volume_by_origin_destination_bus_stops', None),
        ('passenger_volume_by_origin_destination_train_stations', None),
        ('passenger_volume_by_train_stations', None),
        ('passenger_volume_by_bus_stops', GOOD_DATE),
        ('passenger_volume_by_origin_destination_bus_stops', GOOD_DATE),
        ('passenger_volume_by_origin_destination_train_stations', GOOD_DATE),
        ('passenger_volume_by_train_stations', GOOD_DATE),
    ],
)
def test_class_passenger_volume_function(
    client,
    mock_requests_value_str_response,
    function,
    dt,
):
    result = getattr(client, function)(dt)

    assert isinstance(result, str)

@pytest.mark.parametrize(
    ('function', 'dt'),
    [
        ('passenger_volume_by_bus_stops', BAD_DATE_STR),
        ('passenger_volume_by_origin_destination_bus_stops', BAD_DATE_STR),
        (
            'passenger_volume_by_origin_destination_train_stations',
            BAD_DATE_STR,
        ),
        ('passenger_volume_by_train_stations', BAD_DATE_STR),
        ('passenger_volume_by_bus_stops', VERY_OLD_DATE),
        ('passenger_volume_by_origin_destination_bus_stops', VERY_OLD_DATE),
        (
            'passenger_volume_by_origin_destination_train_stations',
            VERY_OLD_DATE,
        ),
        ('passenger_volume_by_train_stations', VERY_OLD_DATE),
    ],
)
def test_class_passenger_volume_function_with_BAD_DATE_STRs(
    client,
    function,
    dt,
):
    with pytest.raises(ValueError):
        _ = getattr(client, function)(dt)

@pytest.mark.parametrize(
    'function',
    [
        'bus_services',
        'bus_routes',
        'bus_stops',
        'taxi_availability',
        'taxi_stands',
    ],
)
def test_class_function(
    client,
    mock_requests_value_list_response,
    function,
):
    result = getattr(client, function)()

    assert isinstance(result, list)
