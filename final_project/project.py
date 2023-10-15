from tkinter import *
from numpy import arange
import re
import math

graph_size = 600

#offset of the coordinate system
x_off = graph_size/2
y_off = graph_size/2

zoom_step = 20

formula = "x**x"
def_range_min = -100
def_range_max = 100

def main():
    main_window = Tk()
    main_window.title("math.py")
    main_window.geometry("1200x600")

    canvas = Canvas(main_window, bg="#C0C0C0", height=graph_size, width=graph_size)
    canvas.place(x=0,y=0)

    canvas.create_line(graph_size/2 , 0 , graph_size/2 , graph_size , width=3)
    canvas.create_line(0 , graph_size/2 ,graph_size , graph_size/2, width=3)

    label = Label(main_window, width=3,height=1 , fg="black" , text="y =" , font=("Arial Bold", 24))
    label.place(x=graph_size+10,y=70)
    form_ent = Entry(main_window, font =("Arial Bold",24))
    form_ent.place(x=graph_size+80,y=70)

    label = Label(main_window , fg="black" , text="zoom in" , font=("Arial Bold", 24))
    label.place(x=graph_size+10,y=140)
    z_ent = Entry(main_window, font =("Arial Bold",24))
    z_ent.place(x=graph_size+140,y=140)
    z_ent.insert(0,"10")

    gen_btn = Button(main_window, text="generate" , font=("Arial Bold", 18),command=lambda: create_graph(canvas,form_ent,z_ent))
    gen_btn.place(x=graph_size+10,y=10)

    main_window.mainloop()

def f(x):
    return -eval(formula)


def create_graph(c,ent,ent_z):
    c.delete("all")

    new_formula = ent.get()
    new_formula = restructure_formula(new_formula)
    set_formula(new_formula)

    new_zoom = int(ent_z.get())
    set_zoom(new_zoom)

    x1 = def_range_of(formula)[0]
    y1 = f(x1)

    c.create_line(graph_size/2 , 0 , graph_size/2 , graph_size , width=3)
    c.create_line(0 , graph_size/2 ,graph_size , graph_size/2, width=3)

    c.create_rectangle(x_off-6,(y_off-1)-zoom_step,x_off+6,(y_off+1)-zoom_step,fill='black')
    c.create_rectangle((x_off-1)+zoom_step,y_off-6,(x_off+1)+zoom_step,y_off+6,fill='black')

    x_step = 0.05

    for x in arange(def_range_of(formula)[0],def_range_of(formula)[-1],x_step):
        y = f(x)

        if not (y1 - y < -70) and not (y1 - y > 70):
            c.create_line(
                            (x1*zoom_step+x_off),
                            (y1*zoom_step+y_off),
                            (x*zoom_step+x_off),
                            (y*zoom_step+y_off),
                            width = 2
                                )

        x1,y1 = x , y




def set_formula(new_formula):
    global formula
    formula = new_formula

def set_zoom(value):
    global zoom_step
    zoom_step = value


def restructure_formula(form:str):
    form = form.replace(" ","")
    form = form.replace(",",".")
    form = form.replace("cos","math.cos").replace("sin","math.sin").replace("tg","math.tan")
    form = form.replace("mod","abs")
    form = form.replace("^","**").replace("sqrt","math.sqrt").replace("log","math.log")
    return form

def def_range_of(form:str):
    range_of_values = []

    if match1 := re.search(r".*sqrt\((.*x.*)\)",form):
        a = match1.group(1)
        for x in range(-100,100):
            try:
                if eval(a) >= 0:
                    range_of_values.append(x)
            except ZeroDivisionError:
                range_of_values.append(x+1)
    elif match1 := re.search(r"(.*)",form):
        a = match1.group(1)
        for x in range(-100,100):
            try:
               
                    range_of_values.append(x)
            except ZeroDivisionError:
                range_of_values.append(x+1)


    return range_of_values
if __name__ == "__main__":
    main()