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

"""Client for interacting with the Public Transport API endpoints."""

import re
from datetime import date
from typing import Optional

from cachetools import cached, TTLCache
from typeguard import typechecked

from ..client import Lta
from ..constants import (
    CACHE_MAXSIZE,
    CACHE_ONE_MINUTE,
    CACHE_FIVE_MINUTES,
    CACHE_TEN_MINUTES,
    CACHE_ONE_HOUR,
    CACHE_ONE_DAY,
    CACHE_ONE_MONTH,
)
from ..timezone import date_is_within_last_three_months
from ..types import Url

from .constants import (
    BUS_ARRIVAL_API_ENDPOINT,
    BUS_SERVICES_API_ENDPOINT,
    BUS_ROUTES_API_ENDPOINT,
    BUS_STOPS_API_ENDPOINT,
    FACILITIES_MAINTENANCE_API_ENDPOINT,
    PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT,
    PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT,
    PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT,
    PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT,
    PLATFORM_CROWD_DENSITY_REAL_TIME_API_ENDPOINT,
    PLATFORM_CROWD_DENSITY_FORECASE_API_ENDPOINT,
    TAXI_AVAILABILITY_API_ENDPOINT,
    TAXI_STANDS_API_ENDPOINT,
    TRAIN_SERVICE_ALERTS_API_ENDPOINT,

    STATION_CODES_REGEX_PATTERN,
    TRAIN_LINES,
)
from .types import (
    BusArrivalDict,
    BusServicesDict,
    BusRoutesDict,
    BusStopsDict,
    PlatformCrowdDensityRealTimeDict,
    PlatformCrowdDensityForecastDict,
    TaxiAvailabilityDict,
    TaxiStandsDict,
    TrainServiceAlertsDict,
)

class Client(Lta):
    """Interact with the public transport-related endpoints.

    References:
        https://www.mytransport.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    @typechecked
    def bus_arrival(
        self,
        bus_stop_code: str,
        service_number: Optional[str]=None,
    ) -> BusArrivalDict | dict:
        """Get real-time Bus Arrival information of Bus Services at a queried
        Bus Stop, including Est. Arrival Time, Est. Current Location, Est.
        Current Load.

        Arguments:
            bus_stop_code (str):
                5-digit bus stop reference code.
            service_number (str):
                (optional) Bus service number.
                If omitted, then all bus services at the bus stop code are
                returned.

        Returns:
            (list) Information about bus arrival at the specified bus stop.

        Raises:
            ValueError
                Raised if bus_stop_code or service_number are not strings.
            ValueError
                Raised if bus_stop_code is not exactly 5 characters long.
            ValueError
                Raised if bus_stop_code is not a number-like string.
        """
        if len(bus_stop_code) != 5:
            raise ValueError('bus_stop_code is not a 5-character string.')
        try:
            _ = int(bus_stop_code)
        except:
            raise ValueError('bus_stop_code is not a valid number.')

        bus_arrival: BusArrivalDict | dict

        bus_arrival = self.send_request(
            BUS_ARRIVAL_API_ENDPOINT,
            BusStopCode=bus_stop_code,
            ServiceNo=service_number,
        )

        return bus_arrival

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    @typechecked
    def bus_services(self) -> list[BusServicesDict | dict]:
        """Get detailed service information for all buses currently in
        operation, including: first stop, last stop, peak / offpeak frequency
        of dispatch.

        Returns:
            (list) Information about bus services currently in operation.
        """
        bus_services: list[BusServicesDict | dict]

        bus_services = self.send_request(BUS_SERVICES_API_ENDPOINT)

        return bus_services

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    @typechecked
    def bus_routes(self) -> list[BusRoutesDict | dict]:
        """Get detailed route information for all services currently in
        operation, including: all bus stops along each route, first/last bus
        timings for each stop.

        Returns:
            (list) Information about bus routes currently in operation.
        """
        bus_routes: list[BusRoutesDict | dict]

        bus_routes = self.send_request(BUS_ROUTES_API_ENDPOINT)

        return bus_routes

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    @typechecked
    def bus_stops(self) -> list[BusStopsDict | dict]:
        """Get detailed information for all bus stops currently being serviced
        by buses, including: Bus Stop Code, location coordinate.

        Returns:
            (list) Location coordinaties of bus stops with active services.
        """
        bus_stops: list[BusStopsDict | dict]

        bus_stops = self.send_request(BUS_STOPS_API_ENDPOINT)

        return bus_stops

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    @typechecked
    def facilities_maintenance(self, station_code: str) -> Url:
        """Get the pre-signed links to JSON file containing facilities
        maintenance schedules of the particular station.

        Arguments:
            station_code (str):
                Station Code of train station.
                Refer to the STATION_CODES_REGEX_PATTERN constant for the
                expected regex pattern that this code has to match.

        Returns:
            (str) Link for downloading the requested JSON file.

        Raises:
            ValueError
                Raised if station_code is not specified.
            ValueError
                Raised if station_code is not a string.
            ValueError:
                Raised if station_code does not match the expected regex
                pattern.
        """
        if station_code is None:
            raise ValueError('Missing argument "station_code".')

        if not re.search(STATION_CODES_REGEX_PATTERN, station_code):
            raise ValueError('Argument "station_code" is invalid.')

        facilities_maintenance_link: Url

        facilities_maintenance_link = self.send_download_request(
            FACILITIES_MAINTENANCE_API_ENDPOINT,
            StationCode=station_code,
        )

        return facilities_maintenance_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    @typechecked
    def passenger_volume_by_bus_stops(
        self,
        dt: Optional[date]=None
    ) -> Url:
        """Get tap in and tap out passenger volume by weekdays and weekends
        for individual bus stop.

        Arguments:
            dt (date):
                (optional) Date of a specific month to get passenger volume.
                This must be a valid date object, e.g. `date(2019, 7, 2)`.
                But only the year and month will be used since that is what
                the endpoint accepts.
                Must be within the last 3 months of the current month.

        Returns:
            (str) Download link of file containing passenger volume data.
        """
        passenger_volume_link: Url

        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    @typechecked
    def passenger_volume_by_origin_destination_bus_stops(
        self,
        dt: Optional[date]=None,
    ) -> Url:
        """Get number of trips by weekdays and weekends from origin to
        destination bus stops.

        Arguments:
            dt (date):
                (optional) Date of a specific month to get passenger volume.
                This must be a valid date object, e.g. `date(2019, 7, 2)`.
                But only the year and month will be used since that is what
                the endpoint accepts.
                Must be within the last 3 months of the current month.

        Returns:
            (str) Download link of file containing passenger volume data.
        """
        passenger_volume_link: Url

        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    @typechecked
    def passenger_volume_by_origin_destination_train_stations(
        self,
        dt: Optional[date]=None,
    ) -> Url:
        """Get number of trips by weekdays and weekends from origin to
        destination train stations.

        Arguments:
            dt (date):
                (optional) Date of a specific month to get passenger volume.
                This must be a valid date object, e.g. `date(2019, 7, 2)`.
                But only the year and month will be used since that is what
                the endpoint accepts.
                Must be within the last 3 months of the current month.
                Default: None, i.e. today.

        Returns:
            (str) Download link of file containing passenger volume data.
        """
        passenger_volume_link: Url

        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    @typechecked
    def passenger_volume_by_train_stations(
        self,
        dt: Optional[date]=None,
    ) -> Url:
        """Get tap in and tap out passenger volume by weekdays and weekends
        for individual train station.

        Arguments:
            dt (date):
                (optional) Date of a specific month to get passenger volume.
                This must be a valid date object, e.g. `date(2019, 7, 2)`.
                But only the year and month will be used since that is what
                the endpoint accepts.
                Must be within the last 3 months of the current month.

        Returns:
            (str) Download link of file containing passenger volume data.
        """
        passenger_volume_link: Url

        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    @typechecked
    def taxi_availability(self) -> list[TaxiAvailabilityDict | dict]:
        """Get location coordinates of all Taxis that are currently available
        for hire. Does not include "Hired" or "Busy" Taxis.

        Returns:
            (list) Location coordinaties of available taxis.
        """
        taxi_availabilities: list[TaxiAvailabilityDict | dict]

        taxi_availabilities = self.send_request(
            TAXI_AVAILABILITY_API_ENDPOINT,
        )

        return taxi_availabilities

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    def taxi_stands(self) -> list[TaxiStandsDict | dict]:
        """Get detailed information of Taxi stands, such as location and whether
        is it barrier free.

        Returns:
            (list) Detailed information of taxi stands .
        """
        taxi_stands: list[TaxiStandsDict | dict]

        taxi_stands = self.send_request(
            TAXI_STANDS_API_ENDPOINT,
        )

        return taxi_stands

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_HOUR))
    def train_service_alerts(self) -> list[TrainServiceAlertsDict]:
        """Get detailed information on train service unavailability during
        scheduled operating hours, such as affected line and stations etc.

        Returns:
            (list) Information about train service unavailability.
        """
        train_service_alerts: list[TrainServiceAlertsDict]

        train_service_alerts = self.send_request(
            TRAIN_SERVICE_ALERTS_API_ENDPOINT,
        )

        return train_service_alerts

    # private

    def __get_passenger_volume_link(
        self,
        endpoint,
        dt: Optional[date]=None
    ) -> Url:
        """Get download link of the passenger volume data file for the
        specific endpoint.

        Arguments:
            endpoint(str):
                API endpoint URL to call.
            dt (date):
                (optional) Date of a specific month to get passenger volume.
                This must be a valid date object, e.g. `date(2019, 7, 2)`.
                But only the year and month will be used since that is what
                the endpoint accepts.
                Must be within the last 3 months of the current month.

        Returns:
            (str) Download link of file containing passenger volume data.

        Raises:
            ValueError:
                Raised if the specified date is more than 3 months ago.
            APIError:
                Raised if no download link is returned.
        """
        if dt is not None and not date_is_within_last_three_months(dt):
            raise ValueError('Argument "dt" is not within the last 3 months.')

        passenger_volume_link: Url

        self.validate_kwargs(Date=dt)

        passenger_volume_link = self.send_download_request(endpoint, Date=dt)

        return passenger_volume_link

__all__ = [
    'Client',
]
