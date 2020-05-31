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

"""Test that the Traffic class is working properly."""

import pytest
from requests.exceptions import HTTPError

from landtransportsg import Traffic

from . import TEST_ACCOUNT_KEY

@pytest.fixture(scope='module')
def client():
    return Traffic(TEST_ACCOUNT_KEY)

@pytest.mark.parametrize(
    'function',
    [
        'carpark_availability',
        # 'erp_rates', # this is tested in test_class_function_with_more_than_five_hundred_records()
        'estimated_travel_times',
        'faulty_traffic_lights',
        'road_openings',
        'road_works',
        'traffic_images',
        'traffic_incidents',
        'traffic_speed_bands',
        'vms',
    ],
)
def test_class_function(client, mock_requests_value_list_response, function):
    result = getattr(client, function)()

    assert isinstance(result, list)

def test_class_function_with_more_than_five_hundred_records(client):
    """This test calls the actual API endpoint so as to be able to receive more
    than 500 entries.
    """
    result = client.erp_rates()

    assert isinstance(result, list)
    assert len(result) > 500

    for v in result:
        assert isinstance(v, dict)
