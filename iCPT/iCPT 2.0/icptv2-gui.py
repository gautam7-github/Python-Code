'''
    PASSWORD GENERATOR
'''

import random
import string
import pyperclip
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import secrets
import tkinter.font as font


def passwordMain(lengthOG, num=False, strength='weak', copy=False):
    letters = string.ascii_letters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punct = string.punctuation
    letter = lower + upper
    length = lengthOG

    # empty string to store password
    paswd = ''
    randomS = random.SystemRandom()
    if strength == 'weak':
        if num:
            length -= 2
            for n in range(2):
                paswd += randomS.choice(digit)
        for i in range(length):
            paswd += randomS.choice(lower)
        paswd = list(paswd)

    elif strength == 'medium':
        if num:
            key = (randomS.randint(1, length) % length) // 2
            if key <= 2:
                key += length % (key+4)
            length -= key
            for n in range(int(key)):
                paswd += randomS.choice(digit)
        for i in range(length-1):
            paswd += randomS.choice(letter)
        paswd += randomS.choice(punct)
        paswd = list(paswd)

    elif strength == 'strong':
        if num:
            key = int((randomS.randint(2, length) % length - 2))
        if key > length / 2:
            key = int(randomS.randint(1, key % length))
        length -= key
        for _ in range(int(key)):
            paswd += secrets.choice(digit)
        key2 = int(randomS.randint(2, (length + 1) // 2))
        if key2 < 3:
            key2 = 3
        for i in range(key2):
            paswd += secrets.choice(letters)
        length -= key2
        for k in range(length):
            paswd += secrets.choice(punct)
        paswd = list(paswd)
        for r in range(int(((length * randomS.randint(1, 100)) % (lengthOG)))):
            randomS.shuffle(paswd)
        if len(paswd) > lengthOG:
            paswd = paswd[:(lengthOG+1)]

    random.shuffle(paswd)
    paswd = ''.join(paswd)
    if copy:
        pyperclip.copy(paswd)
        print('copied to clipboard...')
    return paswd


win = Tk()
win.config(bg='black')
win.geometry('400x400')


# create Font object
myFont = font.Font(family='SF Pro Display')

label1 = Label(win, text='', fg='orange',
               bg='black', font=myFont)
label1.pack()
label2 = Label(win, text='', fg='green', bg='black', font=myFont)
label2.pack()
label3 = Label(win, text='', fg='red', bg='black', font=myFont)
label3.pack()

res_w = ''
res_m = ''
res_s = ''


def update_weak():
    length = len_scale.get()
    length = int(length)
    global res_w
    res_w = passwordMain(length, num=True, strength='weak', copy=False)
    label1.configure(text=res_w)


def update_medium():
    length = len_scale.get()
    length = int(length)
    global res_m
    res_m = passwordMain(length, num=True, strength='medium', copy=False)
    label2.configure(text=res_m)


def update_strong():
    length = len_scale.get()
    length = int(length)
    global res_s
    res_s = passwordMain(length, num=True, strength='strong', copy=False)
    label3.configure(text=res_s)


def copy_pass():
    answer = simpledialog.askstring("Input", "WHICH PASSWORD? (W/M/S)",
                                    parent=win)
    answer = answer[0]
    if answer.lower() == "w":
        pyperclip.copy(res_w)
    elif answer.lower() == "m":
        pyperclip.copy(res_m)
    elif answer.lower() == "s":
        pyperclip.copy(res_s)


len_label = Label(win, text="\|/ LENGTH \|/ ", fg='white', bg='black')
len_label.pack(pady=15, padx=15)
len_scale = Scale(win, from_=6, to=18, orient=HORIZONTAL)
len_scale.pack(pady=2)
btn1 = Button(win, text="PASSWORD WEAK",
              command=update_weak, bg='black', fg='orange')
btn1['font'] = myFont
btn1.pack()
btn2 = Button(win, text="PASSWORD MEDIUM",
              command=update_medium, bg='black', fg='green')
btn2['font'] = myFont
btn2.pack()
btn3 = Button(win, text="PASSWORD STRONG",
              command=update_strong, bg='black', fg='red')
btn3['font'] = myFont
btn3.pack()
btn4 = Button(win, text="COPY TO CLIPBOARD", command=copy_pass)
btn4.pack(pady=15)
win.mainloop()
