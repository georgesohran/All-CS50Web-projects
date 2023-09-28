def main():
    while True:
        try:
            a = input("Fraction: ")
            a = convert(a)
            print(gauge(a))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    result = int((x / y)*100)
    if x > y or result > 100 or result < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    else:
        return result


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 100 >= percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

