#!/usr/bin/env python3

import pytest

from erinnerung import erinnerung


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
                             ([""],       [""]),
                             (["a"],      ["a"]),
                             (["a", "b"], ["a", "b"])
                         ])
def test_eval_equal(test_input, expected):
    assert test_input == expected

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
                             (["a"],      [""]),
                             ([""],       ["a"]),
                             (["a"],      ["b"]),
                             (["a", "a"], ["b", "a"]),
                             (["a", "a"], ["a", "b"]),
                         ])
def test_eval_not_equal(test_input, expected):
    e1 = erinnerung(test_input)
    e2 = erinnerung(expected)

    # two obj instances equal
    assert e1 != e2


def main():
    e = erinnerung(["a", "b"])
    e = erinnerung(["a", "in", "5min"])
    e = erinnerung(["a", "in", "5", "min"])
    e = erinnerung(["a", "in", "5m"])
    e = erinnerung(["a", "in", "5", "m"])


if __name__ == "__main__":
    main()
