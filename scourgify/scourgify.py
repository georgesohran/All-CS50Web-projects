import sys
import csv


try:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<=2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file ")

    p = sys.argv[1]

    with open(p) as file:
        pizza_type = "Regular Pizza"
        reader = csv.reader(file)

except FileNotFoundError:
    sys.exit("File does not exist")