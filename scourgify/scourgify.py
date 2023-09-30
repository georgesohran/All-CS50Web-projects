import sys
import csv

def main():
    try:
        check_input()

        before = sys.argv[1]
        after = sys.argv[2]

        with open(before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                seporate(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def check_input():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<=2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file ")

def seporate(row_dict):
    full = row_dict.pop("name")
    row_dict["last"],row_dict["first"] = full.replace(" ","").split(",")
    print(row_dict)



main()