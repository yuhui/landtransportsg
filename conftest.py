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

# pylint: disable=invalid-name,missing-function-docstring,unused-argument,wildcard-import

"""Mock response to return link response."""

import pytest
from requests_cache import CachedSession

from tests.mocks.api_response_link import APIResponseLink

@pytest.fixture
def mock_requests_link_response(monkeypatch):
    """Requests.get() mocked to return sample API response with value string."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseLink()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)
