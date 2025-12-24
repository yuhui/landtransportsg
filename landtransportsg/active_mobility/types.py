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

"""Active Mobility custom types."""

from typing import TypedDict

class BicycleParkingDict(TypedDict):
    """Type definition for bicycle_parking()"""

    Description: str
    """Brief description of bicycle parking location.

    :example: "Bus Stop 43267"
    """
    Latitude: float
    """Latitude map coordinates of bicycle parking location.

    :example: 1.3927176306916775
    """
    Longitude: float
    """Longitude map coordinates of bicycle parking location.

    :example: 103.82618266340947
    """
    RackType: str
    """Type of bicycle parking facility.

    :example: "Racks or Yellow Box"
    """
    RackCount: int
    """Total number of bicycle parking lots.

    :example: 10
    """
    ShelterIndicator: str
    """Indicate whether the bicycle parking lots are sheltered.

    :example: "Y"
    """

__all__ = [
    'BicycleParkingDict',
]
