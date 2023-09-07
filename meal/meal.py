def main():
    t = input("What time is it?")


def convert(time):
    hour,min = time.split(":")
    hour = float(hour)
    min = float(min)
    min10 = (min*100)/60


if __name__ == "__main__":
    main()