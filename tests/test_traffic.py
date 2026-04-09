# Copyright 2019-2026 Yuhui
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

"""Test that the Traffic class is working properly."""

from os import getenv

import pytest
from dotenv import load_dotenv
from requests_cache import CachedSession
from typeguard import check_type

from landtransportsg import Traffic
from landtransportsg.traffic.types import (
    CarParkAvailabilityDict,
    EstimatedTravelTimesDict,
    FaultyTrafficLightsDict,
    FloodAlertsDict,
    RoadOpeningsDict,
    RoadWorksDict,
    TrafficImagesDict,
    TrafficIncidentsDict,
    TrafficSpeedBandsDict,
    VMSDict,
)

from .mocks.api_response_traffic import (
    APIResponseCarParkAvailability,
    APIResponseEstimatedTravelTimes,
    APIResponseFaultyTrafficLights,
    APIResponseFloodAlerts,
    APIResponseRoadOpenings,
    APIResponseRoadWorks,
    APIResponseTrafficImages,
    APIResponseTrafficIncidents,
    APIResponseTrafficSpeedBands,
    APIResponseVMS,
)

@pytest.fixture(scope='module')
def client():
    load_dotenv()
    api_key = getenv('ACCOUNT_KEY')
    return Traffic(api_key)

@pytest.mark.parametrize(
    ('function', 'expected_type', 'mocked_response_class'),
    [
        (
            'carpark_availability',
            list[CarParkAvailabilityDict],
            APIResponseCarParkAvailability,
        ),
        (
            'estimated_travel_times',
            list[EstimatedTravelTimesDict],
            APIResponseEstimatedTravelTimes,
        ),
        (
            'faulty_traffic_lights',
            list[FaultyTrafficLightsDict],
            APIResponseFaultyTrafficLights,
        ),
        (
            'flood_alerts',
            list[FloodAlertsDict],
            APIResponseFloodAlerts,
        ),
        (
            'road_openings',
            list[RoadOpeningsDict],
            APIResponseRoadOpenings,
        ),
        (
            'road_works',
            list[RoadWorksDict],
            APIResponseRoadWorks,
        ),
        (
            'traffic_images',
            list[TrafficImagesDict],
            APIResponseTrafficImages,
        ),
        (
            'traffic_incidents',
            list[TrafficIncidentsDict],
            APIResponseTrafficIncidents,
        ),
        (
            'traffic_speed_bands',
            list[TrafficSpeedBandsDict],
            APIResponseTrafficSpeedBands,
        ),
        (
            'vms',
            list[VMSDict],
            APIResponseVMS,
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

def test_traffic_flow(
    client,
    mock_requests_link_response,
):
    traffic_flow = client.traffic_flow()

    assert isinstance(traffic_flow, str)
