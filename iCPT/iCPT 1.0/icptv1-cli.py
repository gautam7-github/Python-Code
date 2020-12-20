'''
        iCPT

    iNTELLIGENT COMPLETE PASSWORD GENERATOR TOOL


'''
import pyperclip
import random
import string
import pyperclip
import secrets
import datetime


def password(lengthOG, num=False, strength='weak', copy=False):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punct = string.punctuation
    letters = string.ascii_letters
    letter = lower + upper
    length = lengthOG

    # empty string to store password
    paswd = ''
    randomS = random.SystemRandom()
    randomS.seed(datetime.datetime.now())
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
            key = (randomS.randint(0, length) % length) // 2
            if key <= 2:
                key += length % (key+4)
            length -= key
            for n in range(int(key)):
                paswd += randomS.choice(digit)
        for i in range(length):
            paswd += randomS.choice(letter)
        paswd = list(paswd)

    elif strength == 'strong':
        if num:
            key = int((randomS.randint(2, length) % length - 2))
        if key > length / 2:
            key = int(randomS.randint(1, key % length))
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
        print('copied to clipboard : 1')
    return paswd


if __name__ == "__main__":
    while True:
        print("S for Strong")
        print("M for Mediocre")
        print("W for Weakling")
        user_choice = input("ENTER STRENGTH : ")
        if user_choice.upper() == "EXIT":
            break
        pass_len = int(input("LENGTH? : "))
        pass_copy = input("COPY TO CLIPBOARD? (YES/NO) : ")
        pass_copy = pass_copy.upper()
        if user_choice.upper() == "W":
            if pass_copy == "YES":
                print(password(pass_len, num=True, strength='weak', copy=True))
            elif pass_copy == "NO":
                print(password(pass_len, num=True, strength='weak', copy=False))
        elif user_choice.upper() == "M":
            print(password(pass_len, num=True, strength='medium', copy=False))
        elif user_choice.upper() == "S":
            print(password(pass_len, num=True, strength='strong', copy=False))
        else:
            print("RETRY...")
