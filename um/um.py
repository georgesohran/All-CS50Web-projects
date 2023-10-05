import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if match1 := re.search(r"(.* (um)* .*)+",s):
        return "matched"



if __name__ == "__main__":
    main()