# Copyright 2019-2025 Yuhui
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

# pylint: disable=missing-class-docstring,missing-function-docstring

"""Mock responses for the LandTransportSg module."""

class APIResponseBadLink:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'https://datamall2.mytransport.sg/ltaodataservice/$metadata#ValueStr',
            'value': [
                {
                    'Links': 'https://ltafarecard.s3.ap-southeast-1.amazonaws.com/YYYYMM/something.zip',
                },
            ],
        }

class APIResponseFault:
    status_code = 500

    @staticmethod
    def json():
        return {
            'fault': {
                'faultstring': 'Rate limit quota violation. Quota limit exceeded. Identifier : API_KEY',
                'detail': {
                    'errorcode': 'policies.ratelimit.QuotaViolation',
                },
            },
        }

class APIResponseMissingLink:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'https://datamall2.mytransport.sg/ltaodataservice/$metadata#ValueStr',
            'value': [],
        }

class APIResponseValueList:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'https://datamall2.mytransport.sg/ltaodataservice/$metadata#ValueList',
            'value': [
                {
                    'key_1': 'value_1',
                    'key_2': 'value_2',
                },
                {
                    'key_a': 'value_a',
                    'key_b': 'value_b',
                },
            ],
        }

__all__ = [
    'APIResponseBadLink',
    'APIResponseFault',
    'APIResponseMissingLink',
    'APIResponseValueList',
]
