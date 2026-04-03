import webbrowser
import pyautogui
import time
import pyperclip

groups = { "Yagels": "https://web.whatsapp.com/accept?code=KRIi2ftqjYI7dtuWNL9mBi",
          "year0": "https://web.whatsapp.com/accept?code=DsfyW4SLn59FNsIgpeJc8Y",
          "shutes": "https://web.whatsapp.com/accept?code=BhuaH34bpnLKoF8cmQ2mX1",
          "quotes": "https://web.whatsapp.com/accept?code=HuFgVZG405jB7ZqCOwqKAR",
          "yearA": "https://web.whatsapp.com/accept?code=GezyfprTPOx2KsHPUETP7Z"}

name = input("Enter the Username of the person you want to text in said group")
webbrowser.open(groups[input("Enter one of the groups")])
time.sleep(15)
pyperclip.copy(f"@{name}")
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')
pyautogui.typewrite(" I'm sending this only using code ;)")
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl', 'w')