from tkinter import *
from numpy import arange
import math

graph_size = 600

#offset of the coordinate system
x_rel = graph_size/2
y_rel = graph_size/2



def main():
    main_window = Tk()
    main_window.title("math.py")
    main_window.geometry("1200x600")

    canvas = Canvas(main_window, bg="#C0C0C0", height=graph_size, width=graph_size)
    canvas.place(x=0,y=0)

    #points of a graph
    x1 = -100
    y1 = f(x1)

    canvas.create_line(graph_size/2 , 0 , graph_size/2 , graph_size , width=3)
    canvas.create_line(0 , graph_size/2 ,graph_size , graph_size/2, width=3)

    zoom_step = 20
    x_step = 0.05
    for x in arange(-100,100,x_step):
        try:
            y = f(x)
            if not (y1 - y < -50) and not (y1 - y > 50):
                canvas.create_line(
                                    (x1*zoom_step+x_rel),
                                    (y1*zoom_step+y_rel),
                                    (x*zoom_step+x_rel),
                                    (y*zoom_step+y_rel),
                                    width = 2
                                    )
            else:
                pass
            x1,y1 = x , y
        except ZeroDivisionError:
            x1 += 2
            y1 = f(x1)


    main_window.mainloop()



def f(x):
    return -(math.tan(x))





if __name__ == "__main__":
    main()