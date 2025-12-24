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

"""Client for interacting with the Active Mobility API endpoints."""

from typeguard import typechecked

from ..client import Lta
from ..constants import CACHE_ONE_DAY

from .constants import BICYCLE_PARKING_API_ENDPOINT
from .types import BicycleParkingDict

class Client(Lta):
    """Interact with the active mobility-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @typechecked
    def bicycle_parking(
        self,
        latitude: float,
        longitude: float,
        distance: float=0.5,
    ) -> list[BicycleParkingDict | dict]:
        """Get bicycle parking locations within a radius.

        :param latitude: Latitude map coordinates of a location.
        :type latitude: float

        :param longitude: Longitude map coordinates of a location.
        :type longitude: float

        :param distance: Radius in kilometres from the latitude-longitude \
            location to retrieve bicycle parking locations. Defaults to 0.5.
        :type distance: float

        :raises ValueError: distance is a negative float.

        :return: Available bicycle parking locations at the specified \
            location.
        :rtype: list[BicycleParkingDict]
        """
        if isinstance(distance, float) and distance < 0:
            raise ValueError('Argument "distance" cannot be less than zero.')

        bicycle_parking_locations = self.send_request(
            BICYCLE_PARKING_API_ENDPOINT,
            Lat=latitude,
            Long=longitude,
            Dist=distance,
            cache_duration=CACHE_ONE_DAY,
        )

        return bicycle_parking_locations

__all__ = [
    'Client',
]
