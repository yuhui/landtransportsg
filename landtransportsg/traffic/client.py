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

"""Client for interacting with the Traffic API endpoints."""

from warnings import warn

from typeguard import typechecked

from ..constants import (
    CACHE_ONE_MINUTE,
    CACHE_TWO_MINUTES,
    CACHE_FIVE_MINUTES,
    CACHE_ONE_DAY,
)
from ..landtransportsg import LandTransportSg
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

    FAULTY_TRAFFIC_LIGHTS_SANITISE_IGNORE_KEYS,
    TRAFFIC_IMAGES_SANITISE_IGNORE_KEYS,
    TRAFFIC_SPEED_BANDS_SANITISE_IGNORE_KEYS,
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

class Client(LandTransportSg):
    """Interact with the traffic-related endpoints.

    References: \
        https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf
    """

    @typechecked
    def carpark_availability(self) -> list[CarParkAvailabilityDict]:
        """Get number of available lots from HDB, LTA and URA carpark data.

        :return: Available carpark lots.
        :rtype: list[CarParkAvailabilityDict]
        """
        carpark_availability: list[CarParkAvailabilityDict]

        carpark_availability = self.send_request(
            CARPARK_AVAILABILITY_API_ENDPOINT,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return carpark_availability

    @typechecked
    def erp_rates(self) -> list[None]:
        """Get ERP rates of all vehicle types across all timings for each \
        zone.

        This endpoint was removed from DataMall v6.1 on 30 September 2024. \
        This method will be removed from this package's next major release or \
        31 December 2025, whichever comes earlier.

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

    @typechecked
    def estimated_travel_times(self) -> list[EstimatedTravelTimesDict]:
        """Get estimated travel times of expressways (in segments).

        :return: Expressway estimated travel times by segments.
        :rtype: list[EstimatedTravelTimesDict]
        """
        estimated_travel_times: list[EstimatedTravelTimesDict]

        estimated_travel_times = self.send_request(
            ESTIMATED_TRAVEL_TIMES_API_ENDPOINT,
            cache_duration=CACHE_FIVE_MINUTES,
        )

        return estimated_travel_times

    @typechecked
    def faulty_traffic_lights(self) -> list[FaultyTrafficLightsDict]:
        """Get alerts of traffic lights that are currently faulty, or \
        currently undergoing scheduled maintenance.

        :return: Traffic light alerts and their status.
        :rtype: list[FaultyTrafficLightsDict]
        """
        faulty_traffic_lights: list[FaultyTrafficLightsDict]

        faulty_traffic_lights = self.send_request(
            FAULTY_TRAFFIC_LIGHTS_API_ENDPOINT,
            cache_duration=CACHE_TWO_MINUTES,
            sanitise_ignore_keys=FAULTY_TRAFFIC_LIGHTS_SANITISE_IGNORE_KEYS,
        )

        return faulty_traffic_lights

    @typechecked
    def road_openings(self) -> list[RoadOpeningsDict]:
        """Get all planned road openings.

        :return: Road openings for road works.
        :rtype: list[RoadOpeningsDict]
        """
        road_openings: list[RoadOpeningsDict]

        road_openings = self.send_request(
            ROAD_OPENINGS_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
        )

        return road_openings

    @typechecked
    def road_works(self) -> list[RoadWorksDict]:
        """Get approved road works to be carried out/being carried out.

        :return: Road works to be carried out/being carried out.
        :rtype: list[RoadWorksDict]
        """
        road_works: list[RoadWorksDict]

        road_works = self.send_request(
            ROAD_WORKS_API_ENDPOINT,
            cache_duration=CACHE_ONE_DAY,
        )

        return road_works

    @typechecked
    def traffic_flow(self) -> Url:
        """Get hourly average traffic flow, taken from a representative month \
        of every quarter during 0700-0900 hours.

        :return: Link to download the hourly average traffic flow. The link \
            will expire after 5 minutes.
        :rtype: Url
        """
        traffic_flow_link: Url

        traffic_flow_link = self.send_download_request(
            TRAFFIC_FLOW_API_ENDPOINT,
            cache_duration=CACHE_FIVE_MINUTES,
        )

        return traffic_flow_link

    @typechecked
    def traffic_images(self) -> list[TrafficImagesDict]:
        """Get links to images of live traffic conditions along expressways \
        and Woodlands & Tuas Checkpoints.

        :return: Traffic images at expressways and checkpoints.
        :rtype: list[TrafficImagesDict]
        """
        traffic_images: list[TrafficImagesDict]

        traffic_images = self.send_request(
            TRAFFIC_IMAGES_API_ENDPOINT,
            cache_duration=CACHE_FIVE_MINUTES,
            sanitise_ignore_keys=TRAFFIC_IMAGES_SANITISE_IGNORE_KEYS,
        )

        return traffic_images

    @typechecked
    def traffic_incidents(self) -> list[TrafficIncidentsDict]:
        """Get incidents currently happening on the roads, such as Accidents, \
        Vehicle Breakdowns, Road Blocks, Traffic Diversions etc.

        :return: Traffic incidents currently happening.
        :rtype: list[TrafficIncidentsDict]
        """
        traffic_incidents: list[TrafficIncidentsDict]

        traffic_incidents = self.send_request(
            TRAFFIC_INCIDENTS_API_ENDPOINT,
            cache_duration=CACHE_TWO_MINUTES,
        )

        return traffic_incidents

    @typechecked
    def traffic_speed_bands(self) -> list[TrafficSpeedBandsDict]:
        """Get current traffic speeds on expressways and arterial roads, \
        expressed in speed bands.

        :return: Traffic speed bands on expressways and arterial roads.
        :rtype: list[TrafficSpeedBandsDict]
        """
        traffic_speed_bands: list[TrafficSpeedBandsDict]

        traffic_speed_bands = self.send_request(
            TRAFFIC_SPEED_BANDS_API_ENDPOINT,
            cache_duration=CACHE_FIVE_MINUTES,
            sanitise_ignore_keys=TRAFFIC_SPEED_BANDS_SANITISE_IGNORE_KEYS,
        )

        return traffic_speed_bands

    @typechecked
    def vms(self) -> list[VMSDict]:
        """Get traffic advisories (via variable message services) concerning \
        current traffic conditions that are displayed on EMAS signboards \
        along expressways and arterial roads.

        :return: Traffic advisories for expressways and arterial roads.
        :rtype: list[VMSDict]
        """
        vms: list[VMSDict]

        vms = self.send_request(
            VMS_API_ENDPOINT,
            cache_duration=CACHE_TWO_MINUTES,
        )

        return vms

__all__ = [
    'Client',
]
