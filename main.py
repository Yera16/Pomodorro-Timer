from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
def start_button_clicked ():
    global reps
    reps += 1
    work_time = WORK_MIN*60
    relax_time = LONG_BREAK_MIN*60
    short_relax_time = SHORT_BREAK_MIN*60
    if reps % 8 == 0:
        countdown(relax_time)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_relax_time)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_time)
        timer_label.config(text="Work Time", fg=RED)
def reset_button_clicked ():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")



def countdown(count):
    min = int(count/60)
    sec = (count % 60)
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_button_clicked()
        marks = ""
        for _ in range(math.floor(reps/2)):
          marks+="✓"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(108, 115, image=tomato_img)
timer_text = canvas.create_text(108,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)



timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1,row=0)

checkmark_label = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME, 30, "bold"))
checkmark_label.grid(column=1,row=3)

start_button = Button(text="Start", command=start_button_clicked ,highlightthickness = 0, bd = 0)
start_button.config(padx=1,pady=2)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_button_clicked, highlightthickness = 0, bd = 0)
reset_button.config(padx=1,pady=2)
reset_button.grid(column=2,row=2)






window.mainloop()