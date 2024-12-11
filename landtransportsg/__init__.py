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

from datetime import datetime

from .active_mobility import Client as ActiveMobility
from .geospatial import Client as Geospatial
from .public_transport import Client as PublicTransport
from .traffic import Client as Traffic

NAME = 'landtransportsg'
VERSION = '2.0.0' # Production
# VERSION = f'{VERSION}.{datetime.now().strftime("%Y%m%d%H%M")}' # Development
AUTHOR = 'Yuhui'
AUTHOR_EMAIL = 'yuhuibc@gmail.com'

__all__ = [
    'ActiveMobility',
    'Geospatial',
    'PublicTransport',
    'Traffic',
]
__version__ = VERSION
