import pyautogui
import keyboard

print("Press SPACEBAR to map out the exact (X,Y) coordinates of the mouse")
while 1:
    keyboard.wait("space")
    print(pyautogui.position()) #Use for bruteforcer to map out in case if auto-resetting is needed