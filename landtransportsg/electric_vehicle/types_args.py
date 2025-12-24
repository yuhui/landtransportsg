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

"""LandTransportSg DataMall custom types for Electric Vehicle client methods' arguments."""

from typing import TypedDict

class EVChargingPointsArgsDict(TypedDict):
    """Type definition for ev_charging_points() input arguments"""

    postal_code: str
    """Postal code of the location.

    :example: "123456"
    """

__all__ = [
    'EVChargingPointsArgsDict',
]
