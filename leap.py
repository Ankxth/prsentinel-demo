"""Work out whether a year is a leap year (Gregorian calendar rules)."""


def is_leap_year(year):
    """Return True if the year has 366 days."""
    return year % 4 == 0 and year % 100 != 0