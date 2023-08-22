from tkinter import *

# creating a window
window = Tk()

# change title
window.title('My First GUI Program')

# minimum size for the window
window.minsize(width=500, height=400)

# creating a label
my_label = Label(text='I am a label', font=('Cursive', 18, 'bold'))
# display the label
my_label.pack()     #center of the program
# my_label.pack(side='left')       to the left

# changing label like a dictionary
my_label['text'] = 'new label'
my_label.config(text='new labels')

# buttons
def clicked_button():
    text = input.get()
    my_label['text'] = text

btn = Button (text='click me', command=clicked_button)
btn.pack()

# entry
input = Entry(width=10)
# input.pack()
input.place(x=0,y=0) #also used to display on the screen



# keep the window running
window.mainloop()