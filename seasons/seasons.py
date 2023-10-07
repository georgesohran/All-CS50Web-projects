from datetime import timedelta
from datetime import date
import inflect as inf
p = inf.engine()
import re


def main():
    input_date = input("Date of Birth:")
    try:
        if match := re.search(r"([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2})",input_date):
            input_date = date(int(match.group(1)),int(match.group(2)),int(match.group(3)))
            current_date = date.today()
            time_passed_date = current_date - input_date
            total_mins = time_passed_date.total_seconds()/60
            word = p.number_to_words(int(total_mins), andword="")
            print(word,"minutes")
        else:
            print("Invalid date")
    except ValueError:
        print("Invalid date")

def convert_date(d):
    try:
        if match := re.search(r"([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2})",input_date):
            input_date = date(int(match.group(1)),int(match.group(2)),int(match.group(3)))
            current_date = date.today()
            time_passed_date = current_date - input_date
            total_mins = time_passed_date.total_seconds()/60
            word = p.number_to_words(int(total_mins), andword="")
            print(word,"minutes")
        else:
            print("Invalid date")
    except ValueError:
        print("Invalid date")



if __name__ == "__main__":
    main()