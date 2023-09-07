def main():
    t = input("What time is it? ")
    t = convert(t)
    if 7.00 <= t <= 8.00 :
        print("breakfast time")
    if 12.00 <= t <= 13.00 :
        print("lunch time")
    if 18.00 <= t <= 19.00 :
        print("dinner time")


def convert(time):
    if time.endswith("p.m."):
        time.replace("p.m.","")
        hour,min = time.split(":")
        hour = float(hour+12)
        min = float(min)
    if time.endswith("a.m."):
        time.replace("a.m.","")
        hour,min = time.split(":")
        hour = float(hour)
        min = float(min)
    min10 = ((min*100)/60)*0.01
    return hour + min10


if __name__ == "__main__":
    main()