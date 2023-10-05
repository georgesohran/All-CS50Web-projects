import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    c = 0
    if match1 := re.search(r".*\bum\b.*+",s):
        words = re.split(r"\s",s)
        return words




if __name__ == "__main__":
    main()