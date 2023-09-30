import sys
import csv
from tabulate import tabulate


table = []

try:
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<=1:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file ")

    p = sys.argv[1]

    with open(p) as file:
        pizza_type = "Regular Pizza"
        reader = csv.reader(file)
        for row in reader:
            table.append(row)

    print(tabulate(table[1:], table[0], tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")