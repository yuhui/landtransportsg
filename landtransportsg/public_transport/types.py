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

"""Public Transport custom types."""

from datetime import date, datetime, time
from typing import TypedDict

class _NextBusDict(TypedDict):
    """Type definition for _BusArrivalServiceDict"""

    OriginCode: str
    """Reference code of the first bus stop where this bus started its service.

    :example: "77009"
    """
    DestinationCode: str
    """Reference code of the last bus stop where this bus will terminate its \
        service.

    :example: "77131"
    """
    EstimatedArrival: datetime | None
    """Date-time of this bus' estimated time of arrival.

    :example: datetime(2017, 4, 29, 7, 20, 24)
    """
    Monitored: int
    """Indicates if the bus arrival time is based on the schedule from \
        operators:

    - 0 - Value from EstimatedArrival is based on schedule.
    - 1 - Value from EstimatedArrival is estimated based on bus location.

    :example: 1
    """
    Latitude: float | None
    """Current estimated location latitude coordinate of this bus at point of \
        published data.

    :example: 1.42117943692586
    """
    Longitude: float | None
    """Current estimated location longitude coordinate of this bus at point of \
        published data.

    :example: 103.831477233098
    """
    VisitNumber: int | None
    """Ordinal value of the nth visit of this vehicle at this bus stop.

    - 1 - 1st visit.
    - 2 - 2nd visit.
    - etc.

    :example: 1
    """
    Load: str | None
    """Current bus occupancy / crowding level:

    - "SEA" - for Seats Available.
    - "SDA" - for Standing Available.
    - "LSD" - for Limited Standing.

    :example: "SEA"
    """
    Feature: str | None
    """Indicates if bus is wheel-chair accessible:

    - "WAB".
    - blank.

    :example: "WAB"
    """
    Type: str | None
    """Vehicle type:

    - "SD" - for Single Deck.
    - "DD" - for Double Deck.
    - "BD" - for Bendy.

    :example: "SD"
    """

class _BusArrivalServiceDict(TypedDict):
    """Type definition for BusArrivalDict"""

    ServiceNo: str
    """Bus service number.

    :example: "15"
    """
    Operator: str
    """Public Transport Operator Codes:

    - "SBST" - for SBS Transit.
    - "SMRT" - for SMRT Corporation.
    - "TTS" - for Tower Transit Singapore.
    - "GAS" - for Go Ahead Singapore.

    :example: "GAS"
    """
    NextBus: _NextBusDict
    """Bus-level attributes of the 1st next oncoming bus."""
    NextBus2: _NextBusDict
    """Bus-level attributes of the 2nd next oncoming bus."""
    NextBus3: _NextBusDict
    """Bus-level attributes of the 3rd next oncoming bus."""

class BusArrivalDict(TypedDict):
    """Type definition for bus_arrival()"""

    BusStopCode: str
    """Bus stop reference code.

    :example: "83139"
    """
    Services: list[_BusArrivalServiceDict]
    """Bus services."""

class _BusRoutesDict(TypedDict):
    """Type definition for BusRoutesDict and PlannedBusRoutesDict"""

    ServiceNo: str
    """The bus service number.

    :example: "107M"
    """
    Operator: str
    """Operator for this bus service.

    :example: "SBST"
    """
    Direction: int
    """The direction in which the bus travels (1 or 2), loop services only \
        have 1 direction.

    :example: 1
    """
    StopSequence: int
    """The i-th bus stop for this route.

    :example: 28
    """
    BusStopCode: str
    """The unique 5-digit identifier for this physical bus stop.

    :example: "01219"
    """
    Distance: float
    """Distance travelled by bus from starting location to this bus stop (in \
        kilometres).

    :example: 10.3
    """
    WD_FirstBus: time
    """Scheduled arrival of first bus on weekdays.

    :example: time(20, 25)
    """
    WD_LastBus: time
    """Scheduled arrival of last bus on weekdays.

    :example: time(23, 52)
    """
    SAT_FirstBus: time
    """Scheduled arrival of first bus on Saturdays.

    :example: time(14, 27
    """
    SAT_LastBus: time
    """Scheduled arrival of last bus on Saturdays.

    :example: time(23, 49
    """
    SUN_FirstBus: time
    """Scheduled arrival of first bus on Sundays.

    :example: time(6, 20)
    """
    SUN_LastBus: time
    """Scheduled arrival of last bus on Sundays.

    :example: time(23, 49
    """

class BusRoutesDict(_BusRoutesDict):
    """Type definition for bus_routes()"""

class PlannedBusRoutesDict(_BusRoutesDict):
    """Type definition for planned_bus_routes()"""

    EffectiveDate: date
    """The date when the new/updated bus routes will take effect.

    :example: date(2025, 3, 2)
    """

class BusServicesDict(TypedDict):
    """Type definition for bus_services()"""

    ServiceNo: str
    """The bus service number.

    :example: "107M"
    """
    Operator: str
    """Operator for this bus service.

    :example: "SBST"
    """
    Direction: int
    """The direction in which the bus travels (1 or 2), loop services only \
        have 1 direction.

    :example: 1
    """
    Category: str
    """Category of the SBS bus service:

    - "EXPRESS"
    - "FEEDER"
    - "INDUSTRIAL"
    - "TOWNLINK"
    - "TRUNK"
    - "2 TIER FLAT FEE"
    - "FLAT FEE $1.10" (or "$1.90", "$3.50", "$3.80")

    :example: "TRUNK"
    """
    OriginCode: str
    """Bus stop code for first bus stop.

    :example: "64009"
    """
    DestinationCode: str
    """Bus stop code for last bus stop (similar as first stop for loop \
        services).

    :example: "64009"
    """
    AM_Peak_Freq: str
    """Freq of dispatch for AM Peak 0630H - 0830H (range in minutes).

    :example: "5-08"
    """
    AM_Offpeak_Freq: str
    """Freq of dispatch for AM Off-Peak 0831H - 1659H (range in minutes).

    :example: "10-16"
    """
    PM_Peak_Freq: str
    """Freq of dispatch for PM Peak 1700H - 1900H (range in minutes).

    :example: "8-10"
    """
    PM_Offpeak_Freq: str
    """Freq of dispatch for PM Off-Peak after 1900H (range in minutes).

    :example: "12-15"
    """
    LoopDesc: str
    """Location at which the bus service loops, empty if not a loop service.

    :example: "Raffles Blvd"
    """

class BusStopsDict(TypedDict):
    """Type definition for bus_stops()"""

    BusStopCode: str
    """The unique 5-digit identifier for this physical bus stop.

    :example: "01219"
    """
    RoadName: str
    """The road on which this bus stop is located.

    :example: "Victoria St"
    """
    Description: str
    """Landmarks next to the bus stop (if any) to aid in identifying this bus \
        stop.

    :example: "Hotel Grand Pacific"
    """
    Latitude: float
    """Latitude location coordinates for this bus stop.

    :example: 1.29685
    """
    Longitude: float
    """Latitude location coordinates for this bus stop.

    :example: 103.853
    """

class FacilitiesMaintenanceDict(TypedDict):
    """Type definition for facilities_maintenance()"""

    Line: str
    """Code of train network line.

    :example: "NEL"
    """
    StationCode: str
    """Code of trains station.

    :example: "NE12"
    """
    StationName: str
    """Name of trains station.

    :example: "Serangoon"
    """
    LiftID: str | None
    """ID of the lift which is currently under maintenance. This value is \
        optional.

    :example: "B1L01"
    """
    LiftDesc: str
    """Detailed description of the lift which is currently under maintenance.

    :example: "Exit B Street level - Concourse"
    """

class StationCrowdDensityRealTimeDict(TypedDict):
    """Type definition for station_crowd_density_real_time()"""

    Station: str
    """Station code.

    :example: "EW13"
    """
    StartTime: datetime
    """The start of the time interval.

    :example: datetime(2021, 9, 15, 9, 40, 0)
    """
    EndTime: datetime
    """The end of the time interval.

    :example: datetime(2021, 9, 15, 9, 50, 0)
    """
    CrowdLevel: str
    """The crowdedness level indicates:

    - "l" - low
    - "h" - high
    - "m" - moderate
    - blank.

    :example: "l"
    """

class _StationCrowdDensityForecastStationIntervalDict(TypedDict):
    """Type definition for StationCrowdDensityForecastStationDict"""

    Start: datetime
    """The start of the time interval.

    :example: datetime(2021, 9, 15, 0, 0, 0)
    """
    CrowdLevel: str
    """The crowdedness level indicates:

    - "l" - low
    - "h" - high
    - "m" - moderate
    - blank.

    :example: "l"
    """
class _StationCrowdDensityForecastStationDict(TypedDict):
    """Type definition for StationCrowdDensityForecastDict"""

    Station: str
    """Station code.

    :example: "EW13"
    """
    Interval: list[_StationCrowdDensityForecastStationIntervalDict]
    """Array of station crowd density forecast per time interval."""
class StationCrowdDensityForecastDict(TypedDict):
    """Type definition for station_crowd_density_forecast()"""

    Date: datetime
    """Midnight of the forecasted date.

    :example: datetime(2021, 9, 15, 0, 0, 0)
    """
    Stations: list[_StationCrowdDensityForecastStationDict]
    """Array of station crowd density forecast."""

class TaxiAvailabilityDict(TypedDict):
    """Type definition for taxi_availability()"""

    Latitude: float
    """Latitude location coordinates.

    :example: 1.35667
    """
    Longitude: float
    """Longitude location coordinates.

    :example: 103.93314
    """

class TaxiStandsDict(TypedDict):
    """Type definition for taxi_stands()"""

    TaxiCode: str
    """Code representation of Taxi facility.

    :example: "A01"
    """
    Latitude: float
    """Latitude map coordinates for the taxi stand.

    :example: 1.303980684
    """
    Longitude: float
    """Longitude map coordinates for the taxi stand.

    :example: 103.9191828
    """
    Bfa: str
    """Indicate whether the Taxi stand is barrier free.

    :example: "Yes"
    """
    Ownership: str
    """Indicate the owner of the Taxi stand.

    - "LTA" - Land Transport Authority.
    - "CCS" - Clear Channel Singapore.
    - "Private" - Taxi facilities that are constructed and maintained by \
        private entities (e.g. developers/owners of shopping malls, commercial \
        buildings).

    :example: "LTA"
    """
    Type: str
    """Indicate the type of the Taxi stand.

    - "Stand" - allows Taxis to queue in the taxi bays and wait for passengers.
    - "Stop" - allow Taxis to perform immediate pick up and drop off of \
        passengers.

    :example: "Stand"
    """
    Name: str
    """Name of Taxi facility.

    :example: "Orchard Rd along driveway of Lucky Plaza"
    """

class _TrainServiceAlertMessageDict(TypedDict):
    """Type definition for TrainServiceAlertsDict"""
    Content: str
    """Travel advisory notification service for train commuters, published by \
        LTA. This notice is also broadcasted to commuters via the Find-My-Way \
        module in MyTransport mobile app.

    :example: "1710hrs: NEL - No train service between Harbourfront to Dhoby \
        Ghaut stations towards Punggol station due to a signalling fault. Free \
        bus rides are available at designated bus stops.".
    """
    CreatedDate: datetime
    """Date-time of when the message was created.

    :example: datetime(2017, 12, 1, 17, 54, 21)
    """

class _TrainServiceAlertAffectedSegmentDict(TypedDict):
    """Type definition for TrainServiceAlertsDict"""

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

    :example: "NEL"
    """
    Direction: str
    """Indicates direction of service unavailability on the affected line:
    - "Both".
    - towards station name.

    :example: "Punggol"
    """
    Stations: str
    """Indicates the list of affected stations on the affected line.

    :example: "NE1,NE3,NE4,NE5,NE6"
    """
    FreePublicBus: str | None
    """Indicates the list of affected stations where free boarding onto normal \
        public bus services are available.

    - station code.
    - "Free bus service island wide".

    :example: "NE1,NE3,NE4,NE5,NE6"
    """
    FreeMRTShuttle: str | None
    """Indicates the list of affected stations where free MRT shuttle \
        services are available.

    - station code.
    - "EW21|CC22,EW23,EW24|NS1,EW27;NS9,NS13,NS16,NS17|CC15;EW8|CC9,EW5,EW2;NS1|EW24,NS4|BP1*".

    :example: "NE1,NE3,NE4,NE5,NE6"
    """
    MRTShuttleDirection: str | None
    """Indicates the direction of free MRT shuttle services available:

    - "Both".
    - towards station name.

    :example: "Punggol"
    """

class TrainServiceAlertsDict(TypedDict):
    """Type definition for train_service_alerts()"""

    Status: int
    """Indicates if train service is unavailable:

    - 1 - for Normal Train Service.
    - 2 - for Disrupted Train Service.

    :example: 1
    """
    AffectedSegments: list[_TrainServiceAlertAffectedSegmentDict]
    """Array of train servicee affected segments."""
    Message: list[_TrainServiceAlertMessageDict]

__all__ = [
    '_NextBusDict',
    'BusArrivalDict',
    'BusRoutesDict',
    'BusServicesDict',
    'BusStopsDict',
    'FacilitiesMaintenanceDict',
    'PlannedBusRoutesDict',
    '_StationCrowdDensityForecastStationIntervalDict',
    '_StationCrowdDensityForecastStationDict',
    'StationCrowdDensityRealTimeDict',
    'StationCrowdDensityForecastDict',
    'TaxiAvailabilityDict',
    'TaxiStandsDict',
    'TrainServiceAlertsDict',
]
