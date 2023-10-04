import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    mat = re.search(r"^\<iframe .*?src\=\"(.*?)\".*\<\/iframe\>$",s)
    if mat:
        r = reformat(mat.group(1))
        return r

def reformat(s):
    if s.find("youtube")!=-1:
        _,_,_,_,catch = s.split("/")
        return "https://youtu.be/"+catch


if __name__ == "__main__":
    main()