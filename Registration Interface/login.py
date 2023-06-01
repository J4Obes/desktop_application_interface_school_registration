import tkinter
from tkinter import ttk
from tkinter import messagebox

def login():
    index = form_four_index_entry.get()
    comb = selected_combination_combobox.get()
    if index and comb:
        window.destroy()
        import student
    else:
        tkinter.messagebox.showwarning(title='Error', message='You must first enter your form four index number and your combination to log in to the system')


window = tkinter.Tk()
window.title('Login')
window.configure(bg='black')

frame = tkinter.Frame()
frame.pack()
frame.configure(bg='RosyBrown4')

# Login Frame
login_frame = tkinter.LabelFrame(frame, text='Login', font=('Bookman Old Style', 30))
login_frame.grid(row=0, column=0, sticky='news', padx=40, pady=40)
login_frame.configure(bg='DarkSeaGreen')

# Index number Label and Entry
form_four_index_label = tkinter.Label(login_frame, text='Form four index number', font=('Bookman Old Style', 15))
form_four_index_label.grid(row=0, column=0)
form_four_index_label.configure(bg='DarkSeaGreen')
form_four_index_entry = tkinter.Entry(login_frame)
form_four_index_entry.grid(row=0, column=1)

# Combination Label and Entry
selected_combination_label = tkinter.Label(login_frame, text='Your combination', font=('Bookman Old Style', 15))
selected_combination_label.grid(row=1, column=0)
selected_combination_label.configure(bg='DarkSeaGreen')
selected_combination_combobox = ttk.Combobox(login_frame, values=['PCM', 'PGM', 'EGM', 'PCB', 'CBG', 'HGE', 'HGK'])
selected_combination_combobox.grid(row=1, column=1)

for widget in login_frame.winfo_children():
    widget.grid_configure(padx=10, pady=15)

# Login Button
login_button = tkinter.Button(frame, text='Login', font=('Bookman Old Style', 25), command=login)
login_button.grid(row=1, column=0, sticky='ns', padx=20, pady=20)
login_button.configure(bg='DarkSeaGreen')


window.mainloop()
