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
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    return int((x / y)*100)


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

