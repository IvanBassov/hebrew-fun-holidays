# hebrew-year-length.py

from datetime import timedelta
from pyluach import dates, hebrewcal


def hebrew_year_length(year):
    """
    Print the length, classification,
    and Gregorian date range of a given Hebrew year.
    """

    # Start of the Hebrew year (1 Tishrei)
    start = dates.HebrewDate(year, 7, 1)

    # Start of the next Hebrew year (1 Tishrei of the following year)
    next_year = dates.HebrewDate(year + 1, 7, 1)

    # Number of days in this Hebrew year
    days = next_year - start

    # Leap year status
    leap = hebrewcal.Year(year).leap

    # Determine the year type
    if days in (353, 383):
        year_type = "deficient"
    elif days in (354, 384):
        year_type = "regular"
    elif days in (355, 385):
        year_type = "complete"
    else:
        year_type = "unknown"

    name = f"{'leap' if leap else 'common'} {year_type}"

    # Gregorian date range
    start_greg = start.to_greg()
    end_greg = next_year.to_greg().to_pydate() - timedelta(days=1)

    # Print formatted output
    print(
        f"Year {year}: {name} - {days} days "
        f"-> Gregorian: {start_greg:%Y-%m-%d} - {end_greg:%Y-%m-%d}"

    )


# Print Hebrew year length and description for several years
# starting from the current Hebrew year.
current_hebrew_year = dates.HebrewDate.today().year
number_of_years = 5

for y in range(current_hebrew_year, current_hebrew_year + number_of_years):
    hebrew_year_length(y)
