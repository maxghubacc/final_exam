def days_since_birthday(birthday, current_year):
    """
    Calculate the number of days since a birthday.
    :param birthday: birthday in format "DD-MM-YYYY"
    :param current_year: the current year
    :return: number of days
    """

    birth_year = int(birthday[6:])
    current_year = 2026
    years = current_year - birth_year - 1
    days = years * 365

    return days
print(days_since_birthday("01-03-2006", 2026))