from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pwd_input.get()
    with open('data.txt', 'a') as data_file:
        data_file.write(f'{website} : {email} : {password}\n')
        web_input.delete(0, END)
        pwd_input.delete(0, END)


        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100 , image= bg_image)
canvas.grid(column=1, row=0)

web_label = Label(text='Website:')
web_label.grid(column=0,row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
pwd_label = Label(text='Password:')
pwd_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1,row=1, columnspan=2)
web_input.focus()
email_input = Entry(width=35)
email_input.insert(0, 'tony@gmail.com')
email_input.grid(column=1, row=2, columnspan=2)
pwd_input = Entry(width=21)
pwd_input.grid(column=1, row=3)

generate_btn = Button(text='Generate Password', width=15, highlightthickness=0)
generate_btn.grid(column=2, row=3)
addBtn = Button(text='Add', width=35, highlightthickness=0, command=save)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()