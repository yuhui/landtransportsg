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

"""Standardise all datetime-related timezones to SGT (Singapore Time)."""

from datetime import date, datetime, timedelta, tzinfo
from pytz import timezone as pytimezone

# constants for testing dates as date objects
TWO_MONTHS_AGO_DATE = (date.today() + timedelta(-40))
FOUR_MONTHS_AGO_DATE = (date.today() + timedelta(-100))

def datetime_as_sgt(dt):
    """Set a datetime with the SGT timezone and return the datetime.

    Raises:
        ValueError:
            Raised if `dt` is not of datetime class.
    """
    if not isinstance(dt, datetime):
        raise ValueError('dt is not a datetime object.')

    return dt.astimezone(pytimezone('Asia/Singapore'))

def datetime_from_string(val):
    """Convert a YYYY-MM-DDTHH:MM:SS string into a datetime
    and return the datetime.

    Raises:
        ValueError:
            Raised if `val` is not in a valid datetime format.
    """
    # first, try parsing without time
    dt_format = '%Y-%m-%d'
    try:
        dt = datetime.strptime(val, dt_format)
    except:
        # next, try parsing without timezone
        dt_format = '{} %H:%M:%S'.format(dt_format)
        try:
            dt = datetime.strptime(val, dt_format)
        except:
            # last, try parsing with timezone
            dt_format = '{}%z'.format(dt_format)
            dt = datetime.strptime(val, dt_format)
    # if still getting an error, then this isn't a datetime string

    dt = datetime_as_sgt(dt)

    if dt_format is '%Y-%m-%d':
        # the original string was just the date, so return a date object only
        dt = dt.date()

    return dt

def date_is_within_last_three_months(
    check_date,
    cutoff_day=15,
):
    """Return whether the specified date is within the last 3 months of today.

    Arguments:
        check_date (date):
            Date to check if it is within the last 3 months of today.
        cutoff_day (int):
            (optional) The day of the month when a "new month" begins.
            Example: if `cutoff_day` is `15`, then:
                - if today is between 1st and 14th September,
                then last 3 months is between May-July.
                - if today is between 15th and 30th September,
                then last 3 months is between June-August.
            Default: 15, i.e. the new month starts on the 15th day.

    Returns:
        (boolean) True if the specified date is within the last 3 months of
        today.

    Raises:
        ValueError:
            Raised if the check date is not a date object.
            Raised if the cutoff day is not an integer.
            Raised if the cutoff day is not a valid calendar day.
    """
    if not isinstance(check_date, date):
        raise ValueError('check_date is not a date object.')

    if not isinstance(cutoff_day, int):
        raise ValueError('cutoff_day is not an integer.')
    # this will raise a ValueError if cutoff_day is not a valid calendar day.
    try:
        _ = date(2019, 1, cutoff_day)
    except ValueError as e:
        raise e

    today = date.today()
    today_year = today.year
    today_month = today.month
    today_day = today.day

    three_months_ago_year = today_year
    # assume that today is on or after the cutoff day
    three_months_ago_month = today_month - 3
    if today_day < cutoff_day:
        # today is before the cutoff day, get one more earlier month
        three_months_ago_month -= 1
    if three_months_ago_month < 1:
        # adjust year and month to the previous year
        three_months_ago_month += 12
        three_months_ago_year -= 1

    one_month_ago_year = three_months_ago_year
    one_month_ago_month = three_months_ago_month + 2
    if one_month_ago_month > 12:
        # adjust year and month to the next (i.e. current) year
        one_month_ago_month -= 12
        one_month_ago_year += 1

    three_months_ago_day = 1 # first day of the month
    three_months_ago_date = date(
        three_months_ago_year,
        three_months_ago_month,
        three_months_ago_day,
    )
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

    result = check_date >= three_months_ago_date and \
        check_date <= one_month_ago_date
    return result
