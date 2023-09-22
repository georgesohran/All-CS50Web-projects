import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl >= 0 and lvl <= 100:
            break
        pass
    except ValueError:
        pass

n = random.randint(1,lvl)

while True:
    try:
        value = int(input("Guess:"))
        if value > n:
            print("Too large!")
        elif value < n:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

