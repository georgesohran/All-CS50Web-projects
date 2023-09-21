import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    word = input("Input:")
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        figlet.renderText(word)

    elif len(sys.argv) == 2:
        print("Invalid usage")

    elif len(sys.argv) > 2:
        figlet.setFont(sys.argv[2])

main()