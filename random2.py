
"""
===================================================
hello there,
here is a simple traffic light program eith tkinter
i am yet to implement a time function
have fun and improve it
thank you
====================================================

 How to use:
 it runs with python 3.x and 2.7
 clicking of the buttons changes the circle colors

"""
print __doc__
import Tkinter
import tkMessageBox
from Tkinter import *

class trafficLights:
    def __init__(self):
        win=Tk()
        win.title("lights")

        frame = Frame(win)
        frame.pack()
        #.pack is there to be used for positioning the widget
        #https://www.tutorialspoint.com/python/tk_pack.htm
        #gives extar details on how to use .pack(options)

        self.canvas = Canvas(win, height=250, width=1000, bg="white")
        self.canvas.pack()

        #creating the circles
        self.red_shape = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.orange_shape = self.canvas.create_oval(120, 10, 220, 110, fill="white")
        self.green_shape = self.canvas.create_oval(230, 10, 330, 110, fill="white")

        #setting the color variation
        self.color = StringVar()
        #StringVar() this is the way to create a tkinter variable
        #tkinter uses this to pick given variables
        #for further details http://effbot.org/tkinterbook/variable.htm

        redButton= Radiobutton (frame, text="red", bg="red", variable=self.color,
                                value="r",command=self.RadioChange)
        redButton.grid(row=10, column=1)
        orangeButton= Radiobutton (frame, text="orange", bg="orange", variable=self.color,
                                value="o",command=self.RadioChange)
        orangeButton.grid(row=10, column=2)
        greenButton= Radiobutton (frame, text="green", bg="green", variable=self.color,
                                value="g",command=self.RadioChange)
        greenButton.grid(row=10, column=3)

        #picking a starting color
        self.color.set('r')
        self.canvas.itemconfig(self.red_shape, fill="red")


        #closiing the tkinter loop
        win.mainloop()

    def RadioChange(self):
        color = self.color.get()
        #setting the acommand to pick a given value
        if color == "r":
            self.canvas.itemconfig(self.red_shape, fill="red")
            self.canvas.itemconfig(self.orange_shape, fill="white")
            self.canvas.itemconfig(self.green_shape, fill="white")

        elif color == "o":
            self.canvas.itemconfig(self.red_shape, fill="white")
            self.canvas.itemconfig(self.orange_shape, fill="orange")
            self.canvas.itemconfig(self.green_shape, fill="white")
        elif color == "g":
            self.canvas.itemconfig(self.red_shape, fill="white")
            self.canvas.itemconfig(self.orange_shape, fill="white")
            self.canvas.itemconfig(self.green_shape, fill="green")



trafficLights()
