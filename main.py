from tkinter import *
import math

COLOUR_1 = "#0F0E0E"
COLOUR_2 = "#FEC260"
COLOUR_3 = "#EDEDED"
FONT_NAME = "Times"
timer = None


def stop_timer():
    window.after_cancel(timer)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    start_count(00)


def start_count(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, start_count, count + 1)




window = Tk()
window.title("Stopwatch")
window.config(padx=15, pady=15, bg=COLOUR_2)

title_label = Label(text="STOPWATCH", fg=COLOUR_1, bg=COLOUR_2, font=FONT_NAME)
title_label.grid(column=1, row=0)

canvas = Canvas(width=300, height=280, bg=COLOUR_2, highlightthickness=0)
watch = PhotoImage(file="black.png")
canvas.create_image(150, 130, image=watch)
timer_text = canvas.create_text(150, 125, text="00:00", font=(FONT_NAME, 50, "bold"), fill=COLOUR_3)
canvas.grid(columnspan=3, rowspan=2)

start_button = Button(text="Start", highlightthickness=0, width=12, command=start_timer)
start_button.grid(column=0, row=3)
stop_button = Button(text="Stop", highlightthickness=0, width=10, command=stop_timer)
stop_button.grid(column=1, row=3)
reset_button = Button(text="Reset", highlightthickness=0, width=12, command=reset_timer)
reset_button.grid(column=2, row=3)

window.mainloop()
