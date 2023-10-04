import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match1 := re.search(r"([0-9]{1,2})\:?([0-9]{1,2})? (AM)|(PM)",s ):
        return match1.group(1)

...


if __name__ == "__main__":
    main()