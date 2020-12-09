'''
    PASSWORD GENERATOR
'''

import random
import string
import pyperclip
from tkinter import *
import secrets


def weakPass():
    pass


def mediumPass():
    pass


def strongPass():
    pass


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

    if strength == 'weak':
        if num:
            length -= 2
            for n in range(2):
                paswd += random.choice(digit)
        for i in range(length):
            paswd += random.choice(lower)
        paswd = list(paswd)

    elif strength == 'medium':
        if num:
            key = (random.randint(1, length) % length) // 2
            if key <= 2:
                key += length % (key+4)
            length -= key
            for n in range(int(key)):
                paswd += random.choice(digit)
        for i in range(length-1):
            paswd += random.choice(letter)
        paswd += random.choice(punct)
        paswd = list(paswd)

    elif strength == 'strong':
        if num:
            key = int((random.randint(2, length) % length - 2))
        if key > length / 2:
            key = int(random.randint(1, key % length))
        length -= key
        for n in range(int(key)):
            paswd += secrets.choice(digit)
        key2 = int(random.randint(2, (length+1)//2))
        for i in range(key2):
            paswd += secrets.choice(letters)
        length -= key2
        for k in range(length):
            paswd += secrets.choice(punct)
        paswd = list(paswd)
        if len(paswd) > lengthOG:
            paswd = paswd[:(lengthOG+1)]
        for r in range(int(((length * random.randint(1, 100)) % (lengthOG)))):
            random.shuffle(paswd)

    random.shuffle(paswd)
    paswd = ''.join(paswd)
    if copy:
        pyperclip.copy(paswd)
        print('copied to clipboard...')
    return paswd


win = Tk()
win.config(bg='black')
label1 = Label(win, text='', fg='orange', bg='black', font=("Helvetica"))
label1.pack()
label2 = Label(win, text='', fg='green', bg='black', font=("Helvetica"))
label2.pack()
label3 = Label(win, text='', fg='red', bg='black', font=("Helvetica"))
label3.pack()


def update_weak():
    res = passwordMain(8, num=True, strength='weak', copy=False)
    label1.configure(text=res)


def update_medium():
    res = passwordMain(8, num=True, strength='medium', copy=False)
    label2.configure(text=res)


def update_strong():
    res = passwordMain(8, num=True, strength='strong', copy=False)
    label3.configure(text=res)


btn1 = Button(win, text="PASSWORD_WEAK", command=update_weak)
btn1.pack(pady=15)
btn2 = Button(win, text="PASSWORD_MEDIUM", command=update_medium)
btn2.pack(pady=15)
btn3 = Button(win, text="PASSWORD_STRONG", command=update_strong)
btn3.pack(pady=15)
win.mainloop()
