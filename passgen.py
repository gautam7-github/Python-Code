'''
    PASSWORD GENERATOR
'''

import random
import string
import pyperclip


def password(length, num=False, strength='weak'):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punct = string.punctuation

    letter = lower + upper

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
            key = (random.randint(1, length) % length - 1)
            if key <= 2:
                key += length % (key+random.randint(4, 8))
            length -= key
            for n in range(int(key)):
                paswd += random.choice(digit)
        for i in range(length):
            paswd += random.choice(letter)
            paswd += random.choice(punct)
        paswd = list(paswd)
        for r in range(2, (key * random.randint(0, 100) // 7) % (length * 2)):
            random.shuffle(paswd)

    random.shuffle(paswd)
    paswd = ''.join(paswd)
    pyperclip.copy(paswd)
    print('copied to clipboard : 1')
    return paswd


if __name__ == "__main__":
    print('weak : ')
    print(password(8, num=True, strength='weak'))
    print('medium : ')
    print(password(8, num=True, strength='medium'))
    print('strong : ')
    print(password(8, num=True, strength='strong'))
