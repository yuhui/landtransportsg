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

from warnings import warn

from cachetools import cached, TTLCache
from typeguard import typechecked

from ..client import Lta
from ..constants import (
    CACHE_MAXSIZE,
    CACHE_ONE_MINUTE,
    CACHE_TWO_MINUTES,
    CACHE_FIVE_MINUTES,
    CACHE_ONE_DAY,
)
from ..types import Url

from .constants import (
    CARPARK_AVAILABILITY_API_ENDPOINT,
    ESTIMATED_TRAVEL_TIMES_API_ENDPOINT,
    FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT,
    ROAD_OPENINGS_API_ENDPOINT,
    ROAD_WORKS_API_ENDPOINT,
    TRAFFIC_FLOW_API_ENDPOINT,
    TRAFFIC_IMAGES_API_ENDPOINT,
    TRAFFIC_INCIDENTS_API_ENDPOINT,
    TRAFFIC_SPEED_BANDS_API_ENDPOINT,
    VMS_API_ENDPOINT,
)
from .types import (
    CarParkAvailabilityDict,
    EstimatedTravelTimesDict,
    FaultyTrafficLightsDict,
    RoadOpeningsDict,
    RoadWorksDict,
    TrafficImagesDict,
    TrafficIncidentsDict,
    TrafficSpeedBandsDict,
    VMSDict,
)

class Client(Lta):
    """Interact with the traffic-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    @typechecked
    def carpark_availability(self) -> list[CarParkAvailabilityDict | dict]:
        """Get number of available lots from HDB, LTA and URA carpark data.

        :return: Available carpark lots.
        :rtype: list[CarParkAvailabilityDict]
        """
        carpark_availability: list[CarParkAvailabilityDict | dict]

        carpark_availability = self.send_request(
            CARPARK_AVAILABILITY_API_ENDPOINT,
        )

        return carpark_availability

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    @typechecked
    def erp_rates(self) -> list[None]:
        """Get ERP rates of all vehicle types across all timings for each \
        zone.

        This endpoint was removed from DataMall v6.1 on 30 September 2024. \
        This method will be removed in this package's next major release.

        :warns DeprecationWarning: Inform the developer that this method has
            been deprecated.

        :return: ERP rates per vehicle type by zones. Empty list.
        :rtype: list[None]
        """
        warn(
            'ERP rates was removed from LTA DataMall v6.1 on 30 September 2024.',
            DeprecationWarning
        )

        erp_rates: list[None] = []

        return erp_rates

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    @typechecked
    def estimated_travel_times(self) -> list[EstimatedTravelTimesDict | dict]:
        """Get estimated travel times of expressways (in segments).

        :return: Expressway estimated travel times by segments.
        :rtype: list[EstimatedTravelTimesDict]
        """
        estimated_travel_times: list[EstimatedTravelTimesDict | dict]

        estimated_travel_times = self.send_request(
            ESTIMATED_TRAVEL_TIMES_API_ENDPOINT,
        )

        return estimated_travel_times

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWO_MINUTES))
    @typechecked
    def faulty_traffic_lights(self) -> list[FaultyTrafficLightsDict | dict]:
        """Get alerts of traffic lights that are currently faulty, or \
        currently undergoing scheduled maintenance.

        :return: Traffic light alerts and their status.
        :rtype: list[FaultyTrafficLightsDict]
        """
        faulty_traffic_lights: list[FaultyTrafficLightsDict | dict]

        faulty_traffic_lights = self.send_request(
            FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT,
        )

        return faulty_traffic_lights

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    @typechecked
    def road_openings(self) -> list[RoadOpeningsDict | dict]:
        """Get all planned road openings.

        :return: Road openings for road works.
        :rtype: list[RoadOpeningsDict]
        """
        road_openings: list[RoadOpeningsDict | dict]

        road_openings = self.send_request(ROAD_OPENINGS_API_ENDPOINT)

        return road_openings

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    @typechecked
    def road_works(self) -> list[RoadWorksDict | dict]:
        """Get approved road works to be carried out/being carried out.

        :return: Road works to be carried out/being carried out.
        :rtype: list[RoadWorksDict]
        """
        road_works: list[RoadWorksDict | dict]

        road_works = self.send_request(ROAD_WORKS_API_ENDPOINT)

        return road_works

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    @typechecked
    def traffic_images(self) -> list[TrafficImagesDict | dict]:
        """Get links to images of live traffic conditions along expressways \
        and Woodlands & Tuas Checkpoints.

        :return: Traffic images at expressways and checkpoints.
        :rtype: list[TrafficImagesDict]
        """
        traffic_images: list[TrafficImagesDict | dict]

        traffic_images = self.send_request(TRAFFIC_IMAGES_API_ENDPOINT)

        return traffic_images

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWO_MINUTES))
    @typechecked
    def traffic_incidents(self) -> list[TrafficIncidentsDict | dict]:
        """Get incidents currently happening on the roads, such as Accidents, \
        Vehicle Breakdowns, Road Blocks, Traffic Diversions etc.

        :return: Traffic incidents currently happening.
        :rtype: list[TrafficIncidentsDict]
        """
        traffic_incidents: list[TrafficIncidentsDict | dict]

        traffic_incidents = self.send_request(TRAFFIC_INCIDENTS_API_ENDPOINT)

        return traffic_incidents

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    @typechecked
    def traffic_speed_bands(self) -> list[TrafficSpeedBandsDict | dict]:
        """Get current traffic speeds on expressways and arterial roads, \
        expressed in speed bands.

        :return: Traffic speed bands on expressways and arterial roads.
        :rtype: list[TrafficSpeedBandsDict]
        """
        traffic_speed_bands: list[TrafficSpeedBandsDict | dict]

        traffic_speed_bands = self.send_request(
            TRAFFIC_SPEED_BANDS_API_ENDPOINT,
        )

        return traffic_speed_bands

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWO_MINUTES))
    @typechecked
    def vms(self) -> list[VMSDict | dict]:
        """Get traffic advisories (via variable message services) concerning \
        current traffic conditions that are displayed on EMAS signboards \
        along expressways and arterial roads.

        :return: Traffic advisories for expressways and arterial roads.
        :rtype: list[VMSDict]
        """
        vms: list[VMSDict | dict]

        vms = self.send_request(VMS_API_ENDPOINT)

        return vms

__all__ = [
    'Client',
]
