def switch(storing_day):
    return {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }[storing_day]


def displaying_day(day, month, year):
    """
    Displaying the day based on the number by using the Gregorian calendar
    the  given inputs are Day,Month and Year
    """
    storing_year = year - (14 - month) / 12
    calculating_year = (storing_year + (storing_year / 4) - (storing_year / 100) + (year / 400))
    storing_month = (month + 12 * ((14 - month) / 12) - 2)
    storing_day = int((day + calculating_year + (31 * storing_month) / 12) % 7)
    print(switch(storing_day))
    return storing_day


if __name__ == '__main__':
    displaying_day(20, 2, 1996)
