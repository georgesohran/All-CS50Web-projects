def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (2 <=cerecter_count(s)<= 6) and (s[0:2].isalpha()) and (first_num(s)) and (last_cer(s)):
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
        else:
            return True
def last_cer(st):
    for i in range(9):
        if st.find(str(i)) != -1 :
            if st.endswith(str(i)):
                return True
            else:
                return False
        else:
            return True
def symbols(st):
    for c in st:
        if c :
            return False
        else:
            return True

main()