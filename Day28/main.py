from tkinter import *
import math

# -----------------Constants ----------------------
PINK =  '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Cursive'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------reset timer------------
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text='Timer')
    checkmark.config(text='')
    global reps
    reps = 0

# -----------------timer mechanism--------------
def start_timer():
    global reps
    reps +=1

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text='Short Break', fg=PINK)
    else:
        count_down(work_time)
        label.config(text='Work', fg=GREEN)

# ------------------countdown function ---------------

def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = '00'
    elif seconds < 10:
        seconds= f"0{str(seconds)}"

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=''
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            marks +='✔'
        checkmark.config(text=marks)

# --------------ui setup -----------

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
# window.after() execute a command after a time delay


# ----labels
label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
label.grid(column=1, row=0)

# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bc_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=bc_image)
timer_text = canvas.create_text(100,130,text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# ------buttons
start_btn = Button(text='Start', highlightthickness=0, bg=PINK, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', highlightthickness=0, bg=PINK, command=reset)
reset_btn.grid(column=3,row=2)

# -------checkmark
checkmark = Label(text='', fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()