def calculating_payment(principle, rate_of_interest, years):
    """
    Calculating the Monthly payment by given inputs are principle,rate of interest,years
    """
    n = 12 * years
    r = rate_of_interest / (12 * 100)
    payment = (principle * r) / (1 - (1 + r) ** (-n))
    return payment


def test():
    assert calculating_payment(6000, 1, 2) == 252.61248201268052


if __name__ == '__main__':
    calculating_payment(5000, 1, 2)
    