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

# pylint: disable=invalid-name,missing-function-docstring,unused-argument,wildcard-import

import pytest
from requests import Session

from tests.mocks.api_response_value_list import APIResponseValueList
from tests.mocks.api_response_value_str import *

@pytest.fixture
def mock_requests_value_list_response(monkeypatch):
    """Requests.get() mocked to return sample API response with value list."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseValueList()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def mock_requests_value_str_response(monkeypatch):
    """Requests.get() mocked to return sample API response with value string."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseValueStr()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def mock_requests_value_str_bad_value_response(monkeypatch):
    """Requests.get() mocked to return sample API response with bad 'value'."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseValueStrBadValue()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def mock_requests_value_str_missing_link_response(monkeypatch):
    """Requests.get() mocked to return sample API response with missing 'Link'."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseValueStrMissingLink()

    monkeypatch.setattr(Session, 'get', mock_requests_get)

@pytest.fixture
def mock_requests_value_str_bad_link_response(monkeypatch):
    """Requests.get() mocked to return sample API response with bad 'Link'."""

    def mock_requests_get(*args, **kwargs):
        return APIResponseValueStrBadLink()

    monkeypatch.setattr(Session, 'get', mock_requests_get)
