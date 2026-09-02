Auto-Texter

A Python desktop automation tool that sends WhatsApp messages and stickers on your behalf, using screen image recognition and simulated keyboard/mouse input. It opens WhatsApp Web, locates UI elements like the text box or the sticker panel, and drives them with PyAutoGUI.

Features
Send a text message to an individual chat or a saved group
Optionally @mention a specific person inside a group chat before sending
Send stickers from a small local sticker library
"Annoying time" mode, which repeats a message or sticker a chosen number of times
Group shortcuts loaded from environment variables, so you don't have to paste WhatsApp group invite links every run
How it works

The script does not use the WhatsApp API. Instead it

Opens web.whatsapp.com (either a direct chat link for a phone number, or a saved group invite link)
Uses locator (a screen image matcher) to find reference screenshots of UI elements such as the text input box, the emoji/sticker button, and specific stickers
Clicks those locations with pyautogui and pastes text with pyperclip

Because it depends on screen coordinates and image templates, it is tied to the screen resolution and WhatsApp Web layout it was built against.

Limitations
Screen coordinates and image templates are specific to the original author's setup and screen resolution. They need to be recreated for any other machine.
WhatsApp Web's layout can change over time, which may break image matching.
The script controls the mouse and keyboard directly, so the WhatsApp Web tab needs to stay in the foreground and undisturbed while it runs.
This project automates the WhatsApp Web UI rather than using an official API, so it should be used carefully and in line with WhatsApp's terms of service.
