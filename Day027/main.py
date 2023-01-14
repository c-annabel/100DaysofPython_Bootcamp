# TKinter
# GUI
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# Pack(one by one)/Place(precise place)/Grid (only choose one for all)

import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #Adding padding

def button_clicked():
    print("I got clicked.")
    #my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
# my_label.pack(side="left")
#1st method------
my_label["text"] = "New Text"
#2nd method------
my_label.config(text="New Text", padx=20, pady=10)
#my_label.pack() #side=: left, bottom or right
#my_label.place(x=0, y=0) #if no coordinate, it wont show.
my_label.grid(column=0, row=0) #if no widget previously, the position will be the same


#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#New Button
new_button = tkinter.Button(text="2nd Button", command=button_clicked)
#button.pack()
new_button.grid(column=3, row=0)

#Entry
input = tkinter.Entry(width=10)
print(input.get())
#input.pack()
input.grid(column=4, row=3)


# import turtle
# tim = turtle.Turtle()
# tim.hideturtle()
# tim.write("Test Turtle")


window.mainloop()
