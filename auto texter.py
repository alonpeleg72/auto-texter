from secrets import choice
import webbrowser
import pyautogui
import time
import pyperclip
import pywhatkit
import datetime

def group_messenger():
    groups = { "Yagels": "https://web.whatsapp.com/accept?code=KRIi2ftqjYI7dtuWNL9mBi",
            "year0": "https://web.whatsapp.com/accept?code=DsfyW4SLn59FNsIgpeJc8Y",
            "shutes": "https://web.whatsapp.com/accept?code=BhuaH34bpnLKoF8cmQ2mX1",
            "quotes": "https://web.whatsapp.com/accept?code=HuFgVZG405jB7ZqCOwqKAR",
            "yearA": "https://web.whatsapp.com/accept?code=GezyfprTPOx2KsHPUETP7Z"}

    name = input("Enter the Username of the person you want to text in said group")
    message=input("Enter the message you want to send: ")
    print(f"the groups are: {groups.keys()}")
    webbrowser.open(groups[input("Enter one of the groups")])
    time.sleep(15)
    pyperclip.copy(f"@{name}")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

def person_messenger():
    phone_number = input("Enter the phone number of the person you want to text (with country code, e.g. +1234567890): ")
    message = input("Enter the message you want to send: ")
    pywhatkit.sendwhatmsg(phone_number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, wait_time=15, tab_close=True, close_time=5)

def ANNOYING_TIME():
    choice =  input("do you want to send a message to a group or a person?").lower()
    num_messages = int(input("how much messages do you want to send?"))
    match choice:
        case "group":
            for i in range(num_messages):
                group_messenger()
        case "person":
            for i in range(num_messages):
                person_messenger()

if __name__ == "__main__":
    annoying_time = input("is it annoying time? (yes/no)").lower() == "yes"
    match annoying_time:
        case True:
            ANNOYING_TIME()
        case False:
            if input("soo to a person or group?").lower() == "person":
                person_messenger()
            else:
                group_messenger()