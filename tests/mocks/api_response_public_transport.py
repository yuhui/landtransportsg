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

"""Mock responses for the PublicTransport module."""

class APIResponseBusArrival:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival",
            "BusStopCode": "83139",
            "Services": [
                {
                    "ServiceNo": "15",
                    "Operator": "GAS",
                    "NextBus": {
                        "OriginCode": "77009",
                        "DestinationCode": "77009",
                        "EstimatedArrival": "2025-12-23T10:43:34+08:00",
                        "Monitored": 1,
                        "Latitude": "1.331865",
                        "Longitude": "103.90255316666666",
                        "VisitNumber": "1",
                        "Load": "SEA",
                        "Feature": "WAB",
                        "Type": "SD"
                    },
                    "NextBus2": {
                        "OriginCode": "77009",
                        "DestinationCode": "77009",
                        "EstimatedArrival": "2025-12-23T10:47:08+08:00",
                        "Monitored": 1,
                        "Latitude": "1.3352045",
                        "Longitude": "103.909877",
                        "VisitNumber": "1",
                        "Load": "SEA",
                        "Feature": "WAB",
                        "Type": "SD"
                    },
                    "NextBus3": {
                        "OriginCode": "77009",
                        "DestinationCode": "77009",
                        "EstimatedArrival": "2025-12-23T10:52:37+08:00",
                        "Monitored": 1,
                        "Latitude": "1.3473528333333333",
                        "Longitude": "103.92304933333334",
                        "VisitNumber": "1",
                        "Load": "SEA",
                        "Feature": "WAB",
                        "Type": "SD"
                    }
                }
            ]
        }

class APIResponseBusRoutes:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadataBusRoutes",
            "value": [
                {
                    "ServiceNo": "10",
                    "Operator": "SBST",
                    "Direction": 1,
                    "StopSequence": 1,
                    "BusStopCode": "75009",
                    "Distance": 0,
                    "WD_FirstBus": "0500",
                    "WD_LastBus": "2300",
                    "SAT_FirstBus": "0500",
                    "SAT_LastBus": "2300",
                    "SUN_FirstBus": "0500",
                    "SUN_LastBus": "2300"
                }
            ],
        }

class APIResponseBusServices:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#BusServices",
            "value": [
                {
                    "ServiceNo": "15",
                    "Operator": "GAS",
                    "Direction": 1,
                    "Category": "TRUNK",
                    "OriginCode": "77009",
                    "DestinationCode": "77009",
                    "AM_Peak_Freq": "04-09",
                    "AM_Offpeak_Freq": "04-13",
                    "PM_Peak_Freq": "07-15",
                    "PM_Offpeak_Freq": "13-16",
                    "LoopDesc": "Marine Parade Rd"
                }
            ],
        }

class APIResponseBusStops:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#BusStops",
            "value": [
                {
                    "BusStopCode": "01012",
                    "RoadName": "Victoria St",
                    "Description": "Hotel Grand Pacific",
                    "Latitude": 1.29684825487647,
                    "Longitude": 103.85253591654006
                }
            ],
        }

class APIResponseFacilitiesMaintenance:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/v2/FacilitiesMaintenance",
            "value": [
                {
                    "Line": "DTL",
                    "StationCode": "DT2",
                    "StationName": "Cashew",
                    "LiftID": "B1L01",
                    "LiftDesc": "EXIT A STREET LEVEL - CONCOURSE"
                }
            ],
        }

class APIResponseStationCrowdDensityForecast:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/PcdForecast",
            "value": [
                {
                    "Date": "2025-12-22T00:00:00+08:00",
                    "Stations": [
                        {
                            "Station": "EW1",
                            "Interval": [
                                {
                                    "Start": "2025-12-23T00:00:00+08:00",
                                    "CrowdLevel": "l"
                                }
                            ]
                        }
                    ]
                }
            ],
        }

class APIResponseStationCrowdDensityRealTime:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#PcdRealTime",
            "value": [
                {
                    "Station": "EW1",
                    "StartTime": "2025-12-23T10:20:00+08:00",
                    "EndTime": "2025-12-23T10:30:00+08:00",
                    "CrowdLevel": "l"
                }
            ],
        }

class APIResponseTaxiAvailability:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#TaxiAvailability",
            "value": [
                {
                    "Longitude": 103.8749938086,
                    "Latitude": 1.3128455285
                }
            ],
        }

class APIResponseTaxiStands:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#TaxiStands",
            "value": [
                {
                    "TaxiCode": "A01",
                    "Latitude": 1.304294727,
                    "Longitude": 103.8338467,
                    "Bfa": "Yes",
                    "Ownership": "LTA",
                    "Type": "Stand",
                    "Name": "Orchard Rd along driveway of Lucky Plaza"
                }
            ],
        }

class APIResponseTrainServiceAlerts:
    status_code = 200

    @staticmethod
    def json():
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#TrainServicesAlerts",
            "value": {
                "Status": 1,
                "AffectedSegments": [
                    {
                        "Line": "NEL",
                        "Direction": "HarbourFront",
                        "Stations": "NE9,NE8,NE7,NE6",
                        "FreePublicBus": "",
                        "FreeMRTShuttle": "",
                        "MRTShuttleDirection": ""
                    }
                ],
                "Message": [
                    {
                        "Content": "1710hrs: NEL - No train service between Harbourfront to Dhoby Ghaut stations towards Punggol station due to a signalling fault. Free bus rides are available at designated bus stops",
                        "CreatedDate": "2017-12-01 17:54:21"
                    }
                ],
            },
        }

__all__ = [
    'APIResponseBusArrival',
    'APIResponseBusRoutes',
    'APIResponseBusServices',
    'APIResponseBusStops',
    'APIResponseFacilitiesMaintenance',
    'APIResponseStationCrowdDensityForecast',
    'APIResponseStationCrowdDensityRealTime',
    'APIResponseTaxiAvailability',
    'APIResponseTaxiStands',
    'APIResponseTrainServiceAlerts',
]
