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

name = 'landtransportsg'
version = '1.1.0'
author = 'Yuhui'
author_email = 'yuhuibc@gmail.com'

from .active_mobility import Client as ActiveMobility
from .public_transport import Client as PublicTransport
from .traffic import Client as Traffic

__all__ = [
    'ActiveMobility',
    'PublicTransport',
    'Traffic',
]