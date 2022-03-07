import pytest
import monthlypayment


def test_payment():
    """Here the test that checks the value that be Expected is Result or Not """
    assert monthlypayment.calculating_payment(6000, 1, 2) == 252.61248201268052


@pytest.mark.parametrize('principle, rate_of_interest, years, result', [(6000, 1, 2, 252.61248201268052),
                                                                        (20000, 2, 2, 850.8052673695847)])
def test_day_of_week(principle, rate_of_interest, years, result):
    """in this we give the values in the parameters
    in First and Second Parameters that Checks the Value that as Expected """
    assert monthlypayment.calculating_payment(principle, rate_of_interest, years) == 252.61248201268052
