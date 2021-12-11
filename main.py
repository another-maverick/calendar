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
@click.option('-m', '--month', required=False, type=int, help='Enter the calendar month. Format: 1-12')
def print_calendar(year, month):
    """
    main function

    :param year: int
    :param month: int
    """

    assert re.search('^[0-9]\d{3}$', str(year)), 'Year format is incorrect'

    if month:
        assert re.search('(^0?[1-9]$)|(^[1][0-2]$)', str(month)), 'Month format is incorrect'
        print_calendar_month(year, month)
        return
    else:
        print_calendar_year(year)
        return


if __name__ == '__main__':
    print_calendar()
