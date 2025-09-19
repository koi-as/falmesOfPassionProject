import tkinter as tk
from tkinter import *

win=tk.Tk() # top level window
win.geometry('500x500') # width x height
win.title('hopeless romantic')

name1=StringVar()
name2=StringVar()

def flames():
    print('hello')

Label(win, text='Play FLAMES by Koi', font=('Arial', 15), bg='lightgoldenrodyellow').pack()

Label(win, text='Enter Your Name:').pack()
Entry(win, textvariable=name1).pack()
Label(win, text='Enter Your Crushes Name:').pack()
Entry(win, textvariable=name2).pack()

Button(win, text='SHOW RESULTS', bg='lightgoldenrodyellow', command=flames).pack()

win.mainloop()