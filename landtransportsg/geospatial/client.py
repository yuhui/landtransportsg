# Copyright 2020 Yuhui
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

"""Client for interacting with the Geospatial API endpoints."""

from cachetools import cached, TTLCache
from typeguard import typechecked

from ..client import Lta
from ..constants import CACHE_MAXSIZE, CACHE_FIVE_MINUTES
from ..types import Url

from .constants import (
    GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT,

    GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS,
)

class Client(Lta):
    """Interact with the geospatial-related endpoints.

    References:
        https://www.mytransport.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    def __init(self, account_key):
        super(Client, self).__init__(account_key)

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    @typechecked
    def geospatial_whole_island(self, geospatial_layer_id: str) -> Url:
        """Get the SHP files of the requested geospatial layer.

        Arguments:
            geospatial_layer_id (str):
                Name of geospatial layer.
                Refer to the GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS constant for the
                list of valid names.

        Returns:
            (str) Link for downloading the requested SHP file.

        Raises:
            ValueError
                Raised if geospatial_layer_id is not specified.
            ValueError
                Raised if geospatial_layer_id is not a string.
            ValueError:
                Raised if geospatial_layer_id is not a valid ID.
        """
        if geospatial_layer_id is None:
            raise ValueError(
                f'Missing argument "geospatial_layer_id". Allowed IDs: {
                    ', '.join(GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS),
                }',
            )

        if geospatial_layer_id not in GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS:
            raise ValueError(
                f'Invalid argument "geospatial_layer_id". Allowed IDs: {
                    ', '.join(GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS),
                }',
            )

        geospatial_whole_island_link: Url

        geospatial_whole_island_link = self.send_download_request(
            GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT,
            ID=geospatial_layer_id,
        )

        return geospatial_whole_island_link

__all__ = [
    'Client',
]
