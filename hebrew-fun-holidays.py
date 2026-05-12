# hebrew-fun-holidays.py

from pyluach import dates


def date_from_rosh_hashana(day_number, hebrew_year=None):
    """
    Print the Hebrew and Gregorian date
    for a given day number from Rosh Hashana.
    """

    # Default to the current Hebrew year
    if hebrew_year is None:
        hebrew_year = dates.HebrewDate.today().year

    # Rosh Hashana = 1 Tishrei of that year
    rosh_hashana = dates.HebrewDate(hebrew_year, 7, 1)

    # Compute the target Hebrew date
    target_date = rosh_hashana + (day_number - 1)

    # Convert to Gregorian
    gregorian_date = target_date.to_greg()

    # Print formatted output
    print(
        f"Day {day_number} from Rosh Hashana {hebrew_year}: "
        f"{target_date.day} {target_date.month_name()} {target_date.year} "
        f"-> Gregorian: {gregorian_date:%Y-%m-%d}"
    )


# Print Hebrew fun holidays for several years
# starting from the current Hebrew year.
current_hebrew_year = dates.HebrewDate.today().year
number_of_years = 5

for y in range(current_hebrew_year, current_hebrew_year + number_of_years):
    date_from_rosh_hashana(1, y)    # Rosh Hashana itself
    date_from_rosh_hashana(161, y)  # Canonical Phi Day
    date_from_rosh_hashana(256, y)  # Programmer’s Day
    date_from_rosh_hashana(271, y)  # Canonical e-Day
    date_from_rosh_hashana(314, y)  # Canonical Pi Day
    print()
