def main():
    while True:
        try:
            a = input("Fraction: ")
            if convert(a) == None:
                pass
            else:
                a = convert(a)
                if gauge(a) != None:
                    print(gauge(a))
                    break
                else:
                    pass
        e



def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        return int((x / y)*100)
    except (ValueError, ZeroDivisionError):
        return None


def gauge(percentage):
    if percentage > 100 or percentage < 0:
        return None
    elif 0 <= percentage <= 1:
        return "E"
    elif 100 >= percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

