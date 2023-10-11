from tkinter import *
from tkinter import ttk

class Cords(Canvas):
    def __init__(self):
        pass




def main():
    main_window = Tk()
    main_window.title("math.py")
    main_window.geometry("1200x600")
    canvas = Canvas(main_window, bg="#C0C0C0", height=600, width=600)
    canvas.pack(anchor=W)
    canvas.create_line(15, 25, 200, 25)
    canvas.create_line(15, 25, 40, 25)
    main_window.mainloop()

def generate(func):
    for x in range(-50,50):
        pass


if __name__ == "__main__":
    main()
