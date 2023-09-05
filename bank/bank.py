g = input("Greeting: ")
g = g.lower()


if g.find("hello",0,5) != -1:
    print("$0")
elif g.find("h",0,1) != -1:
    print("$20")
else:
    print("$100")