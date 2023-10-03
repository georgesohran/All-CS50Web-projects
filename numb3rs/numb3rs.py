import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match1 = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip)
    if match1:
        one,two,three,four = match1.group(1),match1.group(2),match1.group(3),match1.group(4)
        if int(one) > 255 or int(two) > 255 or int(three) > 255 or int(four) > 255:
            return False
        else:
            return True
    return False

if __name__ == "__main__":
    main()