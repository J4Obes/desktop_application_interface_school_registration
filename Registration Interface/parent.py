import tkinter
from tkinter import ttk
from tkinter import messagebox

def submit():
        first_name = first_name_entry.get()
        second_name = second_name_entry.get()
        last_name = last_name_entry.get()
        if first_name and second_name and last_name:
            tkinter.messagebox.showinfo(title='Registration status', message='Registration complete')
            window.destroy()
            print('First name:', first_name, 'Second name:', second_name, 'Last name:', last_name)
            print('-------------------------------------------------------------------------------------------------------')
        else:
            tkinter.messagebox.showwarning(title='Error', message='Fill all the required information')

window = tkinter.Tk()
window.title('Parent/Guardian information')

frame = tkinter.Frame(window)
frame.pack()
frame.configure(bg='RosyBrown4')

parents_information_frame = tkinter.LabelFrame(frame, text='Parent/Guardian information', font=('Bookman Old Style', 20))
parents_information_frame.grid(row=0, column=0, sticky='news', padx=20, pady=5)
parents_information_frame.configure(bg='DarkSeaGreen')

# First, Second and Last name Labels
first_name_label = tkinter.Label(parents_information_frame, text='First name', font=('Bookman Old Style', 15))
first_name_label.grid(row=0, column=0)
first_name_label.configure(bg='DarkSeaGreen')
second_name_label = tkinter.Label(parents_information_frame, text='Second name', font=('Bookman Old Style', 15))
second_name_label.grid(row=0, column=1)
second_name_label.configure(bg='DarkSeaGreen')
last_name_label = tkinter.Label(parents_information_frame, text='Last name', font=('Bookman Old Style', 15))
last_name_label.grid(row=0, column=2)
last_name_label.configure(bg='DarkSeaGreen')

# First, Second and Last name Entries
first_name_entry = tkinter.Entry(parents_information_frame)
first_name_entry.grid(row=1, column=0)
second_name_entry = tkinter.Entry(parents_information_frame)
second_name_entry.grid(row=1, column=1)
last_name_entry = tkinter.Entry(parents_information_frame)
last_name_entry.grid(row=1, column=2)

# Gender label and Entry
gender_label = tkinter.Label(parents_information_frame, text='Gender', font=('Bookman Old Style', 15))
gender_label.grid(row=0, column=3)
gender_label.configure(bg='DarkSeaGreen')
gender_combobox = ttk.Combobox(parents_information_frame, values=['Male', 'Female'])
gender_combobox.grid(row=1, column=3)

# Specificity Label and Combobox
specificity = tkinter.Label(parents_information_frame, text='Specify', font=('Bookman Old Style', 15))
specificity_combobox = ttk.Combobox(parents_information_frame, values=['Father', 'Mother', 'Guardian'])
specificity.configure(bg='DarkSeaGreen')
specificity.grid(row=2, column=0)
specificity_combobox.grid(row=3, column=0)

# Phone number Label and Entry
phone_number = tkinter.Label(parents_information_frame, text='Available phone number', font=('Bookman Old Style', 15))
phone_number_entry = tkinter.Entry(parents_information_frame)
phone_number.configure(bg='DarkSeaGreen')
phone_number.grid(row=2, column=1)
phone_number_entry.grid(row=3, column=1)

# E-Mail Label and Entry
email_address = tkinter.Label(parents_information_frame, text='Email address(If available)', font=('Bookman Old Style', 15))
email_address_entry = tkinter.Entry(parents_information_frame)
email_address.configure(bg='DarkSeaGreen')
email_address.grid(row=2, column=2)
email_address_entry.grid(row=3, column=2)

# Occupation Label and Entry
occupation_label = tkinter.Label(parents_information_frame, text='Occupation', font=('Bookman Old Style', 15))
occupation_label.configure(bg='DarkSeaGreen')
occupation_label.grid(row=2, column=3)
occupation_entry =tkinter.Entry(parents_information_frame)
occupation_entry.grid(row=3, column=3)

# Nation Label and Combobox
nationality_label = tkinter.Label(parents_information_frame, text='Nationality', font=('Bookman Old Style', 15))
nationality_label.configure(bg='DarkSeaGreen')
nationality_label.grid(row=4, column=0)
nationality_combobox = ttk.Combobox(parents_information_frame, values=['Tanzania', 'Kenya', 'Uganda', 'Rwanda', 'Burundi'])
nationality_combobox.grid(row=5, column=0)

# Region Label and Combobox
region_label = tkinter.Label(parents_information_frame, text='Region', font=('Bookman Old Style', 15))
region_label.configure(bg='DarkSeaGreen')
region_label.grid(row=4, column=1)
region_combobox = ttk.Combobox(parents_information_frame, values=['Arusha', 'Mwanza', 'Kigoma', 'Tabora'])
region_combobox.grid(row=5, column=1)

# District Label and Entry
district_label = tkinter.Label(parents_information_frame, text='District', font=('Bookman Old Style', 15))
district_label.configure(bg='DarkSeaGreen')
district_label.grid(row=4, column=2)
district_entry = tkinter.Entry(parents_information_frame)
district_entry.grid(row=5, column=2)

# Ward Label and Entry
ward_label = tkinter.Label(parents_information_frame, text='Ward', font=('Bookman Old Style', 15))
ward_label.configure(bg='DarkSeaGreen')
ward_label.grid(row=4, column=3)
ward_entry = tkinter.Entry(parents_information_frame)
ward_entry.grid(row=5, column=3)

for widget in parents_information_frame.winfo_children():
    widget.grid_configure(padx=15, pady=8)

# Submit Button
submit_button = tkinter.Button(frame, text='Save and submit', font=('Bookman Old Style', 25), command=submit)
submit_button.grid(row=1, column=0, sticky='ns', padx=20, pady=10)
submit_button.configure(bg='DarkSeaGreen')

window.mainloop()
