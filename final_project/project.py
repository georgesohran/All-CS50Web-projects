from tkinter import *
from tkinter import ttk

import sys
import csv


def main():
    main_window = Tk()
    main_window.title("math.py")
    main_window.geometry("1200x600")
    canvas = Canvas(main_window, bg="blue", height=600, width=600)
    canvas.create_line(15, 25, 200, 25)
    mainloop()


if __name__ == "__main__":
    main()
