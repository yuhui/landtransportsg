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

"""Mock response for the BusArrival endpoint."""

class APIResponseBusArrival(object):
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusArrivalv2/@Element',
            'BusStopCode': '83139',
            'Services': [
                {
                    'ServiceNo': '15',
                    'Operator': 'GAS',
                    'NextBus': {},
                    'NextBus2': {},
                    'NextBus3': {},
                },
            ],
        }
