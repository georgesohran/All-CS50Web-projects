import random

score = 0

def main():
    lvl = get_level()
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == x + y:
                print(score)
            else:
                print("EEE")




def get_level():
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

if __name__ == "__main__":
    main()