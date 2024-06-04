import pandas as pd
import function as fn

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

Comfirm = Tk()
Comfirm.title('REGISTRATION COMFIRMATION')
Comfirm.geometry('500x200')
comfirm_a = IntVar()
comfirm_b = IntVar()

fn.open_new()

def submit():
    if comfirm_a.get() == 1:
        print('Please enter your user ID and password to login your account')
        Comfirm.destroy()
        fn.login()
        if fn.login():
            Q1 = print(input('Do you want to calculate your tax relief? yes/no'))
            if Q1 == 'yes':
                fn.salary_calculation()
            elif Q1 == 'no':
                Q2 = print(input('Do you want to read your previous data? yes/no'))
                if Q2 == 'yes':
                    fn.read()

    elif comfirm_b.get() == 1:
        print('Please register a account to save your information')
        Comfirm.destroy()
        fn.registration()

    elif comfirm_a.get() and comfirm_b.get() == 0:
        print('Please select either YES or NO to REGISTER or LOGIN a account')
        Comfirm.destroy()

Comfirm_label = Label(Comfirm, text='Do you have been registered a account?',padx=10,pady=10, font=('Helvetica 12')).grid(row=1,column=1)
YES_checkbox = Checkbutton(Comfirm, text='YES', variable=comfirm_a).grid(row=1,column=2)
NO_checkbox = Checkbutton(Comfirm, text='NO', variable=comfirm_b).grid(row=1,column=3)
button = Button(Comfirm, text='OK', padx=20,pady=10, command=submit).grid(row=3,column=2)

Comfirm.mainloop()


