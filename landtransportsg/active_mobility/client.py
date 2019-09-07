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

"""Client for interacting with the Active Mobility API endpoints."""

from cachetools import cached, TTLCache
from datetime import date, datetime

from .constants import *
from ..client import __Client

class Client(__Client):
    """Interact with the active mobility-related endpoints.

    References:
        https://www.mytransport.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    def __init(self, account_key):
        super(Client, self).__init__(account_key)

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def bicycle_parking(self, latitude, longitude, distance=0.5):
        """Get bicycle parking locations within a radius.

        Arguments:
            latitude (float):
                Latitude map coordinates of a location.
            longitude (float):
                Longitude map coordinates of a location.
            distance (float):
                (optional) Radius in kilometres from the latitude-longitude
                location to retrieve bicycle parking locations.
                Default: 0.5.

        Returns:
            (list) Available bicycle parking locations at the specified
            location.

        Raises:
            ValueError:
                If latitude, longitude or distance are not floats.
        """
        if not isinstance(latitude, float):
            raise ValueError("latitude is not a float.")
        if not isinstance(longitude, float):
            raise ValueError("longitude is not a float.")
        if not isinstance(distance, float):
            raise ValueError("distance is not a float.")

        bicycle_parking_locations = self.send_request(
            BICYCLE_PARKING_API_ENDPOINT,
            Lat=latitude,
            Long=longitude,
            Dist=distance,
        )

        return bicycle_parking_locations
