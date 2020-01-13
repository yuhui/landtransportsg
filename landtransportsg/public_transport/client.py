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

from cachetools import cached, TTLCache

import landtransportsg.timezone as timezone
from .constants import *
from ..client import __Client
from ..exceptions import APIError

class Client(__Client):
    """Interact with the public transport-related endpoints.

    References:
        https://www.mytransport.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    def __init(self, account_key):
        super(Client, self).__init__(account_key)

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def bus_arrival(self, bus_stop_code, service_number=None):
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
        if not isinstance(bus_stop_code, str):
            raise ValueError('bus_stop_code is not a string.')
        if len(bus_stop_code) != 5:
            raise ValueError('bus_stop_code is not a 5-character string.')
        try:
            _ = int(bus_stop_code)
        except:
            raise ValueError('bus_stop_code is not a valid number.')

        if service_number is not None and not isinstance(service_number, str):
            raise ValueError('service_number is not a string.')

        bus_arrival = self.send_request(
            BUS_ARRIVAL_API_ENDPOINT,
            BusStopCode=bus_stop_code,
            ServiceNo=service_number,
        )

        return bus_arrival

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def bus_services(self):
        """Get detailed service information for all buses currently in
        operation, including: first stop, last stop, peak / offpeak frequency
        of dispatch.

        Returns:
            (list) Information about bus services currently in operation.
        """
        bus_services = self.send_request(BUS_SERVICES_API_ENDPOINT)

        return bus_services

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def bus_routes(self):
        """Get detailed route information for all services currently in
        operation, including: all bus stops along each route, first/last bus
        timings for each stop.

        Returns:
            (list) Information about bus routes currently in operation.
        """
        bus_routes = self.send_request(BUS_ROUTES_API_ENDPOINT)

        return bus_routes

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def bus_stops(self):
        """Get detailed information for all bus stops currently being serviced
        by buses, including: Bus Stop Code, location coordinate.

        Returns:
            (list) Location coordinaties of bus stops with active services.
        """
        bus_stops = self.send_request(BUS_STOPS_API_ENDPOINT)

        return bus_stops

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    def passenger_volume_by_bus_stops(self, dt=None):
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
        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    def passenger_volume_by_origin_destination_bus_stops(self, dt=None):
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
        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    def passenger_volume_by_origin_destination_train_stations(self, dt=None):
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
        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    def passenger_volume_by_train_stations(self, dt=None):
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
        passenger_volume_link = self.__get_passenger_volume_link(
            PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT,
            dt,
        )

        return passenger_volume_link

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def taxi_availability(self):
        """Get location coordinates of all Taxis that are currently available
        for hire. Does not include "Hired" or "Busy" Taxis.

        Returns:
            (list) Location coordinaties of available taxis.
        """
        taxi_availabilities = self.send_request(
            TAXI_AVAILABILITY_API_ENDPOINT,
        )

        return taxi_availabilities

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MONTH))
    def taxi_stands(self):
        """Get detailed information of Taxi stands, such as location and whether
        is it barrier free.

        Returns:
            (list) Detailed information of taxi stands .
        """
        taxi_stands = self.send_request(
            TAXI_STANDS_API_ENDPOINT,
        )

        return taxi_stands

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_HOUR))
    def train_service_alerts(self):
        """Get detailed information on train service unavailability during
        scheduled operating hours, such as affected line and stations etc.

        Returns:
            (list) Information about train service unavailability.
        """
        train_service_alerts = self.send_request(
            TRAIN_SERVICE_ALERTS_API_ENDPOINT,
        )

        return train_service_alerts

    # private

    def __get_passenger_volume_link(self, endpoint, dt=None):
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
        if dt is not None and \
            not timezone.date_is_within_last_three_months(dt):
            raise ValueError('dt is not within the last 3 months.')

        self.validate_kwargs(Date=dt)

        passenger_volume = self.send_request(endpoint, Date=dt)

        if len(passenger_volume) is 0:
            raise APIError("Download link not returned.")

        passenger_volume_link = passenger_volume[0].get('Link')
        if passenger_volume_link is None:
            raise APIError("Download link not returned.")

        return passenger_volume_link
