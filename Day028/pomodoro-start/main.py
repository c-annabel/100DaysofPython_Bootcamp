from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = "✓"
WORK_MIN = 0.4
SECONDS_PER_MIN = 60
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = int(WORK_MIN * SECONDS_PER_MIN)
    short_break_sec = int(SHORT_BREAK_MIN * SECONDS_PER_MIN)
    long_break_sec = int(LONG_BREAK_MIN * SECONDS_PER_MIN)

    # If it's the 8th rep:
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # If it's the 2/4/6 rep:
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # If it's the 1/3/5/7 rep:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Can't monitor the screen on every refresh
# import time
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

def count_down(count):
    # formating the time:
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        # https://stackoverflow.com/questions/11328920/is-python-strongly-typed
        count_sec = f"0{count_sec}"  # Not in Java or swift etc. #Dynamic Typing, change from an integer to a string for display

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK
        check_label.config(text=marks)


    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Widget
# https://colorhunt.co (Color Hunt)
canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# position adjustment is essential
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
check_label.grid(column=1, row=3)

window.mainloop()
