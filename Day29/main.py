from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # list comprehension for the for loop below
    pwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pwd_list = pwd_letters + pwd_symbols + pwd_numbers

    shuffle(pwd_list)
    password = ''.join(pwd_list)
    pwd_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_input.get()
    email = email_input.get()
    password = pwd_input.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='please fill all the  fields')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Email: {email} \npassword: {password} \nIs it ok to save?')
            
        if is_ok:
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

generate_btn = Button(text='Generate Password', width=15, highlightthickness=0, command=generate_pwd)
generate_btn.grid(column=2, row=3)
addBtn = Button(text='Add', width=35, highlightthickness=0, command=save)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()