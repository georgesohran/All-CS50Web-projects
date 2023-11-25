from re import search


def main():
    card_num = input("Number: ")

    if search("^14",card_num)

def is_valid(card_num:str):
    sum1 = 0
    sum2 = 0

    for i in range(len(card_num), step = 2):
        if int(card_num[i])*2 > 9:
            sum1 += (int(card_num[i])*2) % 10
            sum1 += (int(card_num[i])*2) % 100
        else:
            sum1 += int(card_num[i])*2

    for i in range(len(card_num), step = 2, start = 1):
        sum2 += card_num[i]

    sum3 = sum1 + sum2

    return True



if __name__ == "__main__":
    main()
