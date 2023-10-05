import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    c = 0
    if match1 := re.search(r".*\bum\b.*+",s):
        words = re.split(r"\s",s)
        for word in words:
            if word == "um":
                count+=1
    return c



if __name__ == "__main__":
    main()