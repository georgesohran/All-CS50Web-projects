import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    mat = re.search(r'^\<iframe .*src\="(.*)".*$',s)
    if mat:
        return mat.group(1)


def reformat(s):
    m = re.search(r'^.*://.*/.*/(.*)$',s)
    if m and s.has("youtube")



if __name__ == "__main__":
    main()