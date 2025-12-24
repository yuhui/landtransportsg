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

from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_ONE_DAY
from ..landtransportsg import LandTransportSg

from .constants import (
    BICYCLE_PARKING_API_ENDPOINT,
    BICYCLE_PARKING_DEFAULT_ARGS,
    BICYCLE_PARKING_ARGS_KEY_MAP,
)
from .types_args import BicycleParkingArgsDict
from .types import BicycleParkingDict

class Client(LandTransportSg):
    """Interact with the active mobility-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @typechecked
    def bicycle_parking(
        self,
        **kwargs: Unpack[BicycleParkingArgsDict],
    ) -> list[BicycleParkingDict]:
        """Get bicycle parking locations within a radius.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: BicycleParkingArgsDict

        :raises ValueError: distance is a negative float.

        :return: Available bicycle parking locations at the specified \
            location.
        :rtype: list[BicycleParkingDict]
        """
        bicycle_parking_locations: list[BicycleParkingDict]

        params = self.build_params(
            params_expected_type=BicycleParkingArgsDict,
            original_params=kwargs,
            default_params=BICYCLE_PARKING_DEFAULT_ARGS,
            key_map=BICYCLE_PARKING_ARGS_KEY_MAP,
        )

        distance = params['Dist']

        if isinstance(distance, float) and distance < 0:
            raise ValueError('Argument "distance" cannot be less than zero.')

        bicycle_parking_locations = self.send_request(
            BICYCLE_PARKING_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_DAY,
        )

        return bicycle_parking_locations

__all__ = [
    'Client',
]
