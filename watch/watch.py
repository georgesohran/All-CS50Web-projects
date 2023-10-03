import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    mat = re.search(r'^\<iframe .*src\="(.*)".*$',s)
    if mat:
        return mat.group(1)


def reformat(s):
    if "www" in s:
        pass
    elif "http" in s:
        pass
    elif "https" in s
if __name__ == "__main__":
    main()