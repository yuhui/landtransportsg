# Copyright 2020-2025 Yuhui. All rights reserved.
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

from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_FIVE_MINUTES
from ..landtransportsg import LandTransportSg
from ..types import Url

from .constants import (
    GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT,
    GEOSPATIAL_WHOLE_ISLAND_ARGS_KEY_MAP,

    GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS,
)
from .types_args import GeospatiaWholeIslandArgsDict

class Client(LandTransportSg):
    """Interact with the geospatial-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @typechecked
    def geospatial_layer_ids(self) -> tuple[str, ...]:
        """Return the tuple of valid geospatial layer IDs.

        :return: Tuple of valid geospatial layer IDs.
        :rtype: tuple[str, ...]
        """
        geospatial_whole_island_ids: tuple[str, ...]

        geospatial_whole_island_ids = GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS

        return geospatial_whole_island_ids

    @typechecked
    def geospatial_whole_island(
        self,
        **kwargs: Unpack[GeospatiaWholeIslandArgsDict],
    ) -> Url:
        """Get the SHP files of the requested geospatial layer.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: GeospatiaWholeIslandArgsDict

        :raises ValueError: geospatial_layer_id is not a valid ID.

        :return: Link for downloading the requested SHP file.
        :rtype: Url
        """
        geospatial_whole_island_link: Url

        params = self.build_params(
            params_expected_type=GeospatiaWholeIslandArgsDict,
            original_params=kwargs,
            key_map=GEOSPATIAL_WHOLE_ISLAND_ARGS_KEY_MAP,
        )

        if params['ID'] not in GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS:
            allowed_ids = ', '.join(GEOSPATIAL_WHOLE_ISLAND_LAYER_IDS)
            raise ValueError(
                f'Invalid argument "geospatial_layer_id". Allowed IDs: {allowed_ids}',
            )

        geospatial_whole_island_link = self.send_download_request(
            GEOSPATIAL_WHOLE_ISLAND_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_FIVE_MINUTES,
        )

        return geospatial_whole_island_link

__all__ = [
    'Client',
]
