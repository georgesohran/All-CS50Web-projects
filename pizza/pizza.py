import sys
import csv
from tabulate import tabulate

count = 0

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
            print(row)

#    print(tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")