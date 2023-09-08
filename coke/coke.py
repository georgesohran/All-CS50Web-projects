due = 50

while due > 0:
    print("Amount Due:",due)
    incoin = int(input("Insert Coin: "))
    match incoin:
        25:
            due -= incoin
        10:
            due -= incoin
        5:
            due -= incoin
        _:
            continue