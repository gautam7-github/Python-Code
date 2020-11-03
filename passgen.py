'''
    PASSWORD GENERATOR
'''

import random
import string

def password(length, num=False, strength='weak'):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    letter = lower + upper
    digit = string.digits
    punct = string.punctuation

    paswd = ''

    if strength == 'weak':
        if num:
            length -= 2
            for n in range(2):
                paswd += random.choice(digit)
        for i in range(length):
            paswd += random.choice(lower)
    elif strength == 'medium':
        for i in range(length):
            pass
    elif strength == 'strong':
        pass

    paswd = list(paswd)
    random.shuffle(paswd)
    return ''.join(paswd)

print(password(6,num=True))