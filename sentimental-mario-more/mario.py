def main():
    height = -48
    while height <= 0 and height > 8:
        try:
            height = int(input("Height: "))
        except ValueError:
            pass

    for i in range(height):
        print_row(i+1,height)



def print_row(i,h):
    print(" " * (h-i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)


if __name__ == "__main__":
    main()
