import re

def main():

    change = get_input()

    


def get_input():
    while True:
        try:
            return float(input("Change owed: "))
        except ValueError:
            continue

if __name__ == "__main__":
    main()
