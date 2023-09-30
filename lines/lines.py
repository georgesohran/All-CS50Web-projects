import sys

try:
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<1:
        sys.exit("Too few command-line arguments")

    f = sys.argv[1]
    with open(f) as File:
        lines = File.readlines()
        

except FileNotFoundError:
    sys.exit("File does not exist")