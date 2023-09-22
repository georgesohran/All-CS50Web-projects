import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
        p.join(names)
    except EOFError:
        print()
        break