import pyautogui
import time
import keyboard
import itertools
import pydirectinput
pyautogui.FAILSAFE = True #DON'T CHANGE THIS

len=4 #CHANGE THIS IF NEEDED

def bruteforce(auto_reset=True, reset_after=2): #Change reset_after if needed
    tries=0 #initialised locally. Use if bruteforce has limited attempts to reset the attempts
    print("Waiting for start input(Press SpaceBar)")
    keyboard.wait("space")
    print("Running until the combo is found...")
    x, y = pyautogui.position()
    for combo in itertools.product('0123456789', repeat=len): #add letters if necessary for your case. Check with the documentation for correct usage
        px = pyautogui.pixel(x, y) 
        if px != (80,80,80): #get color of return button or whatever you want to use so that the bruteforce stops after the right code is entered
            print("Pixel changed. Stopping")
            break 

        num=''.join(combo)
        print(f"Current number: {num} \n")
        for digit in num:
            pydirectinput.press(digit)
            time.sleep(0.2)

        if auto_reset:
            tries += 1

        time.sleep(1) #small break

        if auto_reset and tries==reset_after: 
            pyautogui.click()
            pyautogui.moveTo(830,590) # Map these with listener.py
            pyautogui.click()
            pyautogui.moveTo(1089,955)
            pyautogui.click()
            pyautogui.moveTo(835,713)
            pyautogui.click()
            pyautogui.moveTo(848,872)
            tries=0

if __name__ == "__main__":
    bruteforce(auto_reset=True) #Change auto_reset from HERE not the function 
    


