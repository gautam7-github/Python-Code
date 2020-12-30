'''
        iCPT

    iNTELLIGENT COMPLETE PASSWORD GENERATOR TOOL


'''
import pyperclip
import regex
import random
import string
import pyperclip
import secrets
import datetime
import os


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
        key2 = int(randomS.randint(2, (length+1)//2))
        for i in range(key2):
            paswd += secrets.choice(letters)
        length -= key2
        for k in range(length):
            paswd += secrets.choice(punct)
        paswd = list(paswd)
        if len(paswd) > lengthOG:
            paswd = paswd[:(lengthOG+1)]
        for r in range(int(((length * randomS.randint(1, 100)) % (lengthOG)))):
            random.shuffle(paswd)

    random.shuffle(paswd)
    paswd = ''.join(paswd)
    if copy:
        pyperclip.copy(paswd)
        print('copied to clipboard : 1')
    return paswd


def check_ST(password_USER):
    strongRegex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
    mediumRegex = r"^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})"
    if regex.match(strongRegex, password_USER) is not None:
        print(f'Password : {password_USER} : STRONG')
    elif regex.match(mediumRegex, password_USER) is not None:
        print(f'Password : {password_USER} : MEDIUM')
    else:
        print(f'Password : {password_USER} : WEAK')


def RUNAPP_GENPASS():
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


if __name__ == "__main__":
    user_says = '0'
    while user_says != '3':
        if os.name == 'posix':
            _ = os.system("clear")
        else:
            _ = os.system("cls")
        user_says = input('''
        1. GENERATE PASSWORD
        2. CHECK PASSWORD STRENGTH
        3. EXIT
        $$ :
        ''')[0]
        if user_says == '1':
            RUNAPP_GENPASS()
            _ = input()  # getch() equivalent
        elif user_says == '2':
            password_by_user = input(" :PASSWORD: -> ")
            check_ST(password_USER=password_by_user)
            _ = input()  # getch() equivalent
