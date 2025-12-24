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

"""LandTransportSg DataMall custom types for Active Mobility client methods' arguments."""

from typing import NotRequired, TypedDict

class BicycleParkingArgsDict(TypedDict):
    """Type definition for bicycle_parking() input arguments"""

    latitude: float
    """Latitude map coordinates of location.

    :example: 1.364897
    """
    longitude: float
    """Longitude map coordinates of location.

    :example: 103.766094
    """
    distance: NotRequired[float | None]
    """Radius in kilometre.

    :example: 0.5
    :default: 0.5
    """

__all__ = [
    'BicycleParkingArgsDict',
]
