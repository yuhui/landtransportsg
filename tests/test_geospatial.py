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
from .mocks.api_response_geospatial_whole_island \
    import APIResponseGeospatialWholeIsland

# constants for testing valid geospatial_layer_id
GOOD_GEOSPATIAL_LAYER_ID = 'ArrowMarking'

# constants for testing bad geospatial_layer_id
BAD_GEOSPATIAL_LAYER_ID = 'ArrowMarkings'

@pytest.fixture
def mock_requests_geospatial_whole_island_response(monkeypatch):
    """Requests.Session().get() mocked to return sample GeospatialWholeIsland
    API response.
    """
    def mock_requests_get(*args, **kwargs):
        return APIResponseGeospatialWholeIsland()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def client():
    return Geospatial(TEST_ACCOUNT_KEY)

def test_geospatial_whole_island(
    client,
    mock_requests_geospatial_whole_island_response,
):
    geospatial_whole_island = client.geospatial_whole_island(
        GOOD_GEOSPATIAL_LAYER_ID,
    )

    assert isinstance(geospatial_whole_island, str)

    geospatial_layer_zip_filename = '/{}.zip'.format(GOOD_GEOSPATIAL_LAYER_ID)
    assert geospatial_layer_zip_filename in geospatial_whole_island

@pytest.mark.parametrize(
    'geospatial_layer_id',
    [
        None,
        12345,
        BAD_GEOSPATIAL_LAYER_ID,
    ],
)
def test_geospatial_whole_island_with_bad_inputs(client, geospatial_layer_id):
    with pytest.raises(ValueError):
        _ = client.geospatial_whole_island(geospatial_layer_id)

def test_geospatial_whole_island_with_bad_value(
    client,
    mock_requests_value_str_bad_value_response,
):
    with pytest.raises(APIError):
        _ = client.geospatial_whole_island(GOOD_GEOSPATIAL_LAYER_ID)

def test_geospatial_whole_island_with_missing_link(
    client,
    mock_requests_value_str_missing_link_response,
):
    with pytest.raises(APIError):
        _ = client.geospatial_whole_island(GOOD_GEOSPATIAL_LAYER_ID)

def test_geospatial_whole_island_with_bad_link(
    client,
    mock_requests_value_str_bad_link_response,
):
    with pytest.raises(APIError):
        _ = client.geospatial_whole_island(GOOD_GEOSPATIAL_LAYER_ID)
