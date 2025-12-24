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

# pylint: disable=line-too-long

"""Constants for all Public Transport-related APIs."""

from ..constants import BASE_API_ENDPOINT

BUS_ARRIVAL_API_ENDPOINT = f'{BASE_API_ENDPOINT}/v3/BusArrival'
BUS_SERVICES_API_ENDPOINT = f'{BASE_API_ENDPOINT}/BusServices'
BUS_ROUTES_API_ENDPOINT = f'{BASE_API_ENDPOINT}/BusRoutes'
BUS_STOPS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/BusStops'
FACILITIES_MAINTENANCE_API_ENDPOINT = f'{BASE_API_ENDPOINT}/FacilitiesMaintenance'
PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/PV/Bus'
PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/PV/ODBus'
PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/PV/ODTrain'
PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/PV/Train'
STATION_CROWD_DENSITY_REAL_TIME_API_ENDPOINT = f'{BASE_API_ENDPOINT}/PCDRealTime'
STATION_CROWD_DENSITY_FORECAST_API_ENDPOINT = f'{BASE_API_ENDPOINT}/PCDForecast'
TAXI_AVAILABILITY_API_ENDPOINT = f'{BASE_API_ENDPOINT}/Taxi-Availability'
TAXI_STANDS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/TaxiStands'
TRAIN_SERVICE_ALERTS_API_ENDPOINT = f'{BASE_API_ENDPOINT}/TrainServiceAlerts'

"""
All MRT station codes start with 2 uppercase letters, then 1-2 digits. \
E.g. NS1, DT35.
"""
STATION_CODES_REGEX_PATTERN = r"^[A-Z]{2}[0-9]{1,2}$"
BUS_ARRIVAL_ARGS_KEY_MAP = {
    'bus_stop_code': 'BusStopCode',
    'service_number': 'ServiceNo',
}
PASSENGER_VOLUME_ARGS_KEY_MAP = {
    'dt': 'Date',
}
STATION_CROWD_DENSITY_ARGS_KEY_MAP = {
    'train_line': 'TrainLine',
}


TRAIN_LINES = (
    'BPL',
    'CCL',
    'CEL',
    'CGL',
    'DTL',
    'EWL',
    'NEL',
    'NSL',
    'PLRT',
    'SLRT',
    'TEL',
)

__all__ = [
    'BUS_ARRIVAL_API_ENDPOINT',
    'BUS_SERVICES_API_ENDPOINT',
    'BUS_ROUTES_API_ENDPOINT',
    'BUS_STOPS_API_ENDPOINT',
    'FACILITIES_MAINTENANCE_API_ENDPOINT',
    'PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT',
    'PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT',
    'PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT',
    'PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT',
    'STATION_CROWD_DENSITY_REAL_TIME_API_ENDPOINT',
    'STATION_CROWD_DENSITY_FORECAST_API_ENDPOINT',
    'TAXI_AVAILABILITY_API_ENDPOINT',
    'TAXI_STANDS_API_ENDPOINT',
    'TRAIN_SERVICE_ALERTS_API_ENDPOINT',

    'STATION_CODES_REGEX_PATTERN',
    'BUS_ARRIVAL_ARGS_KEY_MAP',
    'PASSENGER_VOLUME_ARGS_KEY_MAP',
    'STATION_CROWD_DENSITY_ARGS_KEY_MAP',

    'TRAIN_LINES',
]
