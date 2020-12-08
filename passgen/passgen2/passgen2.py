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


def main():
    res = passwordMain(8, num=True, strength='weak', copy=False)
    res2 = passwordMain(8, num=True, strength='medium', copy=False)
    res3 = passwordMain(9, num=True, strength='strong', copy=False)
    win = Tk()
    win.title("PASSGEN 2.0")
    win.configure(bg='black')
    label1 = Label(win, text=res, fg='orange', bg='black', font=("Helvetica"))
    label1.pack()
    label2 = Label(win, text=res2, fg='green', bg='black', font=("Helvetica"))
    label2.pack()
    label3p = Label(win, text=res3, fg='red', bg='black', font=("Helvetica"))
    label3p.pack()

    btn1 = Button(win, text="PRESS HERE").pack(pady=15)
    win.mainloop()


if __name__ == "__main__":
    main()
