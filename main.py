import math

BLACK = "#1B1A17"
GOLD = "#F0A500"
ORANGE = "#E45826"
WHITISH = "#E6D5B8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    label.config(text= 'Timer')
    canvas.itemconfig(timer_txt, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_brk = SHORT_BREAK_MIN * 60
    long_brk = LONG_BREAK_MIN * 60
    reps += 1
    # print(reps)
    if reps % 8 == 0:
        counter(long_brk)
        label.config(text=" Long Break", fg=WHITISH)
    elif reps % 2 == 0:
        counter(short_brk)
        label.config(text="Break", fg=ORANGE)
    else:
        counter(work_sec)
        label.config(text="Work", fg=GOLD)
        # icon = "✔"
        # tick.config(text="✔")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    # count -= 1
    minutes = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        count_sec = f"0{sec}"
        pass
    else:
        count_sec = sec
    canvas.itemconfig(timer_txt, text=f"{minutes}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(math.floor(work_sessions)):
            marks += "✔"
            pass
        tick.config(text=marks)

    pass


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=BLACK)

label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=BLACK, fg=GOLD)
label.grid(row=0, column=1)
# canvas = Canvas(width=200, height=270, bg=BLACK, highlightthickness=0)
canvas = Canvas(width=200, height=270, bg=BLACK, highlightthickness=0)
dragon_img = PhotoImage(file="draco.png")
canvas.create_image(100, 135, image=dragon_img)
timer_txt = canvas.create_text(100, 180, text="00:00", font=(FONT_NAME, 32, "bold"), fill="White")
canvas.grid(row=1, column=1)


def action():
    # print("Do something")

    pass


# calls action() when pressed
start_but = Button(text="start", command=start_timer, highlightthickness=10)
start_but.grid(row=2, column=0)

reset = Button(text="reset", highlightthickness=10, command=reset_timer)
reset.grid(row=2, column=2)

tick = Label(fg=ORANGE, bg=BLACK)
tick.grid(row=3, column=1)

window.mainloop()
