from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
to_learn = {}
try:
    data = pandas.read_csv('data/wordsToLearn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global curr_card, timer
    window.after_cancel(timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=curr_card['French'], fill='black')
    canvas.itemconfig(img, image=front_card)
    timer = window.after(3000, func=card_flip)

def card_flip():
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=curr_card['English'], fill='white')
    canvas.itemconfig(img, image=back_card)

def is_known():
    to_learn.remove(curr_card)
    data  = pandas.DataFrame(to_learn)
    data.to_csv('data/wordsToLearn.csv', index=False)
    next_card()

window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file='images/card_front.png')
back_card = PhotoImage(file='images/card_back.png')
img = canvas.create_image(400, 263,image=front_card)
title = canvas.create_text(400, 150, text='', font=('cursive', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('cursive', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

crossImg = PhotoImage(file='images/wrong.png')
unknownButton = Button(image=crossImg, highlightthickness=0, command=next_card)
unknownButton.grid(column=0, row=1)

checkImg = PhotoImage(file='images/right.png')
checkBtn = Button(image=checkImg, highlightthickness=0, command=is_known)
checkBtn.grid(column=1,row=1)

next_card()
window.mainloop()
