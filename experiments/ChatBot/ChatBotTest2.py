 #!/usr/bin/python3
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import preprocessors
import os
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.wm_attributes("-topmost", 1)
ROOT.focus_force()
ROOT.withdraw()

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.YELLOW + "Gary Wheller - ChatBot")

## start speech
import pyttsx3
import sys

## This and SYS are for Pyinstaller
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
## End

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')

def speak(text):
    engineio.say(text)
    engineio.runAndWait()
## stop speech load

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

## Looks for YML language files
corpus_path = 'english/' ## Does not run without english/ path, this is for pyinstaller

## collates the Language YML files
for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

engineio.setProperty('rate', 130)
engineio.setProperty('voice',voices[0].id)
print('Hello You. Do you want to play a game?')
speak('Hello You. Do you want to play a game?')
print('I am an AI based, learning ChatBot')
speak('I am an AI based, learning ChatBot')
print('I listen to what you say, and my friend learns the best response')
speak('I listen to what you say, and my friend learns the best response')
print('She speaks gibberish for a while. bare with us')
speak('She speaks gibberish for a while. bare with us')
print(style.RED + 'Ask a question. Say Bye to leave')
speak('Ask a question. SAy Bye to leave')

while True:
    message = simpledialog.askstring(title="ChatBot", prompt="Ask us something:")
    print(message)
    engineio.setProperty('rate', 130)
    engineio.setProperty('voice',voices[0].id)
    speak(message)
    if message.strip() == 'Bye':
        print(style.YELLOW + 'ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        engineio.setProperty('rate', 180)
        engineio.setProperty('voice',voices[1].id)
        speak(reply)
        print(style.WHITE + 'ChatBot:', reply)
