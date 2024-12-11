# Copyright 2019-2024 Yuhui
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

"""Mock response to return an error response."""

class APIResponseFault(object):
    status_code = 500

    @staticmethod
    def json():
        return {
            'fault': {
                'faultstring': 'Rate limit quota violation. Quota limit  exceeded. Identifier : API_KEY',
                'detail': {
                    'errorcode': 'policies.ratelimit.QuotaViolation',
                },
            },
        }
