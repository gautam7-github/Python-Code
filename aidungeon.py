print("WELCOME TO AI DUNGEON")
print("You are about to enter a world of endless possibilities,")
print("where you can do absolutely anything you can imagine....")
print("ARE YOU READY ? ")

def start_game():
    print("PICK YOUR SETTING : ")

menu_resp = input("YES (y) OR NO (n) : ")
if menu_resp == 'y':
    start_game()
elif menu_resp == 'n':
    print("COWARD")
    print("GO HOME AND CRY")
else:
    print("HEY!!!")
    print("ENTER VALID CHOICE")