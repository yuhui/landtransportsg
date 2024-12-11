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

"""Standardise all datetime-related timezones to SGT (Singapore Time)."""

from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from typeguard import typechecked

# constants for testing dates as date objects
TWO_MONTHS_AGO_DATE = (date.today() + timedelta(-40))
FOUR_MONTHS_AGO_DATE = (date.today() + timedelta(-100))

@typechecked
def datetime_as_sgt(dt: datetime) -> datetime:
    """Set a datetime with the SGT timezone and return the datetime.

    :param dt: Datetime to convert to SGT timezone.
    :type dt: datetime

    :return: The datetime in SGT timezone.
    :rtype: datetime
    """
    dt_sg: datetime = dt.astimezone(ZoneInfo('Asia/Singapore'))
    return dt_sg

@typechecked
def datetime_from_string(val: str) -> datetime | date:
    """Convert a YYYY-MM-DDTHH:MM:SS string into a datetime and return the \
    datetime.

    :param val: String to convert to a datetime.
    :type val: str

    :raises ValueError: `val` is not a recognised datetime string.

    :return: The value as a datetime or date, if there is no time.
    :rtype: datetime | date
    """
    dt: datetime | date

    # first, try parsing without time
    dt_format = '%Y-%m-%d'

    try:
        dt = datetime.strptime(val, dt_format)
    except ValueError:
        # next, try parsing without timezone
        dt_format = f'{dt_format} %H:%M:%S'
        try:
            dt = datetime.strptime(val, dt_format)
        except ValueError:
            # last, try parsing with timezone
            dt_format = f'{dt_format}%z'
            try:
                dt = datetime.strptime(val, dt_format)
            except ValueError as e:
                # still getting an error, so this isn't a datetime string
                raise ValueError('val is not a datetime string') from e

    dt = datetime_as_sgt(dt)

    if dt_format == '%Y-%m-%d':
        # the original string was just the date, so return a date object only
        dt = dt.date()

    return dt

@typechecked
def date_is_within_last_three_months(
    check_date: date,
    cutoff_day: int=15,
) -> bool:
    """Return whether the specified date is within the last 3 months of today.

    :param check_date: Date to check if it is within the last 3 months of \
        today.
    :type check_date: date

    :param cutoff_day: The day of the month when a "new month" begins. \
        Example: if `cutoff_day` is `15`, then if today is between 1st and \
        14th September, then last 3 months is between May-July, else if today \
        is between 15th and 30th September, then last 3 months is between \
        June-August. Defaults to 15, i.e. the new month starts on the 15th day.
    :type cutoff_day: int

    :raises ValueError: `cutoff day` is not a valid calendar day.

    :returns: `True` if the specified date is within the last 3 months of
        today.
    :rtype: bool
    """
    # raise a ValueError if cutoff_day is not a valid calendar day
    try:
        _ = date(2019, 1, cutoff_day)
    except ValueError as e:
        raise e

    result: bool

    today = date.today()
    today_year = today.year
    today_month = today.month
    today_day = today.day

    # assume that today is on or after the cutoff day
    three_months_ago_year = today_year
    three_months_ago_month = today_month - 3
    if today_day < cutoff_day:
        # today is before the cutoff day, get one more earlier month
        three_months_ago_month -= 1
    if three_months_ago_month < 1:
        # adjust year and month to the previous year
        three_months_ago_month += 12
        three_months_ago_year -= 1

    three_months_ago_day = 1 # first day of the month

    three_months_ago_date = date(
        three_months_ago_year,
        three_months_ago_month,
        three_months_ago_day,
    )

    one_month_ago_year = three_months_ago_year
    one_month_ago_month = three_months_ago_month + 2
    if one_month_ago_month > 12:
        # adjust year and month to the next (i.e. current) year
        one_month_ago_month -= 12
        one_month_ago_year += 1

    one_month_ago_day = 31 # last day of the month
    if one_month_ago_month == 2:
        one_month_ago_day = 29 if one_month_ago_year % 4 == 0 else 28
    elif one_month_ago_month in [4, 6, 9, 11]:
        one_month_ago_day = 30

    one_month_ago_date = date(
        one_month_ago_year,
        one_month_ago_month,
        one_month_ago_day,
    )

    check_date_more_than_three_months_ago = check_date \
        >= three_months_ago_date
    check_date_less_than_one_month_ago = check_date \
        <= one_month_ago_date

    result = check_date_more_than_three_months_ago and \
        check_date_less_than_one_month_ago

    return result

__all__ = [
    'datetime_from_string',
    'date_is_within_last_three_months',
]
