def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  (last_cer(s)):
        return True
    else:
        return False

def cerecter_count(st):
    cc = 0
    for _ in st:
        cc += 1
    return cc

def first_num(st):
    dc = 0
    for c in st :
        if c.isdigit() and dc == 0:
            dc = 1
            if int(c) == 0 :
                return False
            else:
                return True
def last_cer(st):
    for i in range(9):
        if st.endswith(str(i)):
            return True
        else:
            return False

main()