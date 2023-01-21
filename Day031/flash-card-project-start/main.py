#Wikipedia List: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
#hermitedave/FrequencyWords:
#OpenSubtitle: https://www.opensubtitles.org/en/search/subs
#GoogleTranslate: GOOGLETRANSLATE(text, [source_language, target_language])
#=GoogleTranslate(A2, "es", "en")
#Google Language Support: https://cloud.google.com/translate/docs/languages?hl=en

from tkinter import *
import pandas
import random

FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

# ---------------------------- MAIN SETUP ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data= pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    #french_dict = {row.French: row.English for (index, row) in data.iterrows()}
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text = "French", fill="black")
    canvas.itemconfig(word_text, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text = current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) #No index saved

    next_card()


    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
#window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas Widget
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# position adjustment is essential
card_background = canvas.create_image(400, 263, image=card_front_img)
#canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=cross_image, highlightthickness=0, command=next_card)
no_button.config(highlightbackground=BACKGROUND_COLOR)
no_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
yes_button = Button(image=check_image, highlightthickness=0, command=is_known)
yes_button.config(highlightbackground=BACKGROUND_COLOR)
yes_button.grid(column=1, row=1)

next_card()

window.mainloop()


