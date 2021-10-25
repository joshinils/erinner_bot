#!/usr/bin/env python3

from py import test
import pytest

from erinnerung import erinnerung
from debug_print import *

import datetime
from datetime import date, timedelta


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
