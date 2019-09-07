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

"""Client for interacting with the Traffic API endpoints."""

from cachetools import cached, TTLCache

from .constants import *
from ..client import __Client

class Client(__Client):
    """Interact with the traffic-related endpoints.

    References:
        https://www.mytransport.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    def __init(self, account_key):
        super(Client, self).__init__(account_key)

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def carpark_availability(self):
        """Get number of available lots from HDB, LTA and URA carpark data.

        Returns:
            (list) Available carpark lots.
        """
        carpark_availability = self.send_request(
            CARPARK_AVAILABILITY_API_ENDPOINT,
        )

        return carpark_availability

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def erp_rates(self):
        """Get ERP rates of all vehicle types across all timings for each zone.

        Returns:
            (list) ERP rates per vehicle type by zones.
        """
        erp_rates = self.send_request(ERP_RATES_API_ENDPOINT)

        return erp_rates

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    def estimated_travel_times(self):
        """Get estimated travel times of expressways (in segments).

        Returns:
            (list) Expressway estimated travel times by segments.
        """
        estimated_travel_times = self.send_request(
            ESTIMATED_TRAVEL_TIMES_API_ENDPOINT,
        )

        return estimated_travel_times

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWO_MINUTES))
    def faulty_traffic_lights(self):
        """Get alerts of traffic lights that are currently faulty, or currently
        undergoing scheduled maintenance.

        Returns:
            (list) Traffic light alerts and their status.
        """
        faulty_traffic_lights = self.send_request(
            FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT,
        )

        return faulty_traffic_lights

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def road_openings(self):
        """Get all planned road openings.

        Returns:
            (list) Road openings for road works.
        """
        road_openings = self.send_request(ROAD_OPENINGS_API_ENDPOINT)

        return road_openings

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def road_works(self):
        """Get all road works being / to be carried out.

        Returns:
            (list) Road works that are being / to be carried out.
        """
        road_works = self.send_request(ROAD_WORKS_API_ENDPOINT)

        return road_works

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def traffic_images(self):
        """Get links to images of live traffic conditions along expressways
        and Woodlands & Tuas Checkpoints.

        Returns:
            (list) Traffic images at expressways and checkpoints.
        """
        traffic_images = self.send_request(TRAFFIC_IMAGES_API_ENDPOINT)

        return traffic_images

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWO_MINUTES))
    def traffic_incidents(self):
        """Get incidents currently happening on the roads, such as Accidents,
        Vehicle Breakdowns, Road Blocks, Traffic Diversions etc.

        Returns:
            (list) Traffic incidents currently happening.
        """
        traffic_incidents = self.send_request(TRAFFIC_INCIDENTS_API_ENDPOINT)

        return traffic_incidents

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    def traffic_speed_bands(self):
        """Get current traffic speeds on expressways and arterial roads,
        expressed in speed bands.

        Returns:
            (list) Traffic speed bands on expressways and arterial roads.
        """
        traffic_speed_bands = self.send_request(
            TRAFFIC_SPEED_BANDS_API_ENDPOINT,
        )

        return traffic_speed_bands

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWO_MINUTES))
    def vms(self):
        """Get traffic advisories (via variable message services) concerning
        current traffic conditions that are displayed on EMAS signboards along
        expressways and arterial roads.

        Returns:
            (list) Traffic advisories for expressways and arterial roads.
        """
        vms = self.send_request(VMS_API_ENDPOINT)

        return vms
