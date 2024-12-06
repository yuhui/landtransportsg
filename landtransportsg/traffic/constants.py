# Copyright 2019-2024 Yuhui. All rights reserved.
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

from ..constants import BASE_API_ENDPOINT

CARPARK_AVAILABILITY_API_ENDPOINT = f'{
    BASE_API_ENDPOINT
}/CarParkAvailabilityv2'
ESTIMATED_TRAVEL_TIMES_API_ENDPOINT = f'{BASE_API_ENDPOINT}/EstTravelTimes'
FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/FaultyTrafficLights'
ROAD_OPENINGS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/RoadOpenings'
ROAD_WORKS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/RoadWorks'
TRAFFIC_FLOW_API_ENDPOINT = f'{BASE_API_ENDPOINT}/TrafficFlow'
TRAFFIC_IMAGES_API_ENDPOINT = f'{BASE_API_ENDPOINT}/Traffic-Imagesv2'
TRAFFIC_INCIDENTS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/TrafficIncidents'
TRAFFIC_SPEED_BANDS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/v3/TrafficSpeedBands'
VMS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/VMS'

__all__ = [
    'CARPARK_AVAILABILITY_API_ENDPOINT',
    'ESTIMATED_TRAVEL_TIMES_API_ENDPOINT',
    'FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT',
    'ROAD_OPENINGS_API_ENDPOINT',
    'ROAD_WORKS_API_ENDPOINT',
    'TRAFFIC_FLOW_API_ENDPOINT',
    'TRAFFIC_IMAGES_API_ENDPOINT',
    'TRAFFIC_INCIDENTS_API_ENDPOINT',
    'TRAFFIC_SPEED_BANDS_API_ENDPOINT',
    'VMS_API_ENDPOINT',
]
