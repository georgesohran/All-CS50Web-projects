import sys
import csv


try:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<=2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file ")

    before = sys.argv[1]
    after = sys.argv[2]

    with open(before) as file:
        reader = csv.reader(file)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")