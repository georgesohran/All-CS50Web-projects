import random


def main():
    pass


def get_level():
    try:
        lvl = int(input())
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