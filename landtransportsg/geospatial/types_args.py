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

"""LandTransportSg DataMall custom types for Geospatial client methods' arguments."""

from typing import TypedDict

class GeospatiaWholeIslandArgsDict(TypedDict):
    """Type definition for geospatial_whole_island() input arguments"""

    geospatial_layer_id: str
    """Name of Geospatial Layer. Use ``geospatial_layer_ids()`` for the list \
        of Geospatial layers.

    :example: "ArrowMarking"
    """

__all__ = [
    'GeospatiaWholeIslandArgsDict',
]
