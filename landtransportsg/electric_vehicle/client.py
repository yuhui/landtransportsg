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

"""Client for interacting with the Electric Vehicle API endpoints."""

from re import fullmatch
from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_FIVE_MINUTES
from ..landtransportsg import LandTransportSg

from .constants import (
    EV_CHARGING_POINTS_API_ENDPOINT,
    EV_CHARGING_POINTS_ARGS_KEY_MAP,

    EV_CHARGING_POINTS_SANITISE_IGNORE_KEYS,
)
from .types_args import EVChargingPointsArgsDict
from .types import EVChargingPointsDict

class Client(LandTransportSg):
    """Interact with the electric vehicle-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @typechecked
    def ev_charging_points(
        self,
        **kwargs: Unpack[EVChargingPointsArgsDict],
    ) -> EVChargingPointsDict:
        """Returns electric vehicle charging points in Singapore and their \
        availabilities.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EVChargingPointsArgsDict

        :raises ValueError: postal_code is not a 6-digit string.

        :return: Available EV charging points at the specified location.
        :rtype: EVChargingPointsDict
        """
        ev_charging_points: EVChargingPointsDict

        params = self.build_params(
            params_expected_type=EVChargingPointsArgsDict,
            original_params=kwargs,
            key_map=EV_CHARGING_POINTS_ARGS_KEY_MAP,
        )

        postal_code = params['PostalCode']

        if fullmatch('[0-9]{6}', postal_code) is None:
            raise ValueError('Argument "postal_code" must be a 6-digit string.')

        ev_charging_points = self.send_request(
            EV_CHARGING_POINTS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_FIVE_MINUTES,
            sanitise_ignore_keys=EV_CHARGING_POINTS_SANITISE_IGNORE_KEYS,
        )

        return ev_charging_points

__all__ = [
    'Client',
]
