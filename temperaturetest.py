import pytest
import temperatureconversion


def test_of_temperature():
    assert temperatureconversion.conversion(36) == 96


@pytest.mark.parametrize('celsius ,result', [(36, 96),
                                             (35, 95)])
def test_temperature_conversion(celsius, result):
    assert temperatureconversion.conversion(celsius) == 96
