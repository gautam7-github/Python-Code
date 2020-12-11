import pyautogui
import time

time.sleep(6)
file = open('spam.txt', 'r')
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press('enter')

