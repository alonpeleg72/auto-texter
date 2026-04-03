import webbrowser
import pyautogui
import time
import pyperclip

def messenger(message, name):
    pyautogui.click(1188, 1622)
    if name != None and name != "none":
        pyperclip.copy(f"@{name}")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    
def  person_chat_open():
    phone_number = input("Enter the phone number of the person you want to text (with country code, e.g. +1234567890): ")
    message = input("Enter the message you want to send: ")
    webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_number}")
    return message

def group_chat_open():
    groups = { "yagels": "https://web.whatsapp.com/accept?code=KRIi2ftqjYI7dtuWNL9mBi",
            "year0": "https://web.whatsapp.com/accept?code=DsfyW4SLn59FNsIgpeJc8Y",
            "shutes": "https://web.whatsapp.com/accept?code=BhuaH34bpnLKoF8cmQ2mX1",
            "quotes": "https://web.whatsapp.com/accept?code=HuFgVZG405jB7ZqCOwqKAR",
            "yearA": "https://web.whatsapp.com/accept?code=GezyfprTPOx2KsHPUETP7Z"}
    
    print(f"the groups are: {groups.keys()}")
    selected_group = input("Enter one of the groups: ")
    webbrowser.open(groups[selected_group])

def ANNOYING_TIME():
    choice =  input("do you want to send a message to a group or a person?").lower()
    num_messages = int(input("how much messages do you want to send?"))
    
    match choice:
        case "group":
            message=input("Enter the message you want to send: ")
            name = input("Enter the Username of the person you want to text in said group")
           
            group_chat_open()
            time.sleep(15)
            for i in range(num_messages):
                time.sleep(2)
                messenger(message, name)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
        
        case "person":
            message = person_chat_open()
            time.sleep(10)
            for i in range(num_messages):
                time.sleep(2)
                messenger(message, None)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')

def group_messenger():
    name = input("Enter the Username of the person you want to text in said group")
    message = input("Enter the message you want to send: ")
    group_chat_open()
    time.sleep(15)
    
    messenger(message, name)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

def person_messenger():
    message = person_chat_open()
    time.sleep(12)
    
    messenger(message, None)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

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