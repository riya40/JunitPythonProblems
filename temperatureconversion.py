import pytest
"""
displaying the temperature in given celsius or fahrenheit
"""


def conversion(celsius):
    fahrenheit_value = int((celsius * (9 / 5)) + 32)
    return fahrenheit_value


def test():
    assert conversion(36) == 96
