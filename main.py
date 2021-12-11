#!/usr/bin/env python

import calendar
import click
import re


def print_calendar_year(year):
    """
    prints the calendar of the year that is passed.

    :param year: int
    :return: None
    """
    sep = calendar.TextCalendar(calendar.SUNDAY)
    sep.pryear(year)


def print_calendar_month(year, month):
    """
    prints the calendar of the year and month that is passed.
    :param year: int
    :param month: int
    :return: None
    """

    sep = calendar.TextCalendar(calendar.SUNDAY)
    sep.prmonth(year, month)


@click.command()
@click.option('-y', '--year', required=True, type=int, help='Enter the calendar year')
@click.option('-m', '--month', required=False, help='Enter the calendar month. '
                                                    'Format: 1-12; Jan-Dec, January-December')
def print_calendar(year, month):
    """
    main function

    :param year: int
    :param month: int or str
    """

    assert re.search('^[0-9]\d{3}$', str(year)), 'Year format is incorrect'

    if month:
        assert re.search('(^0?[1-9]$)|(^[1][0-2]$)|'
                         '(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|'
                         'Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|'
                         'Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)', str(month), re.IGNORECASE), \
            'Month format is incorrect'

        if len(month) <= 2:
            print_calendar_month(year, int(month))
        else:
            month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
                         'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
                         'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
            month_abbr = month.lower()[0:3]
            print_calendar_month(year, month_map[month_abbr])
        return
    else:
        print_calendar_year(year)
        return


if __name__ == '__main__':
    print_calendar()
