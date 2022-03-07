import tobinary
import pytest


def test_to_binary():
    """Testing the given values"""
    assert tobinary.decimal_to_binary(11) == [1, 1, 1, 0]


@pytest.mark.parametrize('number ,result', [(10, [1, 1, 1, 0]), (10, [1, 1]), (11, [1, 1, 1, 0])])
def test_day_of_week(number, result):
    """Testing With different types of parameters"""
    assert tobinary.decimal_to_binary(number, result) == [1, 1, 1, 0]
