import vendingmachine1
import pytest


def test_of_vending_machine():
    """Testing the Value as expects is Resultant """
    assert vendingmachine1.change_conversion(1000) == 500 * 2


def test_vending_machine():
    """Testing The resultant without giving value """
    assert vendingmachine1.change_conversion() == 500 * 2


@pytest.mark.parametrize('change,result', [(1000, 500 * 2,),
                                           (500, 500), (2000, 500 * 4)])
def test_vending_machine(change, result):
    """Testing With different types of parameters"""
    assert vendingmachine1.change_conversion(change) == 500 * 2
