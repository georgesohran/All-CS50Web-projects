import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    tfrom , tto = s.split(" to ")
    match1 = re.search(r"([0-9]{1,2})\:?([0-9]{1,2})? (AM?|PM?)",tfrom)
    match2 = re.search(r"([0-9]{1,2})\:?([0-9]{1,2})? (AM?|PM?)",tto)
    if match1 and match2:
        hours1, mins1 = match1.group(1), match1.group(2)
        APM1  = match1.group(3)
        return "success"




if __name__ == "__main__":
    main()