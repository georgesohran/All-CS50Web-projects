def main():
    while True:
        a = input("Fraction: ")
        try:
            x, y = a.split("/")
            x = int(x)
            y = int(y)
            out = x / y
            if out < 0 or out > 1:
                pass
            elif 0 <= out <= 0.01:
                print("E")
                break
            elif 1 >= out >= 0.99:
                print("F")
                break
            else:
                out = round(out,2)
                print(f"{int(out*100)}%")
                break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

