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

"""Constants for all Geospatial-related APIs."""

from ..constants import BASE_API_ENDPOINT

GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT = f'{
    BASE_API_ENDPOINT
}/GeospatialWholeIsland'

GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS = (
    'ArrowMarking',
    'Bollard',
    'BusStopLocation',
    'ControlBox',
    'ConvexMirror',
    'CoveredLinkWay',
    'CyclingPath',
    'DetectorLoop',
    'ERPGantry',
    'Footpath',
    'GuardRail',
    'KerbLine',
    'LampPost',
    'LaneMarking',
    'ParkingStandardsZone',
    'PassengerPickupBay',
    'PedestrainOverheadbridge_UnderPass',
    'RailConstruction',
    'Railing',
    'RetainingWall',
    'RoadCrossing',
    'RoadHump',
    'RoadSectionLine',
    'SchoolZone',
    'SilverZone',
    'SpeedRegulatingStrip',
    'StreetPaint',
    'TaxiStand',
    'TrafficLight',
    'TrafficSign',
    'TrainStation',
    'TrainStationExit',
    'VehicularBridge_Flyover_Underpass',
    'WordMarking',
)

__all__ = [
    'GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT',
    'GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS',
]
