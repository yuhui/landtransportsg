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

"""Public Transport custom types.
    """

from datetime import datetime
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

class _NextBusDict(TypedDict):
    """Type definition for BusArrivalDict"""

    OriginCode: str
    """Reference code of the first bus stop where this bus started its service.
    Example: "77009".
    """
    DestinationCode: str
    """Reference code of the last bus stop where this bus will terminate its service.
    Example: "77131".
    """
    EstimatedArrival: datetime
    """Date-time of this bus' estimated time of arrival.
    Example: datetime(2017, 4, 29, 7, 20, 24).
    """
    Monitored: int
    """Indicates if the bus arrival time is based on the schedule from operators:
    - 0 - Value from EstimatedArrival is based on schedule.
    - 1 - Value from EstimatedArrival is estimated based on bus location.
    Example: 1.
    """
    Latitude: str
    """Current estimated location latitude coordinate of this bus at point of published data.
    Example: "1.42117943692586".
    """
    Longitude: str
    """Current estimated location longitude coordinate of this bus at point of published data.
    Example: "103.831477233098".
    """
    VisitNumber: str
    """Ordinal value of the nth visit of this vehicle at this bus stop.
    - "1" - 1st visit.
    - "2" - 2nd visit.
    - etc.
    Example: "1".
    """
    Load: str
    """Current bus occupancy / crowding level:
    - "SEA" - for Seats Available.
    - "SDA" - for Standing Available.
    - "LSD" - for Limited Standing.
    Example: "SEA".
    """
    Feature: str
    """Indicates if bus is wheel-chair accessible:
    - "WAB".
    - blank.
    Example: "WAB".
    """
    Type: str
    """Vehicle type:
    - "SD" - for Single Deck.
    - "DD" - for Double Deck.
    - "BD" - for Bendy.
    Example: "SD".
    """
class BusArrivalDict(TypedDict):
    """Type definition for bus_arrival()"""

    ServiceNo: str
    """Bus service number.
    Example: "15".
    """
    Operator: str
    """Public Transport Operator Codes:
    - "SBST" - for SBS Transit.
    - "SMRT" - for SMRT Corporation.
    - "TTS" - for Tower Transit Singapore.
    - "GAS" - for Go Ahead Singapore.
    Example: "GAS".
    """
    NextBus: _NextBusDict
    """Bus-level attributes of the 1st next oncoming bus."""
    NextBus2: _NextBusDict
    """Bus-level attributes of the 2nd next oncoming bus."""
    NextBus3: _NextBusDict
    """Bus-level attributes of the 3rd next oncoming bus."""

class BusServicesDict(TypedDict):
    """Type definition for bus_services()"""

    ServiceNo: str
    """The bus service number.
    Example: "107M".
    """
    Operator: str
    """Operator for this bus service.
    Example: "SBST".
    """
    Direction: int
    """The direction in which the bus travels (1 or 2), loop services only have 1 direction.
    Example: 1.
    """
    Category: str
    """Category of the SBS bus service: EXPRESS, FEEDER, INDUSTRIAL, TOWNLINK, TRUNK, 2 TIER FLAT FEE, FLAT FEE $1.10 (or $1.90, $3.50, $3.80).
    Example: "TRUNK".
    """
    OriginCode: str
    """Bus stop code for first bus stop.
    Example: "64009".
    """
    DestinationCode: str
    """Bus stop code for last bus stop (similar as first stop for loop services).
    Example: "64009".
    """
    AM_Peak_Freq: str
    """Freq of dispatch for AM Peak 0630H - 0830H (range in minutes).
    Example: "5-08".
    """
    AM_Offpeak_Freq: str
    """Freq of dispatch for AM Off-Peak 0831H - 1659H (range in minutes).
    Example: "10-16".
    """
    PM_Peak_Freq: str
    """Freq of dispatch for PM Peak 1700H - 1900H (range in minutes).
    Example: "8-10".
    """
    PM_Offpeak_Freq: str
    """Freq of dispatch for PM Off-Peak after 1900H (range in minutes).
    Example: "12-15".
    """
    LoopDesc: str
    """Location at which the bus service loops, empty if not a loop service.
    Example: "Raffles Blvd".
    """

class BusRoutesDict(TypedDict):
    """Type definition for bus_routes()"""

    ServiceNo: str
    """The bus service number.
    Example: "107M".
    """
    Operator: str
    """Operator for this bus service.
    Example: "SBST".
    """
    Direction: int
    """The direction in which the bus travels (1 or 2), loop services only have 1 direction.
    Example: 1.
    """
    StopSequence: int
    """The i-th bus stop for this route.
    Example: 28.
    """
    BusStopCode: str
    """The unique 5-digit identifier for this physical bus stop.
    Example: "01219".
    """
    Distance: float
    """Distance travelled by bus from starting location to this bus stop (in kilometres).
    Example: 10.3.
    """
    WD_FirstBus: str
    """Scheduled arrival of first bus on weekdays.
    Example: "2025".
    """
    WD_LastBus: str
    """Scheduled arrival of last bus on weekdays.
    Example: "2352".
    """
    SAT_FirstBus: str
    """Scheduled arrival of first bus on Saturdays.
    Example: "1427".
    """
    SAT_LastBus: str
    """Scheduled arrival of last bus on Saturdays.
    Example: "2349".
    """
    SUN_FirstBus: str
    """Scheduled arrival of first bus on Sundays.
    Example: "0620".
    """
    SUN_LastBus: str
    """Scheduled arrival of last bus on Sundays.
    Example: "2349".
    """

class BusStopsDict(TypedDict):
    """Type definition for bus_stops()"""

    BusStopCode: str
    """The unique 5-digit identifier for this physical bus stop.
    Example: "01219".
    """
    RoadName: str
    """The road on which this bus stop is located.
    Example: "Victoria St".
    """
    Description: str
    """Landmarks next to the bus stop (if any) to aid in identifying this bus stop.
    Example: "Hotel Grand Pacific".
    """
    Latitude: float
    """Latitude location coordinates for this bus stop.
    Example: 1.29685.
    """
    Longitude: float
    """Latitude location coordinates for this bus stop.
    Example: 103.853.
    """

class PlatformCrowdDensityRealTimeDict(TypedDict):
    """Type definition for platform_crowd_density_real_time()"""

    Station: str
    """Station code.
    Example: "EW13".
    """
    StartTime: datetime
    """The start of the time interval.
    Example: datetime(2021, 9, 15, 9, 40, 0).
    """
    EndTime: datetime
    """The end of the time interval.
    Example: datetime(2021, 9, 15, 9, 50, 0).
    """
    CrowdLevel: str
    """The crowdedness level indicates:
    - "l" - low.
    - "h" - high.
    - "m" - moderate.
    - blank.
    Example: "l".
    """

class _PlatformCrowdDensityForecastStationIntervalDict(TypedDict):
    """Type definition for PlatformCrowdDensityForecastStationDict"""

    Start: datetime
    """The start of the time interval.
    Example: datetime(2021, 9, 15, 0, 0, 0).
    """
    CrowdLevel: str
    """The crowdedness level indicates:
    - "l" - low.
    - "h" - high.
    - "m" - moderate.
    - blank.
    Example: "l".
    """
class _PlatformCrowdDensityForecastStationDict(TypedDict):
    """Type definition for PlatformCrowdDensityForecastDict"""

    Station: str
    """Station code.
    Example: "EW13".
    """
    Interval: list[_PlatformCrowdDensityForecastStationIntervalDict]
    """Array of platform crowd density forecast per station per time interval."""
class PlatformCrowdDensityForecastDict(TypedDict):
    """Type definition for platform_crowd_density_forecast()"""

    Date: datetime
    """Midnight of the forecasted date.
    Example: datetime(2021, 9, 15, 0, 0, 0).
    """
    Stations: list[_PlatformCrowdDensityForecastStationDict]
    """Array of platform crowd density forecast per station."""

class TaxiAvailabilityDict(TypedDict):
    """Type definition for taxi_availability()"""

    Latitude: float
    """Latitude location coordinates.
    Example: 1.35667.
    """
    Longitude: float
    """Longitude location coordinates.
    Example: 103.93314.
    """

class TaxiStandsDict(TypedDict):
    """Type definition for taxi_stands()"""

    TaxiCode: str
    """Code representation of Taxi facility.
    Example: "A01".
    """
    Latitude: float
    """Latitude map coordinates for the taxi stand.
    Example: 1.303980684.
    """
    Longitude: float
    """Longitude map coordinates for the taxi stand.
    Example: 103.9191828.
    """
    Bfa: str
    """Indicate whether the Taxi stand is barrier free.
    Example: "Yes".
    """
    Ownership: str
    """Indicate the owner of the Taxi stand.
    - "LTA" - Land Transport Authority.
    - "CCS" - Clear Channel Singapore.
    - "Private" - Taxi facilities that are constructed and maintained by private entities (e.g. developers/owners of shopping malls, commercial buildings).
    Example: "LTA".
    """
    Type: str
    """Indicate the type of the Taxi stand.
    - "Stand" - allows Taxis to queue in the taxi bays and wait for passengers.
    - "Stop" - allow Taxis to perform immediate pick up and drop off of passengers.
    Example: "Stand".
    """
    Name: str
    """Name of Taxi facility.
    Example: "Orchard Rd along driveway of Lucky Plaza".
    """

class TrainServiceAlertsDict(TypedDict):
    """Type definition for train_service_alerts()"""

    Status: int
    """Indicates if train service is unavailable:
    - 1 - for Normal Train Service.
    - 2 - for Disrupted Train Service.
    Example: 1.
    """
    Line: str
    """Train network line affected:
    - "CCL" - for Circle Line.
    - "CEL" - for Circle Line Extension - BayFront, Marina Bay.
    - "CGL" - for Changi Extension - Expo, Changi Airport.
    - "DTL" - for Downtown Line.
    - "EWL" - for East West Line.
    - "NEL" - for North East Line.
    - "NSL" - for North South Line.
    - "PEL" - for Punggol LRT East Loop.
    - "PWL" - for Punggol LRT West Loop.
    - "SEL" - for Sengkang LRT East Loop.
    - "SWL" - For Sengkang LRT West Loop.
    - "BPL" - for Bukit Panjang LRT.
    Example: "NEL".
    """
    Direction: str
    """Indicates direction of service unavailability on the affected line:
    - "Both".
    - towards station name.
    Example: "Punggol".
    """
    Stations: str
    """Indicates the list of affected stations on the affected line.
    Example: "NE1,NE3,NE4,NE5,NE6".
    """
    FreePublicBus: str
    """Indicates the list of affected stations where free boarding onto normal public bus services are available.
    - station code.
    - "Free bus service island wide".
    Example: "NE1,NE3,NE4,NE5,NE6".
    """
    FreeMRTShuttle: str
    """Indicates the list of affected stations where free MRT shuttle services^ are available.
    - station code.
    - "EW21|CC22,EW23,EW24|NS1,EW27;NS9,NS13,NS16,NS17|CC15;EW8|CC9,EW5,EW2;NS1|EW24,NS4|BP1*".
    Example: "NE1,NE3,NE4,NE5,NE6".
    """
    MRTShuttleDirection: str
    """Indicates the direction of free MRT shuttle services available:
    - "Both".
    - towards station name.
    Example: "Punggol".
    """
    Message: str
    """Travel advisory notification service for train commuters, published by LTA. This notice is also broadcasted to commuters via the Find-My-Way module in MyTransport mobile app.
    - Content.
    - CreatedDate.
    Example: "1710hrs: NEL - No train service between Harbourfront to Dhoby Ghaut stations towards Punggol station due to a signalling fault. Free bus rides are available at designated bus stops. 2017-12-01 17:54:21".
    """

__all__ = [
    '_NextBusDict',
    'BusArrivalDict',
    'BusServicesDict',
    'BusRoutesDict',
    'BusStopsDict',
    'PlatformCrowdDensityRealTimeDict',
    '_PlatformCrowdDensityForecastStationIntervalDict',
    '_PlatformCrowdDensityForecastStationDict',
    'PlatformCrowdDensityForecastDict',
    'TaxiAvailabilityDict',
    'TaxiStandsDict',
    'TrainServiceAlertsDict',
]
