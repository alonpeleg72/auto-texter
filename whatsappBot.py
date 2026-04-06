import sys
sys.dont_write_bytecode = True
import webbrowser
import pyautogui
pyautogui.PAUSE = 0
import time
import pyperclip
import locator

# the global variables used
GROUPS = { "yagels": "https://web.whatsapp.com/accept?code=KRIi2ftqjYI7dtuWNL9mBi",
            "year0": "https://web.whatsapp.com/accept?code=DsfyW4SLn59FNsIgpeJc8Y",
            "shutes": "https://web.whatsapp.com/accept?code=BhuaH34bpnLKoF8cmQ2mX1",
            "quotes": "https://web.whatsapp.com/accept?code=HuFgVZG405jB7ZqCOwqKAR",
            "yearA": "https://web.whatsapp.com/accept?code=GezyfprTPOx2KsHPUETP7Z"}

STICKERS = {"why yes": r'C:\Users\alonp\documents\degree\year1\CS\WhatsappBot\whatsapp_bot_images\WhyYes.png',
                   "why not": r'C:\Users\alonp\documents\degree\year1\CS\WhatsappBot\whatsapp_bot_images\WhyNot.png'}
TOP_LEFT_X = 1201
TOP_LEFT_Y = 552
TOP_RIGHT_X = 2259
TOP_RIGHT_Y = 556
BOTTOM_LEFT_X = 1194
BOTTOM_LEFT_Y = 1541
BOTTOM_RIGHT_X = 2271
BOTTOM_RIGHT_Y = 1544
STICKER_PANEL_REGION = (TOP_LEFT_X, TOP_LEFT_Y, TOP_RIGHT_X - TOP_LEFT_X, BOTTOM_LEFT_Y - TOP_LEFT_Y)

def messenger(message, name):
    location = locator.locateOnScreen(r'C:\Users\alonp\documents\degree\year1\CS\WhatsappBot\whatsapp_bot_images\TextLine.png', confidence=0.85)
    pyautogui.click(location)
    if name != None and name != "none":
        pyperclip.copy(f"@{name}")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

def stickerman(selected_sticker):
       location_open_emojis = locator.locateOnScreen(r'C:\Users\alonp\documents\degree\year1\CS\WhatsappBot\whatsapp_bot_images\StickerAndEmoji.png', confidence=0.85)
       pyautogui.click(location_open_emojis)
       time.sleep(0.5)
       location_stickers = locator.locateOnScreen(r'C:\Users\alonp\documents\degree\year1\CS\WhatsappBot\whatsapp_bot_images\Stickers.png', confidence=0.85, region=STICKER_PANEL_REGION)
       pyautogui.click(location_stickers)
       time.sleep(0.5)

       location_selected_sticker = locator.locateOnScreen(STICKERS[selected_sticker], confidence=0.85, region=STICKER_PANEL_REGION)
       pyautogui.click(location_selected_sticker)
       time.sleep(0.5)
       pyautogui.press('escape')
       time.sleep(0.3)

def  person_chat_open():
    phone_number = input("Enter the phone number of the person you want to text (with country code, e.g. +1234567890): ")
    message = input("Enter the message you want to send: ")
    webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_number}")
    return message

def group_chat_open():
    print(f"the groups are: {GROUPS.keys()}")
    selected_group = input("Enter one of the groups: ")
    webbrowser.open(GROUPS[selected_group])

def exit_program():
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('enter') #saftey measure to make sure the tab is closed

def ANNOYING_TIME():
    choice =  input("do you want to send a message to a group or a person?").lower()
    num_messages = int(input("how much messages do you want to send?"))
    sticker = input("do you want to send a sticker? (yes/no)").lower()
    
    match choice:
        case "group":
            if (sticker == "yes"): 
                selected_sticker = input(f"the stickers are: {STICKERS.keys()}\nwhich sticker do you want to send?").lower()
                group_chat_open()
                time.sleep(15)
                for i in range(num_messages):
                    time.sleep(0.5)
                    stickerman(selected_sticker)
            else:
                message=input("Enter the message you want to send: ")
                name = input("Enter the Username of the person you want to text in said group")
                group_chat_open()
                time.sleep(15)
                for i in range(num_messages):
                    time.sleep(0.5)
                    messenger(message, name)
            exit_program()

        case "person":
            if (sticker == "yes"):
                selected_sticker = input(f"the stickers are: {STICKERS.keys()}\nwhich sticker do you want to send?").lower()
                person_chat_open()
                time.sleep(15)
                for i in range(num_messages):
                    time.sleep(0.5)
                    stickerman(selected_sticker)
            else:
                message = person_chat_open()
                time.sleep(15)
                for i in range(num_messages):
                    time.sleep(0.5)
                    messenger(message, None)
            exit_program()

def group_messenger():
    name = input("Enter the Username of the person you want to text in said group (none if you dont want to tag anyone): ")
    if (input("do you want to send a sticker? (yes/no)").lower() == "yes"):
        selected_sticker = input(f"the stickers are: {STICKERS.keys()}\nwhich sticker do you want to send?").lower()
        group_chat_open()
        time.sleep(15)
        stickerman(selected_sticker)
    else :    
        message = input("Enter the message you want to send: ")
        group_chat_open()
        time.sleep(15)
    
        messenger(message, name)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('enter')

def person_messenger():
    if (input("do you want to send a sticker? (yes/no)").lower() == "yes"):
        selected_sticker = input(f"the stickers are: {STICKERS.keys()}\nwhich sticker do you want to send?").lower()
        group_chat_open()
        time.sleep(15)
        stickerman(selected_sticker)
    else :
        message = person_chat_open()
        time.sleep(15)
        
        messenger(message, None)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('enter')

if __name__ == "__main__":
    annoying_time = input("is it annoying time? (yes/no)").lower() == "yes"
    match annoying_time:
        case True:
            ANNOYING_TIME()
        case False:
            if input("soo to a person or group?").lower() == "person":
                if (input("do you want to send a sticker? (yes/no)").lower() == "yes"):
                    selected_sticker = input(f"the stickers are: {STICKERS.keys()}\nwhich sticker do you want to send?").lower()
                    person_chat_open()
                    time.sleep(15)
                    stickerman(selected_sticker)
                else:
                    person_messenger()
            else:
                if (input("do you want to send a sticker? (yes/no)").lower() == "yes"):
                    selected_sticker = input(f"the stickers are: {STICKERS.keys()}\nwhich sticker do you want to send?").lower()
                    group_chat_open()
                    time.sleep(15)
                    stickerman(selected_sticker)
                else:
                    group_messenger()