import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match1 = re.search(r"^([0-9])3")


if __name__ == "__main__":
    main()