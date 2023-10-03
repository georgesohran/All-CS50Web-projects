import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    mat = re.search(r"^<iframe .*",s)


...


if __name__ == "__main__":
    main()