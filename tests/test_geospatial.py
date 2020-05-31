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

"""Test that the Geospatial class is working properly."""

import pytest
from datetime import date, timedelta
from requests import Session
from requests.exceptions import HTTPError

from landtransportsg import Geospatial
from landtransportsg.exceptions import APIError

from . import TEST_ACCOUNT_KEY

@pytest.fixture
def client():
    return Geospatial(TEST_ACCOUNT_KEY)

def test_geospatial_whole_island(
    client,
    mock_requests_value_str_response,
):
    geospatial_whole_island = client.geospatial_whole_island(
        'ArrowMarking',
    )

    assert isinstance(geospatial_whole_island, str)

@pytest.mark.parametrize(
    'geospatial_layer_id',
    [
        None, # unspecified ID
        12345, # non-string ID
        'ArrowMarkings', # invalid ID
    ],
)
def test_geospatial_whole_island_with_bad_inputs(client, geospatial_layer_id):
    with pytest.raises(ValueError):
        _ = client.geospatial_whole_island(geospatial_layer_id)
