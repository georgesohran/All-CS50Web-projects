import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    mat = re.search(r'^\<iframe .*src\=\"|\'(.*)\"|\'.*$',s)
    if mat:
        mat = reformat(mat.group(1))
        return mat


def reformat(s):
    m = re.search(r'^.*://.*/.*/(.*)$',s)
    if m and s.find("youtube") != -1:
        return "https://youtu.be/" + m.group(1)



if __name__ == "__main__":
    main()