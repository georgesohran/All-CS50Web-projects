# Math drawing
#### Video Demo:  https://youtu.be/OOxBY7DS3ac
This is my final project for CS50
# Description:

## Libraries i used:
1. **tkinter**
for creating GUI
2. **numpy**
for one function that gives me a range of floats: _arange()_
3. **re**
to match formula that was given
4. **math**
to compute the functions like _cos, sin_, etc.

## How Does It Work?
### Main screen
The program opens the window with the help of Tkinter module. There is an entry for the formula, entry for the zoom value and a button that generates the graph on a dedicated canvas on the left of the window.
### Generating graphs
First-of-all the program gets the users input from zoom entry and formula entry and then, based on the formula, it generates _y_ coordinate for each _x_ from -100 to 100 and then draws a line from the previous coordinates to the new coordinates with _canvas.create_line_ method. Also it draws marks on each axis of the value 1. The zoom works as follows: the program gets the input value, then multiplies the _x_ and _y_ coordinates of the lines on the graph and of the marks on both axis by this value.

## Thank you for your atention, and thanks to CS50 for the course.