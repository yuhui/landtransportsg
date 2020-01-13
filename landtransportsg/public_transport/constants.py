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

"""Constants for all Public Transport-related APIs."""

from ..constants import (
    BASE_API_ENDPOINT,
    CACHE_MAXSIZE,
    CACHE_ONE_MINUTE,
    CACHE_ONE_HOUR,
    CACHE_ONE_DAY,
    CACHE_ONE_MONTH,
)

BUS_ARRIVAL_API_ENDPOINT = '{}/BusArrivalv2'.format(BASE_API_ENDPOINT)
BUS_SERVICES_API_ENDPOINT = '{}/BusServices'.format(BASE_API_ENDPOINT)
BUS_ROUTES_API_ENDPOINT = '{}/BusRoutes'.format(BASE_API_ENDPOINT)
BUS_STOPS_API_ENDPOINT = '{}/BusStops'.format(BASE_API_ENDPOINT)
PASSENGER_VOLUME_BY_BUS_STOPS_API_ENDPOINT = '{}/PV/Bus'.format(
    BASE_API_ENDPOINT,
)
PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_BUS_STOPS_API_ENDPOINT = \
    '{}/PV/ODBus'.format(BASE_API_ENDPOINT)
PASSENGER_VOLUME_BY_ORIGIN_DESTINATION_TRAIN_STATIONS_API_ENDPOINT = \
    '{}/PV/ODTrain'.format(BASE_API_ENDPOINT)
PASSENGER_VOLUME_BY_TRAIN_STATIONS_API_ENDPOINT = '{}/PV/Train'.format(
    BASE_API_ENDPOINT,
)
TAXI_AVAILABILITY_API_ENDPOINT = '{}/Taxi-Availability'.format(
    BASE_API_ENDPOINT,
)
TAXI_STANDS_API_ENDPOINT = '{}/TaxiStands'.format(
    BASE_API_ENDPOINT,
)
TRAIN_SERVICE_ALERTS_API_ENDPOINT = '{}/TrainServiceAlerts'.format(
    BASE_API_ENDPOINT,
)
