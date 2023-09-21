import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    if len(sys.argv) == 2:
        print(sys.argv)
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3:
        print(sys.argv)
        if sys.argv[1] != '-f' or sys.argv[1] != '--font':
            sys.exit("Invalid usage")

    if len(sys.argv) == 1:
        word = input("Input:")
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)
        print(figlet.renderText(word))

    elif len(sys.argv) > 2:
        word = input("Input:")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(word))


main()