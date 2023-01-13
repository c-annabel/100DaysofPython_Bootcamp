# TKinter
# GUI
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack()

# import turtle
#
# tim = turtle.Turtle()
# tim.hideturtle()
# tim.write("Test Turtle")

window.mainloop()
