# Copyright 2019-2025 Yuhui. All rights reserved.
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

from typing import Unpack

from typeguard import typechecked

from ..constants import (
    CACHE_ONE_MINUTE,
    CACHE_FIVE_MINUTES,
    CACHE_TEN_MINUTES,
    CACHE_ONE_HOUR,
    CACHE_ONE_DAY,
)
from ..landtransportsg import LandTransportSg
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
    PLANNED_BUS_ROUTES_API_ENDPOINT,
    STATION_CROWD_DENSITY_REAL_TIME_API_ENDPOINT,
    STATION_CROWD_DENSITY_FORECAST_API_ENDPOINT,
    TAXI_AVAILABILITY_API_ENDPOINT,
    TAXI_STANDS_API_ENDPOINT,
    TRAIN_SERVICE_ALERTS_API_ENDPOINT,

    BUS_ARRIVAL_ARGS_KEY_MAP,
    PASSENGER_VOLUME_ARGS_KEY_MAP,
    STATION_CROWD_DENSITY_ARGS_KEY_MAP,

    BUS_ARRIVAL_SANITISE_IGNORE_KEYS,
    BUS_ROUTES_SANITISE_IGNORE_KEYS,
    BUS_STOPS_SANITISE_IGNORE_KEYS,
    BUS_SERVICES_SANITISE_IGNORE_KEYS,

    TRAIN_LINES,
)
from .types_args import (
    BusArrivalArgsDict,
    PassengerVolumeArgsDict,
    StationCrowdDensityArgsDict,
)
from .types import (
    BusArrivalDict,
    BusServicesDict,
    BusRoutesDict,
    BusStopsDict,
    FacilitiesMaintenanceDict,
    PlannedBusRoutesDict,
    StationCrowdDensityRealTimeDict,
    StationCrowdDensityForecastDict,
    TaxiAvailabilityDict,
    TaxiStandsDict,
    TrainServiceAlertsDict,
)

class Client(LandTransportSg):
    """Interact with the public transport-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @typechecked
    def bus_arrival(
        self,
        **kwargs: Unpack[BusArrivalArgsDict],
    ) -> BusArrivalDict:
        """Get real-time Bus Arrival information of Bus Services at a queried \
        Bus Stop, including Est. Arrival Time, Est. Current Location, Est. \
        Current Load.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: BusArrivalArgsDict

        :raises ValueError: bus_stop_code is not exactly 5 characters long.
        :raises ValueError: bus_stop_code is not a number-like string.

        :return: Information about bus arrival at the specified bus stop.
        :rtype: BusArrivalDict
        """
        params = self.build_params(
            params_expected_type=BusArrivalArgsDict,
            original_params=kwargs,
            key_map=BUS_ARRIVAL_ARGS_KEY_MAP,
        )

        bus_stop_code = kwargs['bus_stop_code']

        try:
            _ = int(bus_stop_code)
        except Exception as e:
            raise ValueError(
                'Argument "bus_stop_code" is not a valid number.'
            ) from e

        if len(bus_stop_code) != 5:
            raise ValueError(
                'Argument "bus_stop_code" must be 5-digits long.'
            )

        bus_arrival: BusArrivalDict

        bus_arrival = self.send_request(
            BUS_ARRIVAL_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
            sanitise_ignore_keys=BUS_ARRIVAL_SANITISE_IGNORE_KEYS,
        )

        return bus_arrival

    @typechecked
    def bus_routes(self) -> list[BusRoutesDict]:
        """Get detailed route information for all services currently in \
        operation, including: all bus stops along each route, first/last bus \
        timings for each stop.

        :return: Information about bus routes currently in operation.
        :rtype: list[BusRoutesDict]
        """
        bus_routes: list[BusRoutesDict]

        bus_routes = self.send_request(
            BUS_ROUTES_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
            sanitise_ignore_keys=BUS_ROUTES_SANITISE_IGNORE_KEYS,
        )

        return bus_routes

    @typechecked
    def bus_services(self) -> list[BusServicesDict]:
        """Get detailed service information for all buses currently in \
        operation, including: first stop, last stop, peak / offpeak frequency \
        of dispatch.

        :return: Information about bus services currently in operation.
        :rtype: list[BusServicesDict]
        """
        bus_services: list[BusServicesDict]

        bus_services = self.send_request(
            BUS_SERVICES_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
            sanitise_ignore_keys=BUS_SERVICES_SANITISE_IGNORE_KEYS,
        )

        return bus_services

    @typechecked
    def bus_stops(self) -> list[BusStopsDict]:
        """Get detailed information for all bus stops currently being \
        serviced by buses, including: Bus Stop Code, location coordinate.

        :return: Location coordinaties of bus stops with active services.
        :rtype: list[BusStopsDict]
        """
        bus_stops: list[BusStopsDict]

        bus_stops = self.send_request(
            BUS_STOPS_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
            sanitise_ignore_keys=BUS_STOPS_SANITISE_IGNORE_KEYS,
        )

        return bus_stops

    @typechecked
    def facilities_maintenance(self) -> list[FacilitiesMaintenanceDict]:
        """Returns adhoc lift maintenance in MRT stations.

        :return: Station codes and namse with IDs of lifts being serviced.
        :rtype: list[FacilitiesMaintenanceDict]
        """
        facilities_maintenance: list[FacilitiesMaintenanceDict]

        facilities_maintenance = self.send_request(
            FACILITIES_MAINTENANCE_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
            sanitise_ignore_keys=BUS_STOPS_SANITISE_IGNORE_KEYS,
        )

        return facilities_maintenance

    @typechecked
    def passenger_volume_by_bus_stops(
        self,
        **kwargs: Unpack[PassengerVolumeArgsDict],
    ) -> Url:
        """Get tap in and tap out passenger volume by weekdays and weekends \
        for individual bus stop.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: PassengerVolumeArgsDict

        :return: Download link of file containing passenger volume data.
        :rtype: Url
        """
        params = self.build_params(
            params_expected_type=PassengerVolumeArgsDict,
            original_params=kwargs,
            key_map=PASSENGER_VOLUME_ARGS_KEY_MAP,
        )

        if 'dt' in kwargs:
            dt = kwargs['dt']
            if dt is not None and not date_is_within_last_three_months(dt):
                raise ValueError('Argument "dt" is not within the last 3 months.')

        passenger_volume_link: Url

        passenger_volume_link = self.send_download_request(
            PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_FIVE_MINUTES,
        )

        return passenger_volume_link

    @typechecked
    def passenger_volume_by_origin_destination_bus_stops(
        self,
        **kwargs: Unpack[PassengerVolumeArgsDict],
    ) -> Url:
        """Get number of trips by weekdays and weekends from origin to \
        destination bus stops.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: PassengerVolumeArgsDict

        :return: Download link of file containing passenger volume data.
        :rtype: Url
        """
        params = self.build_params(
            params_expected_type=PassengerVolumeArgsDict,
            original_params=kwargs,
            key_map=PASSENGER_VOLUME_ARGS_KEY_MAP,
        )

        if 'dt' in kwargs:
            dt = kwargs['dt']
            if dt is not None and not date_is_within_last_three_months(dt):
                raise ValueError('Argument "dt" is not within the last 3 months.')

        passenger_volume_link: Url

        passenger_volume_link = self.send_download_request(
            PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_DAY,
        )

        return passenger_volume_link

    @typechecked
    def passenger_volume_by_origin_destination_train_stations(
        self,
        **kwargs: Unpack[PassengerVolumeArgsDict],
    ) -> Url:
        """Get number of trips by weekdays and weekends from origin to \
        destination train stations.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: PassengerVolumeArgsDict

        :return: Download link of file containing passenger volume data.
        :rtype: Url
        """
        params = self.build_params(
            params_expected_type=PassengerVolumeArgsDict,
            original_params=kwargs,
            key_map=PASSENGER_VOLUME_ARGS_KEY_MAP,
        )

        if 'dt' in kwargs:
            dt = kwargs['dt']
            if dt is not None and not date_is_within_last_three_months(dt):
                raise ValueError('Argument "dt" is not within the last 3 months.')

        passenger_volume_link: Url

        passenger_volume_link = self.send_download_request(
            PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_DAY,
        )

        return passenger_volume_link

    @typechecked
    def passenger_volume_by_train_stations(
        self,
        **kwargs: Unpack[PassengerVolumeArgsDict],
    ) -> Url:
        """Get tap in and tap out passenger volume by weekdays and weekends \
        for individual train station.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: PassengerVolumeArgsDict

        :return: Download link of file containing passenger volume data.
        :rtype: Url
        """
        params = self.build_params(
            params_expected_type=PassengerVolumeArgsDict,
            original_params=kwargs,
            key_map=PASSENGER_VOLUME_ARGS_KEY_MAP,
        )

        if 'dt' in kwargs:
            dt = kwargs['dt']
            if dt is not None and not date_is_within_last_three_months(dt):
                raise ValueError('Argument "dt" is not within the last 3 months.')

        passenger_volume_link: Url

        passenger_volume_link = self.send_download_request(
            PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_DAY,
        )

        return passenger_volume_link

    @typechecked
    def planned_bus_routes(self) -> list[PlannedBusRoutesDict]:
        """Get planned new/updated bus routes information.

        Important note: Data to be released only ON/AFTER the Effective Date.

        :return: Information about planned bus routes.
        :rtype: list[PlannedBusRoutesDict]
        """
        planned_bus_routes: list[PlannedBusRoutesDict]

        planned_bus_routes = self.send_request(
            PLANNED_BUS_ROUTES_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
        )

        return planned_bus_routes

    @typechecked
    def train_lines(self) -> tuple[str, ...]:
        """Return the tuple of valid train lines.

        :return: Tuple of valid train lines.
        :rtype: tuple[str, ...]
        """
        train_lines: tuple[str, ...]

        train_lines = TRAIN_LINES

        return train_lines

    @typechecked
    def station_crowd_density_real_time(
        self,
        **kwargs: Unpack[StationCrowdDensityArgsDict],
    ) -> list[StationCrowdDensityRealTimeDict]:
        """Get real-time MRT/LRT station crowdedness level of a particular \
        train network line. Refer to the train_lines() method for the list of \
        valid train network lines.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: StationCrowdDensityArgsDict

        :raises ValueError: train_line is not specified.
        :raises ValueError: train_line is not a valid train network line.

        :return: Station crowdedness level of the specified train network \
            line.
        :rtype: list[StationCrowdDensityRealTimeDict]
        """
        params = self.build_params(
            params_expected_type=StationCrowdDensityArgsDict,
            original_params=kwargs,
            key_map=STATION_CROWD_DENSITY_ARGS_KEY_MAP,
        )

        train_line = kwargs['train_line']

        if train_line not in TRAIN_LINES:
            raise ValueError(
                'Invalid argument "train_line". Use train_lines() to get a list of valid train line codes'
            )

        station_crowd_density_real_time: list[
            StationCrowdDensityRealTimeDict
        ]

        station_crowd_density_real_time = self.send_request(
            STATION_CROWD_DENSITY_REAL_TIME_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TEN_MINUTES,
        )

        return station_crowd_density_real_time

    @typechecked
    def station_crowd_density_forecast(
        self,
        **kwargs: Unpack[StationCrowdDensityArgsDict],
    ) -> list[StationCrowdDensityForecastDict]:
        """Get forecasted MRT/LRT statiion crowdedness level of a particular \
        train network line at 30 minutes interval. Refer to the train_lines() \
        method for the list of valid train network lines.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: StationCrowdDensityArgsDict

        :raises ValueError: train_line is not specified.
        :raises ValueError: train_line is not a valid train network line.

        :return: Forecasted platform crowdedness level of the specified \
            train network line.
        :rtype: list[StationCrowdDensityForecastDict]
        """
        params = self.build_params(
            params_expected_type=StationCrowdDensityArgsDict,
            original_params=kwargs,
            key_map=STATION_CROWD_DENSITY_ARGS_KEY_MAP,
        )

        train_line = kwargs['train_line']

        if train_line not in TRAIN_LINES:
            raise ValueError(
                'Invalid argument "train_line". Use train_lines() to get a list of valid train line codes'
            )

        station_crowd_density_forecast: list[
            StationCrowdDensityForecastDict
        ]

        station_crowd_density_forecast = self.send_request(
            STATION_CROWD_DENSITY_FORECAST_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_DAY,
        )

        return station_crowd_density_forecast

    @typechecked
    def taxi_availability(self) -> list[TaxiAvailabilityDict]:
        """Get location coordinates of all Taxis that are currently available \
        for hire. Does not include "Hired" or "Busy" Taxis.

        :return: Location coordinaties of available taxis.
        :rtype: list[TaxiAvailabilityDict]
        """
        taxi_availabilities: list[TaxiAvailabilityDict]

        taxi_availabilities = self.send_request(
            TAXI_AVAILABILITY_API_ENDPOINT,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return taxi_availabilities

    def taxi_stands(self) -> list[TaxiStandsDict]:
        """Get detailed information of Taxi stands, such as location and \
        whether is it barrier free.

        :return: Detailed information of taxi stands.
        :rtype: list[TaxiStandsDict]
        """
        taxi_stands: list[TaxiStandsDict]

        taxi_stands = self.send_request(
            TAXI_STANDS_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
        )

        return taxi_stands

    def train_service_alerts(self) -> list[TrainServiceAlertsDict]:
        """Get detailed information on train service unavailability during \
        scheduled operating hours, such as affected line and stations etc.

        :return: Information about train service unavailability.
        :rtype: list[TrainServiceAlertsDict]
        """
        train_service_alerts: list[TrainServiceAlertsDict]

        train_service_alerts = self.send_request(
            TRAIN_SERVICE_ALERTS_API_ENDPOINT,
            cache_duration=CACHE_ONE_HOUR,
        )

        return train_service_alerts

__all__ = [
    'Client',
]
