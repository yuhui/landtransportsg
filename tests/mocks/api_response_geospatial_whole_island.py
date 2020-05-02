# Copyright 2020 Yuhui
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

"""Mock response for the GeospatialWholeIsland endpoint."""

class APIResponseGeospatialWholeIsland(object):
    status_code = 200

    @staticmethod
    def json():
        return {
            'odata.metadata': 'http://datamall2.mytransport.sg/ltaodataservice/$metadata#GeospatialWholeIsland',
            'value': [
                {
                    'Link': 'https://dmgeospatial.s3.ap-southeast-1.amazonaws.com/ArrowMarking.zip?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aDmFwLXNvdXRoZWFzdC0xIkgwRgIhAIN4tBFM1SfwMwSlVTIOVmXVAaOSUfUdu3xBS3t2pbL%2FAiEAgjFQwaCnibEerCFMcOl0cG7UxHM2H%2BtvfxVDAjTiJmMqowMIRhABGgwzNDA2NDUzODEzMDQiDCIH4dJ4UxE9dlkkyiqAAz8iwAKuPjxRZeCB%2BxFv%2B6oBG48OW%2BqJV1y1F9THR3QoJg0LzA4giKT7SjygDFuwrQX8ZuwnGXu7ElU3FeSkvQq8jOGklK9E4wRJ%2BI20o26EI6KEXToe5IHQhDk2u7VcJs41xHIPTPbtXVFHDwHIEhwE69xRXjjZDf4zgEUUEYq%2FtQ4Ql5deGh8llcvku4WKUAK268x9jYiCW%2FNvEHySXxRSoTwIeKdX17JhfUjOrAYxfHM8EcTdJ9GMNT1q93V0G5iB0BWuJjVLdWf4UYmyn%2BZTyZNYFSZX1ef3skrloh5FxhfWa%2FKsSEwbnwYCrcA7rdw0nrM5Y4OdOVstVx%2FCaCDG3hzloVEfOuiJW5aq3T9m2%2BVRNHDgZPg4k48cs64mmQpBkSHGyzr8D8PSU0t4fsf0YOSClxJDBIp5Cls7BfusPRW9dpnPJn5LjvKM9q6oH81d0%2BcwWfYghSt7%2Ft94bWW9alpNo5Lako%2FP%2BkndAUTSDUaNLAyd0uvRtx%2FoB4w15DCM1bX1BTrqAaVoj2iN7TJBqBsKPrSJgIbK96MdHxS1L1q3qH7fTzWYjl%2BhGIHoE2a9XWda9HW9TNUsYW5JuYK7p21d6Y22H6i0dbXKLO9f2%2B8TtsN7i6XUrFmUFAp%2F6qyRdNwGUrR7r7s5c2uSBbht3aIN%2BC39E%2BKko0xVXrtB6rY%2BifTfVw0zzTNnYpJIcB2KpjOaGbnN7S4woGrxMzz8gLA%2FM7%2BnQLvs3zNX5I08IUTgF8726fA8UwaT3mcjNN0CGLIb%2BOPTuYtykBCcx246Rb%2Fiu1%2Be%2Fd2qrD2U%2BWLbLWEbF5tVzvYDZlF8oXASvQZxgQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200502T142446Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAU6UAMAS4A7N6OC5N%2F20200502%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Signature=6d6d3c35e7dfefb3670f766cf61ecc2f620667916ed7b9c614e2c8e39f1f4680',
                },
            ],
        }
