#Coding Horror: blog.codinghorror.com/password-rules-are-bullshit/
from tkinter import *  #doesn't import messagebox, another module of the code
from tkinter import messagebox #not a class
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
#https://www.w3schools.com/python/ref_string_join.asp
#https://pypi.org/project/pyperclip/
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)

    #copy the password too. Pyperclip
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
#effbot (message box) from Tkinter
def save():
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        #messagebox.showinfo(title="Title", message="Information saved!")
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}"
                                                              f"\nEmail: {email}"
                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                email_user_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=30, pady=30, bg="pink")

# Canvas Widget
# https://colorhunt.co (Color Hunt)
# https://tkdocs.com/tutorial/canvas.html
canvas = Canvas(width=250, height=250, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
# position adjustment is essential
canvas.create_image(125, 125, image=logo_img)
canvas.grid(column=1, row=0)

#Labels, columnspan for spanning the columns
website_label = Label(text="Website:", bg="pink", height=2)
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username:", bg="pink", height=1)
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="pink", height=1)
password_label.grid(column=0, row=3)

#Entries
#Tkinsert doc: effbot.org/tkinterbook/entry.htm
website_input = Entry(width=38, highlightbackground="pink")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()  #curson locates
email_user_input = Entry(width=38, highlightbackground="pink")
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "email@address") #insert(END) curson locates in the end of the text
password_input = Entry(width=21, highlightbackground="pink")
password_input.grid(column=1, row=3)

#Buttons (entry 38 = button 36 = entry+button 34, line width = 4)
gp_button = Button(text="Generate Password", highlightbackground="pink", width=13, command=generate_password)
gp_button.grid(column=2, row=3)
add_button = Button(text="Add", highlightbackground="pink", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()