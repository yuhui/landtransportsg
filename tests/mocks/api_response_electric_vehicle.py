# Copyright 2025 Yuhui
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

# pylint: disable=line-too-long,missing-class-docstring,missing-function-docstring

"""Mock response for the ElectricVehicle module."""

class APIResponseEVChargingPoints:
    status_code = 200

    @staticmethod
    def json():
        return {
            "value": {
                "evLocationsData": [
                    {
                        "address": "1 HAMPSHIRE ROAD SINGAPORE 219428",
                        "name": "BLK 1 (LAND TRANSPORT AUTHORITY) (LTA)",
                        "longitude": 103.849331,
                        "latitude": 1.308198,
                        "locationId": "849331219428",
                        "status": "",
                        "chargingPoints": [
                            {
                                "status": "1",
                                "operatingHours": "",
                                "operator": "ST ENGINEERING URBAN SOLUTIONS LTD.",
                                "position": "L1 2",
                                "name": "BLK 1 (LAND TRANSPORT AUTHORITY) (LTA)",
                                "id": "",
                                "plugTypes": [
                                    {
                                        "plugType": "Type 2",
                                        "powerRating": "AC",
                                        "chargingSpeed": "22",
                                        "price": "",
                                        "priceType": "",
                                        "evIds": [
                                            {
                                                "id": "",
                                                "evCpId": "R119284R-001",
                                                "status": "1"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }

__all__ = [
    'APIResponseEVChargingPoints',
]
