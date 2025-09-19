import tkinter as tk
from tkinter import *

win=tk.Tk() # top level window
win.geometry('500x500') # width x height
win.title('hopeless romantic')

name1=StringVar()
name2=StringVar()

def flames():
    n1=name1.get()
    n2=name2.get()
    namestr=n1+n2
    for i in namestr: # for the integer count of letters in namestr
        if namestr.count(i) != 1: # if namestr.count(integer length of namestr) is not equal to 1 
            namestr=namestr.replace(i,"") # replace all repeated letters with blank space. so result of 'google' + 'yahoo' would be 'leyah'
 
    number=len(namestr)%6 # getting count of new string name and taking remainder (modulus) of division by 6
    global rel # what is global rel?
    rel=""
    if number==1:
        rel+="Friends"
    elif number==2:
        rel+="Love"
    elif number==3:
        rel+="Affection"
    elif number==4:
        rel+="Marriage"
    elif number==5:
        rel+="Enemy"
    elif number==0:
        rel+="Siblings"
    else:
        pass # what is pass?
   
    Label(win, text="According to the Game of Flames, your relationship is:").pack()
    Label(win, text=rel).pack()

Label(win, text='Play FLAMES by Koi', font=('Arial', 15), bg='lightgoldenrodyellow').pack()

Label(win, text='Enter Your Name:').pack()
Entry(win, textvariable=name1).pack()
Label(win, text='Enter Your Crushes Name:').pack()
Entry(win, textvariable=name2).pack()

Button(win, text='SHOW RESULTS', bg='lightgoldenrodyellow', command=flames).pack()

win.mainloop()