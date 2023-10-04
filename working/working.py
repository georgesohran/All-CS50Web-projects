import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match1 = re.search(r"([0-9]{1-2})\:([0-9]{1-2})? to ([0-9]{1-2})\:([0-9]{1-2})?")


...


if __name__ == "__main__":
    main()