# Copyright 2019-2025 Yuhui
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

# pylint: disable=invalid-name,missing-function-docstring,redefined-outer-name,unused-argument,redefined-outer-name,unused-argument

"""Test that the Active Mobility class is working properly."""

import pytest
from requests_cache import CachedSession
from typeguard import check_type

from landtransportsg import ActiveMobility
from landtransportsg.active_mobility.types import BicycleParkingDict

from . import TEST_ACCOUNT_KEY
from .mocks.api_response_active_mobility import APIResponseBicycleParking

GOOD_LATITUDE = 1.364897
GOOD_LONGITUDE = 103.766094
GOOD_DISTANCE = 1.2

NEGATIVE_DISTANCE = -1.2

@pytest.fixture(scope='module')
def client():
    return ActiveMobility(TEST_ACCOUNT_KEY)

@pytest.mark.parametrize(
    'kwargs',
    [
        (
            {
                'latitude': GOOD_LATITUDE,
                'longitude': GOOD_LONGITUDE,
            }
        ),
        (
            {
                'latitude': GOOD_LATITUDE,
                'longitude': GOOD_LONGITUDE,
                'distance': GOOD_DISTANCE,
            }
        ),
        (
            {
                'latitude': GOOD_LATITUDE,
                'longitude': GOOD_LONGITUDE,
                'distance': None,
            }
        ),
    ],
)
def test_bicycle_parking(
    client,
    monkeypatch,
    kwargs,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseBicycleParking()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    bicycle_parking_locations = client.bicycle_parking(**kwargs)

    assert check_type(
        bicycle_parking_locations,
        list[BicycleParkingDict,
    ]) == bicycle_parking_locations

@pytest.mark.parametrize(
    'kwargs',
    [
        (
            {
                'latitude': GOOD_LATITUDE,
                'longitude': GOOD_LONGITUDE,
                'distance': NEGATIVE_DISTANCE,
            }
        ),
    ],
)
def test_bicycle_parking_with_invalid_inputs(client, kwargs):
    with pytest.raises(ValueError):
        _ = client.bicycle_parking(**kwargs)
