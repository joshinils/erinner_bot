#!/usr/bin/env python3

from erinnerung import erinnerung

import pytest


def test_0():
    e = erinnerung()
    assert e == e


def test_1():
    e1 = erinnerung()
    e2 = erinnerung()
    assert e1 == e2


def test_2():
    e1 = erinnerung()
    e2 = e1
    assert e1 == e2


def test_3():
    # try:
    #     e = erinnerung("a")
    # except Exception as ex:
    #     print(type(ex))
    #     print(ex)
    with pytest.raises(AssertionError):
        e = erinnerung("a")


def test_4():
    e = erinnerung(["a"])
    assert erinnerung(["a"]) == e


def test_5():
    e = erinnerung()
    e.text = "a"
    assert erinnerung(["a"]) == e


def test_6():
    e = erinnerung()
    e.text = "b"
    assert erinnerung(["a"]) != e

def test_7():
    e = erinnerung(["a"])
    assert e == e

def test_7_1():
    e1 = erinnerung(["a"])
    e2 = e1
    assert e1 == e2

def test_8():
    e1 = erinnerung(["a"])
    e2 = erinnerung(["a"])
    assert e1 == e2

def test_10():
    e1 = erinnerung(["a", "b"])
    e2 = erinnerung(["a", "b"])
    assert e1 == e2

def test_11():
    e1 = erinnerung(["a", "b"])
    e2 = erinnerung(["a", "c"])
    assert e1 != e2


def main():
    e = erinnerung(["a", "b"])
    e = erinnerung(["a", "in", "5min"])
    e = erinnerung(["a", "in", "5", "min"])
    e = erinnerung(["a", "in", "5m"])
    e = erinnerung(["a", "in", "5", "m"])


if __name__ == "__main__":
    test_3()
    main()
