import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    word = input("Input:")
    if len(sys.argv) == 0:
        font = random.shuffle
        print(figlet.renderText(word))