import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        word = input("Input:")
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)
        print(figlet.renderText(word))

    elif len(sys.argv) == 2:
        print("Invalid usage")

    elif len(sys.argv) > 2:
        word = input("Input:")
        figlet.setFont(sys.argv[2])

main()