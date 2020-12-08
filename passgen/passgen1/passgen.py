'''
    PASSWORD GENERATOR
'''

import random
import string
import pyperclip
import secrets


def password(lengthOG, num=False, strength='weak'):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punct = string.punctuation
    letters = string.ascii_letters
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
            key = (random.randint(0, length) % length) // 2
            if key <= 2:
                key += length % (key+4)
            length -= key
            for n in range(int(key)):
                paswd += random.choice(digit)
        for i in range(length):
            paswd += random.choice(letter)
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
    pyperclip.copy(paswd)
    print('copied to clipboard : 1')
    return paswd


if __name__ == "__main__":
    print('weak : ')
    print(password(10, num=True, strength='weak'))
    print('medium : ')
    print(password(8, num=True, strength='medium'))
    print('strong : ')
    print(password(18, num=True, strength='strong'))
