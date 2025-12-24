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

"""Electric Vehicle custom types."""

from typing import TypedDict

class _EVChargingPointsLocationDataChargingPointPlugTypeEVIdDict(TypedDict):
    """Type definition for \
        _EVChargingPointsLocationDataChargingPointPlugTypeDict
    """

    id: str | None
    """Refer to evCpId."""
    evCpId: str
    """Connector ID. Assigned by LTA during charger registration. EV Charger \
        Registration Code makes up first 8 characters.

    :example: "R123456A-001"
    """
    status: str | None
    """Current status of the charger.

    - "0" - Occupied. Includes following OCPI statuses:
        - CHARGING
        - RESERVED
        - BLOCKED
    - "1" - Available. Includes the following OCPI statuses:
        - AVAILABLE
    - "None" - Not Available. Includes the following OCPI statuses:
        - OUTOFORDER
        - INOPERATIVE
        - UNKNOWN
        - PLANNED
        - REMOVED

    :example: "1"
    """

class _EVChargingPointsLocationDataChargingPointPlugTypeDict(TypedDict):
    """Type definition for _EVChargingPointsLocationDataChargingPointDict"""

    plugType: str
    """Plug type of the charging point.

    :example: "Type 2"
    """
    powerRating: str
    """Power rating of the charging point.

    :example: "AC"
    """
    chargingSpeed: float
    """Charging speed of the charging point. Unit: kW.

    :example: 7.4
    """
    price: float | None
    """Charging price, including Value Added Tax.

    :example: 0.70
    """
    priceType: str | None
    """Price type of the charging price.

    - "h"
    - "kWh"

    :example: "kWh"
    """
    evIds: list[_EVChargingPointsLocationDataChargingPointPlugTypeEVIdDict]
    """List of plug IDs."""

class _EVChargingPointsLocationDataChargingPointDict(TypedDict):
    """Type definition for EVChargingPointsDict"""

    status: str
    """Current status of the charger.

    - "0" - Occupied. All charging points are occupied.
    - "1" - Available. At least one charging point is available.
    - "100" - Not Available. All charging points are not available.

    :example: "1"
    """
    operatingHours: str | None
    """Operation hours of the charger."""
    operator: str
    """Charging operator of the charger.

    :example: "EVCO A"
    """
    position: str
    """Position of the charger.

    :example: "L1 Lot 123"
    """
    name: str
    """Name of the charger.

    :example: "123 Road A"
    """
    id: str | None
    """ID of the charger."""
    plugTypes: list[_EVChargingPointsLocationDataChargingPointPlugTypeDict]
    """List of plug types."""

class _EVChargingPointsLocationDataDict(TypedDict):
    """Type definition for EVChargingPointsDict"""

    address: str
    """Address of the charging station.

    :example: "123 Road A Singapore 123456"
    """
    name: str
    """Name of charging station.

    :example: "123 Road A"
    """
    longitude: float
    """Longitude map coordinates of charging station.

    :example: 103.123456
    """
    latitude: float
    """Latitude map coordinates of charging station.

    :example: 1.123456
    """
    locationId: str
    """Location Id of charging station. Made up from the first 6 decimal \
        places of longitude followed by postal code..

    :example: "123456123456"
    """
    status: str | None
    """Status of charging station."""
    chargingPoints: list[_EVChargingPointsLocationDataChargingPointDict]
    """List of charging points."""

class EVChargingPointsDict(TypedDict):
    """Type definition for ev_charging_points()"""
    evLocationsData: list[_EVChargingPointsLocationDataDict]
    """List of EV charging point location data."""

__all__ = [
    '_EVChargingPointsLocationDataChargingPointPlugTypeEVIdDict',
    '_EVChargingPointsLocationDataChargingPointPlugTypeDict',
    '_EVChargingPointsLocationDataChargingPointDict',
    '_EVChargingPointsLocationDataDict',
    'EVChargingPointsDict',
]
