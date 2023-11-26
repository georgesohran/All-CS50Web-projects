import re

def main():

    change = int(get_input() * 100)

    coins = [25,10,5,1]
    count = 0
    idx = 0

    while change > 0:
        a = change - coins[idx]
        if a > 0:
            change = a
            count += 1
        elif a == 0:
            count += 1
            break
        else:
            idx += 1

    print(count)



def get_input():
    while True:
        try:
            return float(input("Change owed: "))
        except ValueError:
            continue

if __name__ == "__main__":
    main()
