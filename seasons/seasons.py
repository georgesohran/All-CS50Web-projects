from datetime import timedelta
from datetime import date
import inflect as inf
import re


def main():
    input_date = input("Date of Birth:")
    if match := re.search(r"([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2})",input_date):
        input_date = date()
        input_date.year = match.group(1)
        input_date.month = match.group(2)
        input_date.day = match.group(3)
        current_date = date()
    else:
        print("no")
...


if __name__ == "__main__":
    main()