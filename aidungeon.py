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
    user_choice = int(input(" - > "))
    if user_choice == 1:
        mystery_start()
    elif user_choice == 2:
        fntsy_start()
    else:
        print(f"AI : CHOOSE FROM THE ABOVE, {name_player.upper()}")
        choice_menu()


def mystery_start():
    print("AI : YOUR CHARACTER IS A ")
    time.sleep(2)
    print("1. DETECTIVE")
    print("2. SPY")
    choser = int(input(" - > "))
    if choser == 1:
        user_chose = "DETECTIVE"
    elif choser == 2:
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
    print(f"YOU ARE {name_player.upper()}, A {user_chose} LIVING IN CHICAGO.")
    time.sleep(1)
    print("YOU HAVE A PISTOL AND A POLICE BADGE.")
    print("YOU ENTER THE FOREST WHERE YOU BELIEVE THE CRIMINAL", end="")
    print("YOU ARE SEARCHING FOR FLED TO.")
    time.sleep(1)
    print("SUDDENLY, YOU HEAR A NOISE.")
    print("YOU TURN AROUND AND SEE A MAN POINTING A GUN AT YOU.")
    time.sleep(1)
    print('"YOU!" THE MAN SAYS.')
    print("AI : WHAT DO YOU DO ?")
    time.sleep(1)
    print("1. SHOOT HIM")
    print("2. TAKE COVER")
    time.sleep(1)
    userdo = input(" - > ")
    if userdo == '1':
        mystery_start_setting1_part1()
    elif userdo == '2':
        mystery_start_setting1_part2()
    else:
        print(f"CHOOSE PROPERLY {name_player.upper()}")


def mystery_start_setting1_part1():
    pass


def mystery_start_setting1_part2():
    pass


def mystery_start_setting2(user_chose):
    print(f"YOU ARE {name_player.upper()}, A {user_chose} LIVING IN CHICAGO.")
    time.sleep(1)
    print("YOU HAVE A PISTOL AND A POLICE BADGE.")


def mystery_start_setting3(user_chose):
    print(f"YOU ARE {name_player.upper()}, A {user_chose} LIVING IN CHICAGO.")
    time.sleep(1)
    print("YOU HAVE A PISTOL AND A POLICE BADGE.")


def fntsy_start():
    pass


start_game()
