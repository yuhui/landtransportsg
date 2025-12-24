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

"""Mock response for the ActiveMobility module."""

class APIResponseBicycleParking:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#BicycleParkingv2",
            "value": [
                {
                    "Description": "BUS STOP 43061",
                    "Latitude": 1.363109,
                    "Longitude": 103.767371,
                    "RackType": "Yellow Box",
                    "RackCount": 10,
                    "ShelterIndicator": "N",
                },
                {
                    "Description": "BUS STOP 43069",
                    "Latitude": 1.362658,
                    "Longitude": 103.767735,
                    "RackType": "Yellow Box",
                    "RackCount": 10,
                    "ShelterIndicator": "N",
                },
            ],
        }

__all__ = [
    'APIResponseBicycleParking',
]
