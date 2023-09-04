a = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
a = a.lower().replace("-","").replace(" ","")

match a :
    case "42"|"fortytwo":
        print("Yes")
    case _:
        print("No")