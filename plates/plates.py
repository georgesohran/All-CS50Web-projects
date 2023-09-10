def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (2 <=cerecter_count(s)<= 6) and (s[0:2].isalpha()):
        return True
    else:
        return False

def cerecter_count(st):
    cc = 0
    for _ in st:
        cc += 1
    return cc

def a(st):
    dc = 0
    for c in st :
        if c.isdigit() and dc == 0 :
            return False
        else:
            return True

main()