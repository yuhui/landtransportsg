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

"""Constants for all Traffic-related APIs."""

from ..constants import (
    BASE_API_ENDPOINT,
    CACHE_MAXSIZE,
    CACHE_ONE_MINUTE,
    CACHE_TWO_MINUTES,
    CACHE_FIVE_MINUTES,
    CACHE_ONE_DAY,
)

CARPARK_AVAILABILITY_API_ENDPOINT = '{}/CarParkAvailabilityv2'.format(
    BASE_API_ENDPOINT,
)
ERP_RATES_API_ENDPOINT = '{}/ERPRates'.format(BASE_API_ENDPOINT)
ESTIMATED_TRAVEL_TIMES_API_ENDPOINT = '{}/EstTravelTimes'.format(
    BASE_API_ENDPOINT,
)
FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT = '{}/FaultyTrafficLights'.format(
    BASE_API_ENDPOINT,
)
ROAD_OPENINGS_API_ENDPOINT = '{}/RoadOpenings'.format(BASE_API_ENDPOINT)
ROAD_WORKS_API_ENDPOINT = '{}/RoadWorks'.format(BASE_API_ENDPOINT)
TRAFFIC_IMAGES_API_ENDPOINT = '{}/Traffic-Images'.format(BASE_API_ENDPOINT)
TRAFFIC_INCIDENTS_API_ENDPOINT = '{}/TrafficIncidents'.format(
    BASE_API_ENDPOINT,
)
TRAFFIC_SPEED_BANDS_API_ENDPOINT = '{}/TrafficSpeedBandsv2'.format(
    BASE_API_ENDPOINT,
)
VMS_API_ENDPOINT = '{}/VMS'.format(BASE_API_ENDPOINT)
