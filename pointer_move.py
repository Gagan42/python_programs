import webbrowser
import pyautogui 
import keyboard 
import time


webbrowser.open('https://onlinebooking.sand.telangana.gov.in')
print(pyautogui.size()) 
time.sleep(4)
pyautogui.moveTo(490, 370, duration = 1) 
# time.sleep(2)
pyautogui.click()


# It writes the content to output

keyboard.write("8186016238")
time.sleep(0.5)
keyboard.press_and_release('tab')
time.sleep(2)
keyboard.write("kushi1521")
# time.sleep(1) 
keyboard.press_and_release('tab') 

# time.sleep(38)

# pyautogui.moveTo(430, 170, duration = 1) 
# # time.sleep(2)
# pyautogui.click()

# time.sleep(2.75)

# pyautogui.moveTo(850, 255, duration = 1) 
# # time.sleep(2)
# pyautogui.click()


# pyautogui.moveTo(845, 425, duration = 1) 
# # time.sleep(2)
# pyautogui.click()

# pyautogui.moveTo(207, 327, duration = 1) 
# pyautogui.click()
