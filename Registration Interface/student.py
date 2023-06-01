import tkinter
from tkinter import ttk
from tkinter import messagebox


def submit():
    terms_and_conditions = rules_and_regulations_variable.get()
    if terms_and_conditions == 'Agreed':
        first_name = first_name_entry.get()
        second_name = second_name_entry.get()
        last_name = last_name_entry.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        region = region_combobox.get()
        tribe = tribe_entry.get()
        religion = religion_combobox.get()
        district = district_entry.get()
        school = school_entry.get()
        ward = ward_entry.get()
        sport = sport_combobox.get()
        parent_status = parent_status_combobox.get()
        living_patner = living_patner_combobox.get()
        address = address_entry.get()
        combination = combination_combobox.get()

        if first_name and second_name and last_name and nationality and region and tribe and religion and age and district and school and ward and sport and parent_status and living_patner and address and combination:
            tkinter.messagebox.showinfo(title='Registration status', message='Congratulations, student\'s personal information has been saved')
            window.destroy()
            print('----------------------------------------------------------')
            import parent
        else:
            tkinter.messagebox.showwarning(title='Error', message='Fill all the required information.')
    else:
        tkinter.messagebox.showwarning(title='Error', message='You have not agreed with school rules and regulations.')

window = tkinter.Tk()
window.title("Student's information")

frame = tkinter.Frame(window)
frame.pack()
frame.configure(bg='RosyBrown4')

student_info_frame = tkinter.LabelFrame(frame, text="Personal information", font=('Bookman Old Style', 20))
student_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)
student_info_frame.configure(bg='DarkSeaGreen')

# First, Second and Last name Labels
first_name_label = tkinter.Label(student_info_frame, text="First name", font=('Bookman Old Style', 13))
first_name_label.grid(row=0, column=0)
first_name_label.configure(bg='DarkSeaGreen')
second_name_label = tkinter.Label(student_info_frame, text="Second name", font=('Bookman Old Style', 13))
second_name_label.configure(bg='DarkSeaGreen')
second_name_label.grid(row=0, column=1)
last_name_label = tkinter.Label(student_info_frame, text="Last name", font=('Bookman Old Style', 13))
last_name_label.configure(bg='DarkSeaGreen')
last_name_label.grid(row=0, column=2)

# First, Second and Last name Entries
first_name_entry = tkinter.Entry(student_info_frame)
first_name_entry.grid(row=1, column=0)
second_name_entry = tkinter.Entry(student_info_frame)
second_name_entry.grid(row=1, column=1)
last_name_entry = tkinter.Entry(student_info_frame)
last_name_entry.grid(row=1, column=2)

# Gender label and Entry
gender_label = tkinter.Label(student_info_frame, text="Gender", font=('Bookman Old Style', 13))
gender_combobox = ttk.Combobox(student_info_frame, values=['Male', 'Female'])
gender_label.configure(bg='DarkSeaGreen')
gender_label.grid(row=0, column=3)
gender_combobox.grid(row=1, column=3)

# Age Label and Entry
age_label = tkinter.Label(student_info_frame, text="Age", font=('Bookman Old Style', 13))
age_label.configure(bg='DarkSeaGreen')
age_spinbox = tkinter.Spinbox(student_info_frame, from_=15, to=24)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

# Date Label and Entry
date_label = tkinter.Label(student_info_frame, text='Date of birth',font=('Bookman Old Style', 13))
date_label.grid(row=2, column=1)
date_label.configure(bg='DarkSeaGreen')
date_spinbox = ttk.Spinbox(student_info_frame, from_=1, to=31)
date_spinbox.grid(row=3, column=1)

# Month Label and Entry
month_label = tkinter.Label(student_info_frame, text='Month', font=('Bookman Old Style', 13))
month_label.grid(row=2, column=2)
month_label.configure(bg='DarkSeaGreen')
month_combobox = ttk.Combobox(student_info_frame, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December'])
month_combobox.grid(row=3, column=2)

# Year Label and Spinbox
year_label = tkinter.Label(student_info_frame, text='Year', font=('Bookman Old Style', 13))
year_label.grid(row=2, column=3)
year_label.configure(bg='DarkSeaGreen')
year_spinbox = ttk.Spinbox(student_info_frame, from_=1980, to=2023)
year_spinbox.grid(row=3, column=3)

# Nation Label and Combobox
nationality_label = tkinter.Label(student_info_frame, text="Nation", font=('Bookman Old Style', 13))
nationality_combobox = ttk.Combobox(student_info_frame, values=["Tanzania", "Uganda", "Kenya", "Rwanda", "Burundi", "South Sudan"])
nationality_label.configure(bg='DarkSeaGreen')
nationality_label.grid(row=4, column=0)
nationality_combobox.grid(row=5, column=0)

# Region Label and Combobox
region_label = tkinter.Label(student_info_frame, text="Region", font=('Bookman Old Style', 13))
region_combobox = ttk.Combobox(student_info_frame, values=['Shinyanga', 'Mwanza', 'Tabora', 'Dar es salaam'])
region_label.configure(bg='DarkSeaGreen')
region_label.grid(row=4, column=1)
region_combobox.grid(row=5, column=1)

# District Label and Entry
district_label = tkinter.Label(student_info_frame, text='District', font=('Bookman Old Style', 13))
district_label.grid(row=4, column=2)
district_label.configure(bg='DarkSeaGreen')
district_entry = tkinter.Entry(student_info_frame)
district_entry.grid(row=5, column=2)

# Ward Label and Entry
ward_label = tkinter.Label(student_info_frame, text='Ward', font=('Bookman Old Style', 13))
ward_label.grid(row=4, column=3)
ward_label.configure(bg='DarkSeaGreen')
ward_entry = tkinter.Entry(student_info_frame)
ward_entry.grid(row=5, column=3)

# School Label and Entry
school_lable = tkinter.Label(student_info_frame, text="Former school", font=('Bookman Old Style', 13))
school_lable.configure(bg='DarkSeaGreen')
school_lable.grid(row=6, column=0)
school_entry = tkinter.Entry(student_info_frame)
school_entry.grid(row=7, column=0)

# Combination Label and Combobox
combination_label = tkinter.Label(student_info_frame, text='Combination', font=('Bookman Old Style', 13))
combination_label.grid(row=6, column=1)
combination_label.configure(bg='DarkSeaGreen')
combination_combobox = ttk.Combobox(student_info_frame, values=['PCM', 'PGM', 'EGM', 'PCB', 'CBG', 'HGE', 'HGK'])
combination_combobox.grid(row=7, column=1)

# Sports Label and Combobox
sport_label =  tkinter.Label(student_info_frame, text='Sport you play', font=('Bookman Old Style', 13))
sport_label.configure(bg='DarkSeaGreen')
sport_label.grid(row=6, column=2)
sport_combobox = ttk.Combobox(student_info_frame, values=['None','Football', 'Netball', 'Basketball', 'Voleyball', 'Riadha', 'Tennis', 'Cricket'])
sport_combobox.grid(row=7, column=2)

# Address Label and Entry
address_label = tkinter.Label(student_info_frame, text='Address', font=('Bookman Old Style', 13))
address_label.grid(row=6, column=3)
address_label.configure(bg='DarkSeaGreen')
address_entry = tkinter.Entry(student_info_frame)
address_entry.grid(row=7, column=3)

# Religion Label and Combobox
religion_label = tkinter.Label(student_info_frame, text='Religion', font=('Bookman Old Style', 13))
religion_combobox = ttk.Combobox(student_info_frame, values=['Islam', 'Christian', 'Other'])
religion_label.configure(bg='DarkSeaGreen')
religion_label.grid(row=8, column=0)
religion_combobox.grid(row=9, column=0)

# Tribe Label and Entry
tribe_label = tkinter.Label(student_info_frame, text='Tribe', font=('Bookman Old Style', 13))
tribe_label.configure(bg='DarkSeaGreen')
tribe_label.grid(row=8, column=1)
tribe_entry = tkinter.Entry(student_info_frame)
tribe_entry.grid(row=9, column=1)

# Living Patner Label and Entry
living_patner_label = tkinter.Label(student_info_frame, text='Who do you live with?', font=('Bookman Old Style', 13))
living_patner_label.grid(row=8, column=2)
living_patner_label.configure(bg='DarkSeaGreen')
living_patner_combobox = ttk.Combobox(student_info_frame, values=['Father only', 'Mother only', 'Both parents', 'Guardian'])
living_patner_combobox.grid(row=9, column=2)

# Parent Status Label and Combobx
parent_status_label = tkinter.Label(student_info_frame, text='Do parents live?', font=('Bookman Old Style', 13))
parent_status_label.grid(row=8, column=3)
parent_status_label.configure(bg='DarkSeaGreen')
parent_status_combobox = ttk.Combobox(student_info_frame, values=['Father only', 'Mother only', 'Both parents', 'All died'])
parent_status_combobox.grid(row=9, column=3)

for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

rules_and_regulations = tkinter.LabelFrame(frame)
rules_and_regulations.grid(row=1, column=0, sticky='news', padx=20, pady=10)
rules_and_regulations.configure(bg='DarkSeaGreen')

rules_and_regulations_label = tkinter.Label(rules_and_regulations, text='School Rules & Regulations', font=('Bookman Old Style', 20))
rules_and_regulations_label.configure(bg='DarkSeaGreen')

rules_and_regulations_variable = tkinter.StringVar(value='Not agreed')
rules_and_regulations_check_buton = tkinter.Checkbutton(rules_and_regulations, text='I Agree with all the school rules and regulations.', font=('Bookman Old Style', 15), variable=rules_and_regulations_variable, onvalue='Agreed', offvalue='Not agreed')
rules_and_regulations_check_buton.configure(bg='DarkSeaGreen')

rules_and_regulations_label.grid(row=0, column=0)
rules_and_regulations_check_buton.grid(row=1, column=0)

button = tkinter.Button(frame, text="Save and submit", font=('Bookman Old Style', 25),  command= submit)
button.grid(row=2, column=0, sticky="ns", padx=20, pady=10)
button.configure(bg='DarkSeaGreen')

window.mainloop()
