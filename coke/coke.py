due = 50

while True:
    print("Amount Due:",due)
    incoin = int(input("Insert Coin: "))
    match incoin:
        case 25:
            due -= incoin
        case 10:
            due -= incoin
        case 5:
            due -= incoin
        case _:
            continue
    