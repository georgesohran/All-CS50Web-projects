import random

def main():
    score = 0
    lvl = get_level()
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        ask(x,y)
    print(score)

def get_level():
    while True:
        try:
            lvl = int(input("Level:"))
            if 1 <= lvl <= 3 :
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,10)
    if level == 2:
        return random.randint(11,100)
    if level == 3:
        return random.randint(101,1000)

def ask(a,b):
    for _ in range(3):
        try:
            ans = int(input(f"{a} + {b} = "))
            if ans == a + b:
                score += 1
                break
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{a} + {b} = {a+b}")


if __name__ == "__main__":
    main()