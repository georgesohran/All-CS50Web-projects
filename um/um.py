import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if match1 := re.search(r".*\bum\b.*+",s):
        matches = re.split(r"")



if __name__ == "__main__":
    main()