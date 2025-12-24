# Copyright 2025 Yuhui. All rights reserved.
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

"""LTA DataMall custom types for Public Transport client methods' arguments."""

from datetime import date
from typing import NotRequired, TypedDict

class BusArrivalArgsDict(TypedDict):
    """Type definition for bus_arrival() input arguments"""

    bus_stop_code: str
    """Bus stop reference code.

    :example: "83139"
    """
    service_number: NotRequired[str | None]
    """Bus service number.

    :example: "15"
    :default: None
    """

class PassengerVolumeArgsDict(TypedDict):
    """Type definition for platform_crowd_density_real_time() and \
        platform_crowd_density_forecast() input arguments"""

    dt: NotRequired[date | None]
    """Date of a specific month to get passenger volume. Only the year and \
        month are used since those are what the endpoint accepts. Must be \
        within the last 3 months of the current month.

    :example: date(2019, 7, 2)
    :default: None
    """

class StationCrowdDensityArgsDict(TypedDict):
    """Type definition for station_crowd_density_real_time() and \
        station_crowd_density_forecast() input arguments"""

    train_line: str
    """Code of train network line. Use ``train_lines()`` for the list train lines.

    :example: "EWL"
    """

__all__ = [
    'BusArrivalArgsDict',
    'PassengerVolumeArgsDict',
    'StationCrowdDensityArgsDict',
]
