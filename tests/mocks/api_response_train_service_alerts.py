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

# pylint: disable=line-too-long,missing-class-docstring,missing-function-docstring

"""Mock response for the TrainServiceAlerts endpoint."""

class APIResponseTrainServiceAlerts:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'http://datamall2.mytransport.sg/ltaodataservice/$metadata#TrainServicesAlerts',
            'value': {
                'Status': 1,
                'AffectedSegments': [],
                'Message': [],
            },
        }
