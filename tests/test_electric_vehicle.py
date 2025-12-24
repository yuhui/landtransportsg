# Copyright 2025 Yuhui
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

"""Test that the Electric Vehicle class is working properly."""

import pytest
from requests_cache import CachedSession
from typeguard import check_type

from landtransportsg import ElectricVehicle
from landtransportsg.electric_vehicle.types import EVChargingPointsDict

from . import TEST_ACCOUNT_KEY
from .mocks.api_response_electric_vehicle import APIResponseEVChargingPoints

GOOD_POSTAL_CODE = '219428'

BAD_POSTAL_CODE = '21942'
INVALID_POSTAL_CODE = 'foo'

@pytest.fixture(scope='module')
def client():
    return ElectricVehicle(TEST_ACCOUNT_KEY)

@pytest.mark.parametrize(
    'postal_code',
    [
        GOOD_POSTAL_CODE,
    ],
)
def test_ev_charging_points(
    client,
    monkeypatch,
    postal_code,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseEVChargingPoints()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    ev_charging_points = client.ev_charging_points(postal_code=postal_code)

    assert check_type(
        ev_charging_points,
        EVChargingPointsDict,
    ) == ev_charging_points

@pytest.mark.parametrize(
    'postal_code',
    [
        BAD_POSTAL_CODE,
        INVALID_POSTAL_CODE,
    ],
)
def test_ev_charging_points_with_invalid_inputs(client, postal_code):
    with pytest.raises(ValueError):
        _ = client.ev_charging_points(postal_code=postal_code)
