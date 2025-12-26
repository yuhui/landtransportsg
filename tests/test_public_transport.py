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

"""Test that the Public Transport class is working properly."""

from datetime import date, timedelta

import pytest
from requests_cache import CachedSession
from typeguard import check_type

from landtransportsg import PublicTransport
from landtransportsg.public_transport.types import (
    BusArrivalDict,
    BusServicesDict,
    BusRoutesDict,
    BusStopsDict,
    FacilitiesMaintenanceDict,
    PlannedBusRoutesDict,
    StationCrowdDensityRealTimeDict,
    StationCrowdDensityForecastDict,
    TaxiAvailabilityDict,
    TaxiStandsDict,
    TrainServiceAlertsDict,
)

from . import TEST_ACCOUNT_KEY
from .mocks.api_response_public_transport import (
    APIResponseBusArrival,
    APIResponseBusRoutes,
    APIResponseBusServices,
    APIResponseBusStops,
    APIResponseFacilitiesMaintenance,
    APIResponsePlannedBusRoutes,
    APIResponseStationCrowdDensityForecast,
    APIResponseStationCrowdDensityRealTime,
    APIResponseTaxiAvailability,
    APIResponseTaxiStands,
    APIResponseTrainServiceAlerts,
)

# constants for testing valid bus_stop_code, service_number and train_line
GOOD_BUS_STOP_CODE = '83139'
GOOD_SERVICE_NUMBER = '15'
GOOD_TRAIN_LINE = 'NSL'

GOOD_DATE = date.today() - timedelta(50)

# constants for testing bad dates
VERY_OLD_DATE = date.today() - timedelta(200)

@pytest.fixture
def client():
    return PublicTransport(TEST_ACCOUNT_KEY)

def test_train_lines(client):
    train_lines = client.train_lines()

    assert isinstance(train_lines, tuple)
    assert len(train_lines) == 11

@pytest.mark.parametrize(
    ('function', 'expected_type', 'mocked_response_class'),
    [
        (
            'bus_routes',
            list[BusRoutesDict],
            APIResponseBusRoutes,
        ),
        (
            'bus_services',
            list[BusServicesDict],
            APIResponseBusServices,
        ),
        (
            'bus_stops',
            list[BusStopsDict],
            APIResponseBusStops,
        ),
        (
            'facilities_maintenance',
            list[FacilitiesMaintenanceDict],
            APIResponseFacilitiesMaintenance,
        ),
        (
            'planned_bus_routes',
            list[PlannedBusRoutesDict],
            APIResponsePlannedBusRoutes,
        ),
        (
            'taxi_availability',
            list[TaxiAvailabilityDict],
            APIResponseTaxiAvailability,
        ),
        (
            'taxi_stands',
            list[TaxiStandsDict],
            APIResponseTaxiStands,
        ),
        (
            'train_service_alerts',
            TrainServiceAlertsDict,
            APIResponseTrainServiceAlerts,
        ),
    ],
)
def test_class_function_with_mocked_response_class(
    client,
    monkeypatch,
    function,
    expected_type,
    mocked_response_class,
):
    def mock_requests_get(*args, **kwargs):
        return mocked_response_class()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    result = getattr(client, function)()

    assert check_type(result, expected_type) == result

@pytest.mark.parametrize(
    ('bus_stop_code', 'service_number'),
    [
        (GOOD_BUS_STOP_CODE, GOOD_SERVICE_NUMBER),
        (GOOD_BUS_STOP_CODE, None),
    ],
)
def test_bus_arrival(
    client,
    monkeypatch,
    bus_stop_code,
    service_number,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseBusArrival()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    bus_arrival = client.bus_arrival(
        bus_stop_code=bus_stop_code,
        service_number=service_number,
    )

    assert check_type(bus_arrival, BusArrivalDict) == bus_arrival

    assert bus_arrival['BusStopCode'] == GOOD_BUS_STOP_CODE

    services = bus_arrival['Services']
    found_service_number_in_services = True \
        if service_number is None or len(services) == 0 else False
    for s in services:
        if s['ServiceNo'] == GOOD_SERVICE_NUMBER:
            found_service_number_in_services = True
    assert found_service_number_in_services is True

@pytest.mark.parametrize(
    ('bus_stop_code', 'service_number'),
    [
        ('8313', GOOD_SERVICE_NUMBER), # 4-character bus_stop_code
        ('foobr', GOOD_SERVICE_NUMBER), # non-number bus_stop_code
    ],
)
def test_bus_arrival_with_invalid_inputs(client, bus_stop_code, service_number):
    with pytest.raises(ValueError):
        _ = client.bus_arrival(
            bus_stop_code=bus_stop_code,
            service_number=service_number,
        )

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
    mock_requests_link_response,
    function,
    dt,
):
    result = getattr(client, function)(dt=dt)

    assert isinstance(result, str)

@pytest.mark.parametrize(
    ('function', 'dt'),
    [
        ('passenger_volume_by_bus_stops', VERY_OLD_DATE),
        ('passenger_volume_by_origin_destination_bus_stops', VERY_OLD_DATE),
        (
            'passenger_volume_by_origin_destination_train_stations',
            VERY_OLD_DATE,
        ),
        ('passenger_volume_by_train_stations', VERY_OLD_DATE),
    ],
)
def test_class_passenger_volume_function_with_invalid_inputs(
    client,
    function,
    dt,
):
    with pytest.raises(ValueError):
        _ = getattr(client, function)(dt=dt)

@pytest.mark.parametrize(
    ('function', 'expected_type', 'mocked_response_class'),
    [
        (
            'station_crowd_density_real_time',
            list[StationCrowdDensityRealTimeDict],
            APIResponseStationCrowdDensityRealTime,
        ),
        (
            'station_crowd_density_forecast',
            list[StationCrowdDensityForecastDict],
            APIResponseStationCrowdDensityForecast,
        ),
    ],
)
def test_station_crowd_density_class_function(
    client,
    monkeypatch,
    function,
    expected_type,
    mocked_response_class,
):
    def mock_requests_get(*args, **kwargs):
        return mocked_response_class()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    result = getattr(client, function)(train_line=GOOD_TRAIN_LINE)

    assert check_type(result, expected_type) == result

@pytest.mark.parametrize(
    ('function', 'train_line'),
    [
        ('station_crowd_density_real_time', '12'), # invalid train_line
        ('station_crowd_density_real_time', 'NS'), # incomplete train_line
        ('station_crowd_density_forecast', '12'), # invalid train_line
        ('station_crowd_density_forecast', 'NS'), # incomplete train_line
    ],
)
def test_station_crowd_density_class_function_invalid_inputs(
    client,
    function,
    train_line
):
    with pytest.raises(ValueError):
        _ = getattr(client, function)(train_line=train_line)
