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

# pylint: disable=line-too-long,missing-class-docstring,missing-function-docstring

"""Mock responses for the Traffic module."""

class APIResponseCarParkAvailability:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#CarParkAvailability",
            "value": [
                {
                    "CarParkID": "C29",
                    "Area": "",
                    "Development": "BLK 501-505 WEST COAST DRIVE",
                    "Location": "1.3126146115229127 103.75923178966639",
                    "AvailableLots": 136,
                    "LotType": "C",
                    "Agency": "HDB"
                }
            ]
        }

class APIResponseEstimatedTravelTimes:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#EstTravelTimes",
            "value": [
                {
                    "Name": "AYE",
                    "Direction": 2,
                    "FarEndPoint": "CITY",
                    "StartPoint": "TUAS CHECKPOINT",
                    "EndPoint": "TUAS WEST RD",
                    "EstTime": 1
                }
            ],
        }

class APIResponseFaultyTrafficLights:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#FaultyTrafficLights",
            "value": [
                {
                    "AlarmID": "GLSC_2_7604_10931391",
                    "NodeID": "16704",
                    "Type": "2",
                    "StartDate": "",
                    "EndDate": "",
                    "Message": "(23/12)10:43 Black Out at CIRCUIT RD/CIRCUIT LINK."
                }
            ],
        }

class APIResponseRoadOpenings:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#RoadOpenings",
            "value": [
                {
                    "EventID": "RMINRM-202510-0239",
                    "StartDate": "2026-01-01",
                    "EndDate": "2026-01-19",
                    "SvcDept": "LAND TRANSPORT AUTHORITY",
                    "RoadName": "KEPPEL ROAD (Bus Lane Affected)",
                    "Other": "For all details,please call +65  63326943"
                }
            ],
        }

class APIResponseRoadWorks:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#RoadWorks",
            "value": [
                {
                    "EventID": "RMAPP-201912-0496",
                    "StartDate": "2019-12-13",
                    "EndDate": "2027-02-28",
                    "SvcDept": "PRIVATE",
                    "RoadName": "REPUBLIC AVENUE",
                    "Other": "For all details"
                }
            ],
        }

class APIResponseTrafficImages:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#Traffic-Imagesv2",
            "value": [
                {
                    "CameraID": "1001",
                    "Latitude": 1.29531332,
                    "Longitude": 103.871146,
                    "ImageLink": "https://dm-traffic-camera-itsc.s3.ap-southeast-1.amazonaws.com/2025-12-23/00-25/1001_0023_20251222162550_09BFB9.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaDmFwLXNvdXRoZWFzdC0xIkcwRQIhANkvM2K7ziaMMnQcNAvUYHYTSKv%2FjhMoXrtPt6SbUdi0AiAw0EUnkblNOUgQf9qggS9TW6KlIYGyXkQ5q22rDPQCeCqEAwj5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAQaDDM0MDY0NTM4MTMwNCIMw13vYCUACmRpvhDeKtgC5BAZ0f0%2FAVXW5H2PaO7aiixzHY2DFYt4ahfrXirsccbfzbwpHyeRNzK3YVQr0oVUL9yZN5roPxORS01v%2FhqSwGmpWl%2Fc86COS8UyleVay8zflcgO%2BL5B8xOyoaLPdM3CGMfQ9TsQwzPWt0V%2BwW7VIrhw9MRS7hcvojSivIt6avZa6bzlPjuqAWZG774j0OA72hV2dO2agQAWITTzDxwgz7ZCFHF%2BlzQQ9bwtexWMpl93XRoKBCdmTGnO19SrgmejZltgcdwuHKGre4FNgH4GPFEYHc0Tv60C3CET3XGAqRHQNewpK8uFdEhxiFE7wmhw%2BV5h2ASMFaNQvVXj9IID0frFJuKVzicoKUD%2BN1fs%2BBUVXghH5k1nsKOqhqe%2BcbEfO6uIMqoj3XNoW0%2FXKLVlKzoIWZ2K5mbgIBOJe5LcKwW%2Be3XwCedl4aO68m7kpVjxmKDDo1AmCU4w8culygY6ngHibYDIkNZnbiLHRlyvm%2Fz%2FqJ2OnIuFm9%2F4FBhB9VkPOwipdZXCoLWCAH97zTtSwKKIYSGEwM2zJNMxSbHBeWbjxZVL98fn3%2FVcQPbTLmAUfWoNtTQGU96mQ9KuiMAYxP49Jk6hi7j58SXUznVO7eRzRM1xLkNxEPWT5UkxRtWIdYrn2CFu1t9Yf2kdg1SOkUPHtwJUk15cT9qTNkGw6w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251222T162550Z&X-Amz-SignedHeaders=host&X-Amz-Credential=ASIAU6UAMAS4JP3RNLGP%2F20251222%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Expires=900&X-Amz-Signature=157e157c98d8a4e9a62e27fec64fd4d31aa1990aea13660d02ef0c5af22e5205"
                }
            ],
        }

class APIResponseTrafficIncidents:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#IncidentSet",
            "value": [
                {
                    "Type": "Roadwork",
                    "Latitude": 1.2887628319444955,
                    "Longitude": 103.84176404675743,
                    "Message": "(23/12)00:26 Road Works in CTE Tunnel (towards AYE) after Havelock. Avoid lane 3."
                }
            ],
        }

class APIResponseTrafficSpeedBands:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#TrafficSpeedBands",
            "lastUpdatedTime": "2025-12-23 00:30:00",
            "value": [
                {
                    "LinkID": "103011995",
                    "RoadName": "NARAYANAN CHETTY ROAD",
                    "RoadCategory": "E",
                    "SpeedBand": 3,
                    "MinimumSpeed": "20",
                    "MaximumSpeed": "29",
                    "StartLon": "103.83838061586873",
                    "StartLat": "1.2921590838224843",
                    "EndLon": "103.83817446261223",
                    "EndLat": "1.2917846048262231"
                }
            ],
        }

class APIResponseVMS:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#VMS",
            "value": [
                {
                    "EquipmentID": "EVMS_RV10",
                    "Latitude": 1.3415545552453492,
                    "Longitude": 103.89864657075502,
                    "Message": "HEAVY TRAFFIC,KPE(TPE),TPE(SLE) EXIT"
                }
            ],
        }

__all__ = [
    'APIResponseCarParkAvailability',
    'APIResponseEstimatedTravelTimes',
    'APIResponseFaultyTrafficLights',
    'APIResponseRoadOpenings',
    'APIResponseRoadWorks',
    'APIResponseTrafficImages',
    'APIResponseTrafficIncidents',
    'APIResponseTrafficSpeedBands',
    'APIResponseVMS',
]
