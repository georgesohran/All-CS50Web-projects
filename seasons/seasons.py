from datetime import timedelta
from datetime import date
import inflect as inf
import re


def main():
    input_date = input("Date of Birth:")
    if match := re.search(r"([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2})",input_date):
        input_date = date(int(match.group(1)),int(match.group(2)),int(match.group(3)))
        current_date = date.today()
        print(input_date)
    else:
        print("no")
...


if __name__ == "__main__":
    main()