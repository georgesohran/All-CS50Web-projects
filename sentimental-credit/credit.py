from re import search


def main():
    card_num = input("Number: ")

    digit_num = len(card_num)

    if search(r"^4[0-9]*",card_num) and digit_num == 16:
        if is_valid(card_num):
            print("VISA")
        else:
            print("INVALID")

    elif search(r"^5[0-9]*",card_num) and digit_num == 15:
        if is_valid(card_num):
            print("MASTERCARD")
        else:
            print("INVALID")

    elif search(r"^3[0-9]*",card_num) and digit_num == 15:
        if is_valid(card_num):
            print("AMEX")
        else:
            print("INVALID")
    else:
        print("INVALID")

def is_valid(card_num:str):
    sum1 = 0
    sum2 = 0

    for i in range(0,len(card_num),2):
        num = int(card_num[i])*2
        if num > 9:
            sum1 += num % 10
            sum1 += num % 100
        else:
            sum1 += num

    for i in range(1,len(card_num),2):
        sum2 += int(card_num[i])

    sum3 = sum1 + sum2

    if sum3 % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
