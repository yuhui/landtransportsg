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

"""Test that the Active Mobility class is working properly."""

import pytest

from landtransportsg import ActiveMobility

from . import TEST_ACCOUNT_KEY

GOOD_LATITUDE = 1.364897
GOOD_LONGITUDE = 103.766094
GOOD_DISTANCE = 1.2

BAD_LATITUDE = 'foo'
BAD_LONGITUDE = 'bar'
BAD_DISTANCE = 'stamp'

@pytest.fixture(scope='module')
def client():
    return ActiveMobility(TEST_ACCOUNT_KEY)

@pytest.mark.parametrize(
    'args',
    [
        ([GOOD_LATITUDE, GOOD_LONGITUDE]),
        ([GOOD_LATITUDE, GOOD_LONGITUDE, GOOD_DISTANCE]),
    ],
)
def test_bicycle_parking(client, mock_requests_value_list_response, args):
    bicycle_parking_locations = client.bicycle_parking(*args)

    assert isinstance(bicycle_parking_locations, list)
    assert len(bicycle_parking_locations) >= 0

    for v in bicycle_parking_locations:
        assert isinstance(v, dict)

@pytest.mark.parametrize(
    'args',
    [
        ([GOOD_LATITUDE, BAD_LONGITUDE]),
        ([BAD_LATITUDE, GOOD_LONGITUDE]),
        ([GOOD_LATITUDE, GOOD_LONGITUDE, BAD_DISTANCE]),
    ],
)
def test_bicycle_parking_with_bad_latitude_longitude(client, args):
    with pytest.raises(ValueError):
        _ = client.bicycle_parking(*args)
