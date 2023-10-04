import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    tfrom , tto = s.split(" to ")
    match1 = re.search(r"([0-9]{1,2})\:?([0-9]{1,2})? (AM?|PM?)",tfrom)
    match2 = re.search(r"([0-9]{1,2})\:?([0-9]{1,2})? (AM?|PM?)",tto)
    if match1 and match2:
        hours1, mins1 = int(match1.group(1)), int(match1.group(2))
        APM1  = match1.group(3)
        hours2, mins2 = int(match2.group(1)), int(match2.group(2))
        APM2  = match2.group(3)
        if APM1 == "PM":
            hours1 += 12
        if APM2 == "PM":
            hours2 += 12
        return




if __name__ == "__main__":
    main()