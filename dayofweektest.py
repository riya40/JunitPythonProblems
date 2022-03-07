import pytest
import dayofweek


def test_of_day():
    """checking the expectes result matched or not"""
    assert dayofweek.displaying_day(20, 2, 1996) == 2


def day_test():
    """In This Values That Only Give Two Parameters"""
    assert dayofweek.displaying_day(20, 1) == 2


@pytest.mark.parametrize('day, month, year,result', [(20, 2, 1996, 2),
                                                     (1, 3, 2022, 2),
                                                     (20, 2, 1996, 3)])
def test_day_of_week(day, month, year, result):
    """In this we give the Different Parameters that are for expecting Different Test """
    assert dayofweek.displaying_day(day, month, year) == 2
