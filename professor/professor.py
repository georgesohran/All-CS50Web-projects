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
    pass


if __name__ == "__main__":
    main()
    for i in range(3):
        print(i)