# Copyright 2019-2026 Yuhui
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

# pylint: disable=missing-class-docstring,missing-function-docstring

"""Mock responses for the LandTransportSg module."""

class APIResponseBadLink:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'https://datamall2.mytransport.sg/ltaodataservice/$metadata#ValueStr',
            'value': [
                {
                    'Links': 'https://ltafarecard.s3.ap-southeast-1.amazonaws.com/YYYYMM/something.zip',
                },
            ],
        }

class APIResponseMissingLink:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'https://datamall2.mytransport.sg/ltaodataservice/$metadata#ValueStr',
            'value': [],
        }

class APIResponseMoreThan500RecordsPage1:
    status_code = 200

    @staticmethod
    def json():
        mock_data = {
            "BusStopCode": "01012",
            "RoadName": "Victoria St",
            "Description": "Hotel Grand Pacific",
            "Latitude": 1.29684825487647,
            "Longitude": 103.85253591654006
        }
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#BusStops",
            "value": [mock_data.copy() for _ in range(500)],
        }

class APIResponseMoreThan500RecordsPage2:
    status_code = 200

    @staticmethod
    def json():
        mock_data = {
            "BusStopCode": "01013",
            "RoadName": "Victoria St",
            "Description": "St. Joseph's Ch",
            "Latitude": 1.29770970610083,
            "Longitude": 103.8532247463225
        }
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#BusStops",
            "value": [mock_data.copy() for _ in range(500)],
        }

class APIResponseMoreThan500RecordsPage3:
    status_code = 200

    @staticmethod
    def json():
        mock_data = {
            "BusStopCode": "01019",
            "RoadName": "Victoria St",
            "Description": "Bras Basah Cplx",
            "Latitude": 1.29698951191332,
            "Longitude": 103.85302201172507
        }
        return {
            "odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/$metadata#BusStops",
            "value": [mock_data.copy() for _ in range(499)],
        }

class APIResponseValueList:
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'https://datamall2.mytransport.sg/ltaodataservice/$metadata#ValueList',
            'value': [
                {
                    'key_1': 'value_1',
                    'key_2': 'value_2',
                },
                {
                    'key_a': 'value_a',
                    'key_b': 'value_b',
                },
            ],
        }

__all__ = [
    'APIResponseBadLink',
    'APIResponseMissingLink',
    'APIResponseMoreThan500RecordsPage1',
    'APIResponseMoreThan500RecordsPage2',
    'APIResponseValueList',
]
