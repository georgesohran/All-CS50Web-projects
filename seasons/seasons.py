from datetime import date
import inflect as inf
p = inf.engine()
import re


def main():
    input_date = input("Date of Birth:")
    print(convert_date(input_date,get_current_date()))

def convert_date(d,curd):
    try:
        if match := re.search(r"([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2})",d):
            d = date(int(match.group(1)),int(match.group(2)),int(match.group(3)))
            time_passed_date = curd - d
            total_mins = time_passed_date.total_seconds()/60
            word = p.number_to_words(int(total_mins), andword="")
            return word.capitalize()+" minutes"
        else:
            return "Invalid date"
    except ValueError:
        return "Invalid date"


def get_current_date():
    return date.today()

if __name__ == "__main__":
    main()