from tkinter import *

# -----------------Constants ----------------------
PINK =  '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Cursive'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# --------------ui setup -----------

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bc_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=bc_image)
canvas.create_text(100,130,text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.pack()


window.mainloop()