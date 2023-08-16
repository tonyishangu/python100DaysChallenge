import tkinter

# creating a window
window = tkinter.Tk()

# change title
window.title('My First GUI Program')

# minimum size for the window
window.minsize(width=500, height=400)

# creating a label
my_label = tkinter.Label(text='I am a label', font=('Cursive', 18, 'bold'))
# display the label
my_label.pack()     #center of the program
# my_label.pack(side='left')       to the left





# keep the window running
window.mainloop()