# Copyright 2019-2024 Yuhui. All rights reserved.
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

"""Exceptions that could occur when interacting with any API endpoint."""

from typing import Optional

from typeguard import typechecked

@typechecked
class APIError(Exception):
    """Error when the API returns an error.

    :param message: The general error message to display when the error is \
        raised.
    :type message: str

    :param errors: Other messages that were part of the raised error. \
        Defaults to None.
    :type errors: list[str]
    """
    def __init__(
        self,
        message: str,
        errors: Optional[list[str]]=None
    ) -> None:
        """Constructor method"""
        super().__init__(message)
        if errors:
            self.errors = errors

__all__ = [
    'APIError',
]
