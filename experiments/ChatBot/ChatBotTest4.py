## Popup buttons version
import tkinter as tk
from tkinter import messagebox
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import preprocessors
import os
os.system("")

## start speech
import pyttsx3
import sys

## This and SYS are for Pyinstaller

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
## End

## Colour load

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

## End

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

## stop speech load
## define first popup

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def StopApplication():
    sys.exit()

def StartApplication():
    MsgBox = tk.messagebox.askquestion ('Start ChatBot','The ChatBot is about to start learning\n\nContinue?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        root.command = StopApplication
        
button1 = tk.Button (root, text='Start ChatBot',command=StartApplication,bg='brown',fg='white')
button2 = tk.Button (root, text='Stop ChatBot',command=StopApplication,bg='brown',fg='white')
canvas1.create_window(150, 110, window=button1)
canvas1.create_window(150, 150, window=button2)
  
root.mainloop()

## start language train

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

## Looks for YML language files
corpus_path = 'english/' ## Does not run without english/ path, this is for pyinstaller

## collates the Language YML files
for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)
print("This program runs from a temporary folder and cleans up after itself")

## Popup

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.text = tk.Text(self, wrap="word", height=20)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        engineio.setProperty('rate', 150)
        engineio.setProperty('voice',voices[0].id)
        self.text.insert("end", "Hello You. Do you want to play a game?\n\nI am an AI Learning ChatBot\nI pickup what you say and search a semantics\nDatabase for a response\n")
        speak('Hello You. Do you want to play a game?')
        self.text.insert("end", "\nAsk us a question.")
        speak('Ask us a question.')
        self.text.bind("<Return>", self.process_input)
        self.prompt = ">>> "

        self.insert_prompt()

    def insert_prompt(self):
        # make sure the last line ends with a newline; remember that
        # tkinter guarantees a trailing newline, so we get the
        # character before this trailing newline ('end-1c' gets the
        # trailing newline, 'end-2c' gets the char before that)
        c = self.text.get("end-2c")
        if c != "\n":
            self.text.insert("end", "\n")
        self.text.insert("end", self.prompt, ("prompt",))

        # this mark lets us find the end of the prompt, and thus
        # the beggining of the user input
        self.text.mark_set("end-of-prompt", "end-1c")
        self.text.mark_gravity("end-of-prompt", "left")
        
    def process_input(self, event=None):
        # if there is an event, it happened before the class binding,
        # thus before the newline actually got inserted; we'll
        # do that here, then skip the class binding.
        self.text.insert("end", "\n")
        command = self.text.get("end-of-prompt", "end-1c")
        self.text.insert("end", command)
        engineio.setProperty('rate', 150)
        engineio.setProperty('voice',voices[0].id)
        speak(command)
        reply = bot.get_response(command)
        engineio.setProperty('rate', 150)
        engineio.setProperty('voice',voices[1].id)
        speak(reply)
        self.text.insert("end", reply)
        self.text.see("end")
        self.insert_prompt()

        # this prevents the class binding from firing, since we 
        # inserted the newline in this method
        return "break"

root= tk.Tk()
root.title("AI ChatBot - © Gary Wheller ")
root.wm_geometry("400x400")
app = Application(root).pack(side="top", fill="both", expand=True)
root.wm_attributes("-topmost", 1)
root.focus_force()
root.mainloop()