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

from .constants import *
from ..client import __Client
from ..exceptions import APIError

class Client(__Client):
    """Interact with the geospatial-related endpoints.

    References:
        https://www.mytransport.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    def __init(self, account_key):
        super(Client, self).__init__(account_key)

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    def geospatial_whole_island(self, geospatial_layer_id):
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
                'Missing geospatial_layer_id. Allowed IDs: {}'.format(
                    ', '.join(GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS),
                ),
            )

        if not isinstance(geospatial_layer_id, str):
            raise ValueError('geospatial_layer_id is not a string.')

        if geospatial_layer_id not in GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS:
            raise ValueError(
                'geospatial_layer_id is invalid. Allowed IDs: {}'.format(
                    ', '.join(GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS),
                ),
            )

        geospatial_whole_island_link = self.send_download_request(
            GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT,
            ID=geospatial_layer_id,
        )

        return geospatial_whole_island_link
