import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    word = input("Input:")
    if len(sys.argv) == 0:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font)
        print(figlet.renderText(word))
    if len(sys.argv) == 1:
        