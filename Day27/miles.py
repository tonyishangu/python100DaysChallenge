from tkinter import *

window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=30, pady=30)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f'{km}')

miles_input = Entry(width=6)
miles_input.grid(column= 1, row=0 )

miles_label = Label(text='Miles')
miles_label.grid(column= 2, row= 0)

label = Label(text='is equal to')
label.grid(column= 0, row= 1)

km_result_label = Label(text='0')
km_result_label.grid(column= 1, row= 1)

km_label = Label(text='Km')
km_label.grid(column= 2, row= 1)

calc_button = Button(text='calculate', command=miles_to_km)
calc_button.grid(column= 1, row= 2)


window.mainloop()