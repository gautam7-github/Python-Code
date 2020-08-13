import random
import time

start_list = ['hello', 'hi', 'hi there', 'yo', 'howdy']
starwars = {'hello there': '(general kenobi!)'}
global name_player


def start_game():
    print("ENTER YOUR NAME : ", end="")
    global name_player
    name_player = input()
    print(f"{name_player.upper()} GREET THE AI TO START THE GAME : ")
    start_runner = True
    while start_runner:
        start_input = input()
        if start_input in start_list:
            start_runner = False
            time.sleep(1.5)
            menu_start()
        elif start_input in starwars:
            start_runner = False
            print(starwars[start_input])
            time.sleep(1.5)
            menu_start()
        else:
            time.sleep(2)
            print("THE AI CAN GREET BETTER THAN YOU!!!")
            print("GREET AGAIN")


def menu_start():
    print("THE AI HAS AWOKEN")
    time.sleep(2)
    print(f"AI : WELCOME TO DUNGEONS & DRAGONS, {name_player.upper()}")
    time.sleep(2)
    print("AI : YOU ARE ABOUT TO EMBARK ON A WILD ADVENTURE")
    time.sleep(2)
    choice_menu()


def choice_menu():
    print("AI : CHOOSE YOUR ADVENTURE SETTING")
    time.sleep(2)
    print("1. MYSTERY")
    print("2. FANTASY")
    user_choice = int(input())
    if user_choice == 1:
        mystery_start()
    elif user_choice == 2:
        fntsy_start()
    else:
        print(f"AI : CHOOSE FROM THE ABOVE, {name_player.upper()}")


def mystery_start():
    print("AI : YOUR CHARACTER IS A ")
    time.sleep(2)
    print("1. DETECTIVE")
    print("2. SPY")
    choser = input()
    if choser == '1':
        user_chose = "DETECTIVE"
    elif choser == '2':
        user_chose = "SPY"
    else:
        user_chose = "DETECTIVE"
    setting = [1, 2, 3]
    ran = random.choice(setting)
    if ran == 1:
        mystery_start_setting1(user_chose)
    elif ran == 2:
        mystery_start_setting2(user_chose)
    else:
        mystery_start_setting3(user_chose)


def mystery_start_setting1(user_chose):
    print(f"\n\n\nYOU ARE {name_player.upper()}, A {user_chose} LIVING IN CHICAGO.")
    time.sleep(1)
    print("YOU HAVE A PISTOL AND A POLICE BADGE.")


def mystery_start_setting2(user_chose):
    print(f"\n\n\nYOU ARE A {user_chose},")


def mystery_start_setting3(user_chose):
    print(f"\n\n\nYOU ARE A {user_chose},")


def fntsy_start():
    pass


start_game()
