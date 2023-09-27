
def main():
    g = input("Greeting: ")
    g = g.replace(" ","")
    print(f"${value(g)}")



def value(greeting):
    if greeting.lower().find("hello",0,5) != -1:
        return 0
    elif greeting.lower().find("h",0,1) != -1:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


