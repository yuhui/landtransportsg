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

"""Test that the timezone functions are working properly."""

import pytest

from datetime import date, datetime
from freezegun import freeze_time
from pytz import timezone as pytimezone

from landtransportsg import timezone

# constants for testing last three months-related dates
GOOD_CUTOFF_DAY = 15
LEAP_YEAR_DATE = freeze_time('2018-03-17')
NON_LEAP_YEAR_DATE = freeze_time('2019-06-03')

@pytest.mark.parametrize(
    ('date_time', 'expected_hour'),
    [
        (datetime(2019, 7, 1, 8), 8),
        (datetime(2019, 7, 1, 8, tzinfo=pytimezone('Asia/Singapore')), 8),
        (datetime(2019, 7, 1, 8, tzinfo=pytimezone('UTC')), 16),
    ],
)
def test_datetime_as_sgt(date_time, expected_hour):
    sgt_date_time = timezone.datetime_as_sgt(date_time)
    assert sgt_date_time.hour is expected_hour

@pytest.mark.parametrize(
    'date_time',
    ['2019-07-13 08:32:17', '2019-07-13 08:32:17+08:00'],
)
def test_datetime_as_sgt_from_bad_datetime(date_time):
    with pytest.raises(ValueError):
        _ = timezone.datetime_as_sgt(date_time)

@pytest.mark.parametrize(
    ('date_time_str', 'expected_date_time'),
    [
        ('2019-07-13 08:32:17', datetime(2019, 7, 13, 8, 32, 17)),
        ('2019-07-13', date(2019, 7, 13)),
    ],
)
def test_datetime_from_string(date_time_str, expected_date_time):
    date_time = timezone.datetime_from_string(date_time_str)
    if isinstance(expected_date_time, datetime):
        expected_date_time = timezone.datetime_as_sgt(expected_date_time)
    assert date_time == expected_date_time

@pytest.mark.parametrize(
    'date_time_str',
    ['foobar', '2019-07-13 08:32', '2019-07 08:32:17', '2019-07'],
)
def test_datetime_from_bad_string(date_time_str):
    with pytest.raises(ValueError):
        _ = timezone.datetime_from_string(date_time_str)

@pytest.mark.parametrize(
    ('fake_today', 'offset_months', 'cutoff_day', 'expected'),
    [
        (LEAP_YEAR_DATE, 0, GOOD_CUTOFF_DAY, False),
        (LEAP_YEAR_DATE, 1, GOOD_CUTOFF_DAY, 'greater or equals'),
        (LEAP_YEAR_DATE, 2, GOOD_CUTOFF_DAY, True),
        (LEAP_YEAR_DATE, 3, GOOD_CUTOFF_DAY, True),
        (LEAP_YEAR_DATE, 4, GOOD_CUTOFF_DAY, 'less than'),
        (LEAP_YEAR_DATE, 5, GOOD_CUTOFF_DAY, False),
        (NON_LEAP_YEAR_DATE, 0, GOOD_CUTOFF_DAY, False),
        (NON_LEAP_YEAR_DATE, 1, GOOD_CUTOFF_DAY, 'greater or equals'),
        (NON_LEAP_YEAR_DATE, 2, GOOD_CUTOFF_DAY, True),
        (NON_LEAP_YEAR_DATE, 3, GOOD_CUTOFF_DAY, True),
        (NON_LEAP_YEAR_DATE, 4, GOOD_CUTOFF_DAY, 'less than'),
        (NON_LEAP_YEAR_DATE, 5, GOOD_CUTOFF_DAY, False),
    ]
)
def test_date_is_within_last_three_months(
    fake_today,
    offset_months,
    cutoff_day,
    expected,
):
    with fake_today:
        today = date.today()
        expected_result = None
        if isinstance(expected, bool):
            expected_result = expected
        elif isinstance(expected, str):
            if expected == 'greater or equals':
                expected_result = today.day >= cutoff_day
            elif expected == 'less than':
                expected_result = today.day < cutoff_day

        year, month, days = __offset_year_month_days(today, offset_months)
        for day in days:
            check_date = date(year, month, day)
            result = timezone.date_is_within_last_three_months(
                check_date,
                cutoff_day,
            )

            if result is not expected_result:
                print(check_date)
            assert result is expected_result

@pytest.mark.parametrize(
    ('check_date', 'cutoff_day'),
    [
        (
            '2019-02-01', # string check_date
            GOOD_CUTOFF_DAY,
        ),
        (
            None, # None check_date
            GOOD_CUTOFF_DAY,
        ),
        (
            date(2018, 12, 20),
            None, # None cutoff_day
        ),
        (
            date(2018, 11, 30),
            '15', # string cutoff_day
        ),
        (
            date(2018, 10, 1),
            100, # invalid cutoff_day
        ),
    ],
)
def test_date_is_within_last_three_months_with_bad_inputs(
    check_date,
    cutoff_day,
):
    with pytest.raises(ValueError):
        _ = timezone.date_is_within_last_three_months(
            check_date,
            cutoff_day,
        )

# private

def __offset_year_month_days(reference_date, offset_months):
    current_month = reference_date.month
    current_year = reference_date.year

    offset_month = current_month - offset_months
    offset_year = current_year
    if offset_month < 1:
        offset_month += 12
        offset_year -= 1
    offset_days = range(1, \
        29 if offset_year % 4 == 0 and offset_month == 2 else (\
            28 if offset_year % 4 != 0 and offset_month == 2 else (
                30 if offset_month in (4, 6, 9, 11) else 31
            )
        )
    )

    return (offset_year, offset_month, offset_days)
