#!/usr/bin/env python3

from py import test
import pytest

from erinnerung import erinnerung
from debug_print import *

import datetime
from datetime import date, timedelta
import itertools
import typing 

def get_arg_list(arg: int) -> typing.List[str]:
    # return [str(arg)]  # debug
    arg_str = str(arg)
    arg_str_list = list(set([arg_str, arg_str.zfill(2)]))
    arg_str_list.sort(reverse=True)
    return arg_str_list


def test_string_list(weeks=0, days=0, hours=0, minutes=0, seconds=0):
    separator = [":", ",", ";", "."]
    # separator = [":"]  # debug
    space = ["", " "]
    # space = [""]  # debug
    separator = [''.join(i) for i in itertools.product(space, separator, space)]

    # print(weeks, days, hours, minutes, seconds) # debug
    ret = [""]

    if (weeks == 0):
        arg_weeks = None
    else:
        arg_weeks = get_arg_list(weeks)
        if days == 0 and hours == 0 and minutes == 0 and seconds == 0:
            week_name = ["w", "woche", "wochen", "week", "weeks"]
            # week_name = ["w"]  # debug
            ret = [''.join(i) for i in itertools.product(arg_weeks, space, week_name)]
        else:
            ret = [''.join(i) for i in itertools.product(arg_weeks, separator)]

    # rest is 0, return early
    if (days == 0 and hours == 0 and minutes == 0 and seconds == 0):
        return ret

    if (days == 0 and weeks == 0):
        arg_days = None
    else:
        arg_days = get_arg_list(days)
        if hours == 0 and minutes == 0 and seconds == 0:
            day_name = ["d", "day", "days", "t", "tag", "tage"]
            # day_name = ["d"]  # debug
            arg_days = [''.join(i) for i in itertools.product(arg_days, space, day_name)]
            ret = [''.join(i) for i in itertools.product(ret, arg_days)]
        else:
            ret = [''.join(i) for i in itertools.product(ret, arg_days, separator)]

    # rest is 0, return early
    if (hours == 0 and minutes == 0 and seconds == 0):
        return ret

    if (hours == 0 and days == 0 and weeks == 0):
        arg_hours = None
    else:
        arg_hours = get_arg_list(hours)
        if minutes == 0 and seconds == 0:
            hour_name = ["h", "hour", "hours", "stunde", "stunden"]
            # hour_name = ["h"]  # debug
            arg_hours = [''.join(i) for i in itertools.product(arg_hours, space, hour_name)]
            ret = [''.join(i) for i in itertools.product(ret, arg_hours)]
        else:
            ret = [''.join(i) for i in itertools.product(ret, arg_hours, separator)]

    # rest is 0, return early
    if (minutes == 0 and seconds == 0):
        return ret

    if (minutes == 0 and hours == 0 and days == 0 and weeks == 0):
        arg_minutes = None
    else:
        arg_minutes = get_arg_list(minutes)
        if seconds == 0:
            minute_name = ["m", "minute", "minutes", "minuten"]
            # minute_name = ["m"]  # debug
            arg_minutes = [''.join(i) for i in itertools.product(arg_minutes, space, minute_name)]
            ret = [''.join(i) for i in itertools.product(ret, arg_minutes)]
        else:
            ret = [''.join(i) for i in itertools.product(ret, arg_minutes, separator)]

    # rest is 0, return early
    if (seconds == 0):
        return ret

    if (seconds == 0 and hours == 0 and hours == 0 and days == 0 and weeks == 0):
        arg_seconds = None
    else:
        arg_seconds = get_arg_list(seconds)

        second_name = ["s", "sec", "sek", "second", "seconds", "sekunden"]
        # second_name = ["s"]  # debug
        arg_seconds = [''.join(i) for i in itertools.product(arg_seconds, space, second_name)]
        ret = [''.join(i) for i in itertools.product(ret, arg_seconds)]

    return ret

def split_list(l: list) -> list:
    new_l = []
    for e in l:
        if len(e) < 3:
            new_l.append(e)
        else:
            new_l += e.split()
    return new_l


# test the parts of the tests itself too!
# how meta!
@pytest.mark.parametrize("test_input,expected",
                         [
                             ([""],       [""]),
                             (["a"],      ["a"]),
                             (["a b"],    ["a", "b"]),
                             (["a", "b"], ["a", "b"]),
                         ])
def test_split_list(test_input, expected):
    split_input = split_list(test_input)
    assert split_input == expected
    assert type(test_input) == type(expected)
    assert type(split_input) == type(expected)


def test_3():
    # try:
    #     e = erinnerung("a")
    # except Exception as ex:
    #     print(type(ex))
    #     print(ex)
    with pytest.raises(AssertionError):
        e = erinnerung("a")
    with pytest.raises(AssertionError):
        e = erinnerung(1)
    with pytest.raises(AssertionError):
        e = erinnerung([])


@pytest.mark.parametrize("test_input,expected",
                         [
                             ([""],    [""]),
                             (["a"],   ["a"]),
                             (["a b"], ["a b"])
                         ])
def test_eval_equal(test_input, expected):
    test_input = split_list(test_input)
    expected = split_list(expected)

    e1 = erinnerung(test_input)
    e2 = erinnerung(test_input)

    # two obj instances equal
    assert e1 == e2

    # equal itself
    assert e1 == e1

    # equal to copy of itself
    e_copy = e1
    assert e1 == e_copy


@pytest.mark.parametrize("test_input,expected",
                         [
                             (["a"],    [""]),
                             ([""],     ["a"]),
                             (["a"],    ["b"]),
                             (["a a"], ["b a"]),
                             (["a a"], ["a b"]),
                         ])
def test_eval_not_equal(test_input, expected):
    test_input = split_list(test_input)
    expected = split_list(expected)

    e1 = erinnerung(test_input)
    e2 = erinnerung(expected)

    # two obj instances equal
    assert e1 != e2


@pytest.mark.parametrize("test_input",
                         [
                             (["a in 5"]),
                             (["a in 5m"]),
                             (["a in 5 m"]),
                             (["a in 5min"]),
                             (["a in 5 min"]),
                             (["a in 5:0"]),
                             (["a in 5:0m"]),
                             (["a in 5:0 m"]),
                             (["a in 5:0min"]),
                             (["a in 5:00 min"]),
                             (["a in 5:00"]),
                             (["a in 5:00m"]),
                             (["a in 5:00 m"]),
                             (["a in 5:00min"]),
                             (["a in 5:00 min"]),
                             (["a in 5.0"]),
                             (["a in 5.0m"]),
                             (["a in 5.0 m"]),
                             (["a in 5.0min"]),
                             (["a in 5.0 min"]),
                             (["a in 5,0"]),
                             (["a in 5,0m"]),
                             (["a in 5,0 m"]),
                             (["a in 5,0min"]),
                             (["a in 5,0 min"]),
                         ])
def test_in_5_min(test_input):
    test_input = split_list(test_input)

    e1 = erinnerung(test_input)

    now = datetime.datetime.now()
    now_plus_5 = now + timedelta(minutes=5)

    seconds_error = (e1.date_due - now_plus_5).total_seconds()
    assert abs(seconds_error) < 1


@pytest.mark.parametrize("test_input",
                         [
                             (["a in 10"]),
                             (["a in 10m"]),
                             (["a in 10 m"]),
                             (["a in 10min"]),
                             (["a in 10 min"]),
                         ])
def test_in_10_min(test_input):
    test_input = split_list(test_input)

    e1 = erinnerung(test_input)

    now = datetime.datetime.now()
    now_plus_10 = now + timedelta(minutes=10)

    seconds_error = (e1.date_due - now_plus_10).total_seconds()
    assert abs(seconds_error) < 1


def main():
    e = erinnerung(["a", "b"])
    e = erinnerung(["a", "in", "5min"])
    e = erinnerung(["a", "in", "5", "min"])
    e = erinnerung(["a", "in", "5m"])
    e = erinnerung(["a", "in", "5", "m"])


if __name__ == "__main__":
    main()
