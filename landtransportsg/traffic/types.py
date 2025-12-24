# Copyright 2024 Yuhui. All rights reserved.
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

"""Traffic custom types."""

from datetime import date, datetime
from typing import TypedDict

class CarParkAvailabilityDict(TypedDict):
    """Type definition for carpark_availability()"""

    CarParkID: str
    """A unique code for this carpark.

    :example: (LTA) "1"
    :example: (URA) "A0007"
    :example: (HDB) "KB7"
    """
    Area: str | None
    """Area of development / building:

    - blank
    - "Orchard"
    - "Marina"
    - "Harbfront"
    - "JurongLakeDistrict"

    :example: (LTA) "Marina"
    :example: (URA) ""
    :example: (HDB) ""
    """
    Development: str
    """Major landmark or address where carpark is located.

    :example: (LTA) "Suntec City"
    :example: (URA) "ANGULLIA PARK OFF STREET"
    :example: (HDB) "BLK 69 GEYLANG BAHRU"
    """
    Location: str
    """Latitude and Longitude map coordinates.

    :example: (LTA) "1.29375 103.85718"
    :example: (URA) "1.3114801086966732 103.77050251295184"
    :example: (HDB) "1.3016364093613493 103.7967913879039"
    """
    AvailableLots: int
    """Number of lots available at point of data retrieval.

    :example: 352
    """
    LotType: str
    """Type of lots:

    - "C" - for Cars
    - "H" - for Heavy Vehicles
    - "Y" - for Motorcycles

    :example: "C"
    """
    Agency: str
    """Agencies.

    :example: (LTA) "LTA"
    :example: (URA) "URA"
    :example: (HDB) "HDB"
    """

class EstimatedTravelTimesDict(TypedDict):
    """Type definition for estimated_travel_times()"""

    Name: str
    """Expressway.

    :example: "AYE"
    """
    Direction: int
    """Direction of travel:

    - 1 - Travelling from east to west, or south to north.
    - 2 - Travelling from west to east, or north to south.

    :example: 1
    """
    FarEndPoint: str
    """The final end point of this whole expressway in current direction of \
        travel.

    :example: "TUAS CHECKPOINT"
    """
    StartPoint: str
    """Start point of this current segment.

    :example: "AYE/MCE INTERCHANGE"
    """
    EndPoint: str
    """End point of this current segment.

    :example: "TELOK BLANGAH RD"
    """
    EstTime: int
    """Estimated travel time in minutes.

    :example: 2
    """

class FaultyTrafficLightsDict(TypedDict):
    """Type definition for faulty_traffic_lights()"""

    AlarmID: str
    """Technical alarm ID.

    :example: "GL703034136"
    """
    NodeID: str
    """A unique code to represent each unique traffic light node.

    :example: "703034136"
    """
    Type: int
    """Type of the technical alarm:

    - 4 - blackout.
    - 13 - flashing yellow.

    :example: 13
    """
    StartDate: datetime | None
    """Start timestamp of the alarm.

    :example: datetime(2014, 4, 12, 1, 58, 0)
    """
    EndDate: datetime | None
    """End timestamp of the alarm. (Blank string if this is not a scheduled \
        maintenance.)

    :example: blank
    """
    Message: str
    """Canning Message.

    :example: "(23/1)8:58 Flashing Yellow at Bedok North Interchange/Bedok \
        North Street 1 Junc."
    """

class RoadOpeningsDict(TypedDict):
    """Type definition for road_openings()"""

    EventID: str
    """ID for this road opening event.

    :example: "RMAPP-201603-0900"
    """
    StartDate: date
    """Start date for the works to be performed for this road opening.

    :example: date(2016, 3, 31)
    """
    EndDate: date
    """End date for the works to be performed for this road opening.

    :example: date(2016, 9, 30)
    """
    SvcDept: str
    """Department or company performing this road work.

    :example: "SP POWERGRID LTD - CUSTOMER PROJ (EAST)"
    """
    RoadName: str
    """Name of new road to be opened.

    :example: "AH SOO GARDEN"
    """
    Other: str
    """Additional information or messages.

    :example: "For details, please call 62409237"
    """

class RoadWorksDict(TypedDict):
    """Type definition for road_works()"""

    EventID: str
    """ID for this road work.

    :example: "RMAPP-201512-0217"
    """
    StartDate: date
    """Start date for the works to be performed for this road work.

    :example: date(2016, 3, 31)
    """
    EndDate: date
    """End date for the works to be performed for this road work.

    :example: date(2016, 9, 30)
    """
    SvcDept: str
    """Department or company performing this road work.

    :example: "SP POWERGRID LTD - CUSTOMER PROJ (EAST)"
    """
    RoadName: str
    """Name of road where work is being performed.

    :example: "AH SOO GARDEN"
    """
    Other: str
    """Additional information or messages.

    :example: "For details, please call 62409237"
    """

class TrafficImagesDict(TypedDict):
    """Type definition for traffic_images()"""

    CameraID: str
    """A unique ID for this camera.

    :example: "5795"
    """
    Latitude: float
    """Latitude map coordinates.

    :example: 1.326024822
    """
    Longitude: float
    """Longitude map coordinates.

    :example: 103.905625
    """
    ImageLink: str
    """Link for downloading this image. Link will expire after 5 minutes.

    :example: https://dm-traffic-camera-itsc.s3.amazonaws.com/2020-04-01/09-24/1001_0918_20200401092500_e0368e.jpg?x-amz-security-token=..
    """

class TrafficIncidentsDict(TypedDict):
    """Type definition for traffic_incidents()"""

    Type: str
    """Incident Types:

    - "Accident"
    - "Road Works"
    - "Vehicle Breakdown"
    - "Weather"
    - "Obstacle"
    - "Road Block"
    - "Heavy Traffic"
    - "Misc."
    - "Diversion"
    - "Unattended Vehicle"

    :example: "Vehicle Breakdown"
    """
    Latitude: float
    """Latitude map coordinates for the start point of this road incident.

    :example: 1.30398068448214
    """
    Longitude: float
    """Longitude map coordinates for the start point of this road incident.

    :example: 103.919182834377
    """
    Message: str
    """Description message for this incident.

    :example: "(29/3)18:22 Vehicle breakdown on ECP (towards Changi Airport) after Still Rd Sth Exit. Avoid lane 3."
    """

class TrafficSpeedBandsDict(TypedDict):
    """Type definition for traffic_speed_bands()"""

    LinkID: str
    """Unique ID for this stretch of road.

    :example: "103046935"
    """
    RoadName: str
    """Road Name.

    :example: "SERANGOON ROAD"
    """
    RoadCategory: str
    """Road Category.

    :example: "E"
    """
    SpeedBand: int
    """Speed Bands Information:

    - 1 - indicates speed range from 0 < 9.
    - 2 - indicates speed range from 10 < 19.
    - 3 - indicates speed range from 20 < 29.
    - 4 - indicates speed range from 30 < 39.
    - 5 - indicates speed range from 40 < 49.
    - 6 - indicates speed range from 50 < 59.
    - 7 - indicates speed range from 60 < 69.
    - 8 - speed range from 70 or more.

    :example: 2
    """
    MinimumSpeed: int
    """Minimum speed in km/h.

    :example: 10
    """
    MaximumSpeed: int
    """Maximum speed in km/h.

    :example: 19
    """
    StartLon: float
    """Longitude map coordinates for start point for this stretch of road.

    :example: 103.86246461405193
    """
    StartLat: float
    """Latitude map coordinates for start point for this stretch of road.

    :example: 1.3220591510051254
    """
    EndLon: float
    """Longitude map coordinates for end point for this stretch of road.

    :example: 103.86315591911669
    """
    EndLat: float
    """Latitude map coordinates for end point for this stretch of road.

    :example: 1.3215993547809128
    """

class VMSDict(TypedDict):
    """Type definition for vms()"""

    EquipmentID: str
    """EMAS equipment ID.

    :example: "amvms_v9104"
    """
    Latitude: float
    """Latitude map coordinates of electronic signboard.

    :example: 1.3927176306916775
    """
    Longitude: float
    """Longitude map coordinates of electronic signboard.

    :example: 103.82618266340947
    """
    Message: str
    """Variable Message being displayed on the EMAS display.

    :example: "VEH BREAKDOWN SH,AFT U.THOMSON"
    """

__all__ = [
    'CarParkAvailabilityDict',
    'EstimatedTravelTimesDict',
    'FaultyTrafficLightsDict',
    'RoadOpeningsDict',
    'RoadWorksDict',
    'TrafficImagesDict',
    'TrafficIncidentsDict',
    'TrafficSpeedBandsDict',
    'VMSDict',
]
