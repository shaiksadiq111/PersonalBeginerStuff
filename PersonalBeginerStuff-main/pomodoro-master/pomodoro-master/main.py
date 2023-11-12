import tkinter
import os
import sys

bg_color = "#f7f6e7"
color1 = "#f7f6e7"
color2 = "#f875aa"

display = tkinter.Tk()
display.configure(bg=bg_color)
display.config(width=380, height=400)
display.title("Pomodoro")

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas()
canvas.config(width=230, height=300, highlightthickness=0)
canvas.configure(bg=bg_color)
canvas.create_image((115, 150), image=tomato_img)
canvas.place(x=90, y=40)

check_marks = tkinter.Label(text="✅")
check_marks.config(bg=bg_color)


def display_mark():
    x = 160
    y = 310
    check_marks.place(x=x, y=y)


timer_ = "25:00"
minutes = 24
second = 0


def timer_break(second):
    global minutes
    timer_ = f"{minutes}:{second}"
    canvas.itemconfig(timer_text, text=timer_)
    if second == 0:
        second = 60
        minutes -= 1
    if minutes == 0:
        minutes = 25
        print("\a")
        print("\a")
        print("\a")
        print("\a")
        start_timer()

    display.after(1000, timer, second - 1)


def timer(second):
    global minutes
    timer_ = f"{minutes}:{second}"
    canvas.itemconfig(timer_text, text=timer_)
    if second == 0:
        second = 60
        minutes -= 1
    if minutes == 0:
        minutes = 5
        print("\a")
        print("\a")
        print("\a")
        print("\a")
        display_mark()

    display.after(1000, timer, second - 1)


def start_timer():
    timer(60)


label1 = tkinter.Label()
label1.config(bg=bg_color, fg=color2, text="Timer", font=("Courier", 30, "bold"))
label1.place(x=160, y=40)

button1 = tkinter.Button()
button1.configure(text="Start", bg=bg_color, font=("Courier", 20, "bold"), highlightthickness=0, command=start_timer)
button1.place(x=25, y=320)

timer_text = canvas.create_text((120, 170), text=timer_, fill=color1, font=("Courier, 30"))


def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)


button2 = tkinter.Button()
button2.configure(text="Reset", bg=bg_color, font=("Courier", 20, "bold"), command=reset, highlightthickness=0)
button2.place(x=280, y=320)

display.mainloop()
