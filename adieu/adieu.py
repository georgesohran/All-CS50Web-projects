import

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break