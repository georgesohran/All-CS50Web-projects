a = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

match a :
    case "42"|"Forty Two"|"forty-two"|"forty two"|"Forty two":
        print("Yes")
    case _:
        print("No")