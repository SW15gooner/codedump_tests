import PySimpleGUI as sg
import pyttsx3

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')

layout = [  [sg.Text('What you print will display below:')],
            [sg.Output(size=(50,10), key='-OUTPUT-')],
            [sg.In(key='')],
            [sg.Button('Submit'), sg.Button('Clear'), sg.Button('Exit')]  ]

window = sg.Window('ChatBot', layout)

def speak(text):
        engineio.say(text)
        engineio.runAndWait()
        engineio.setProperty('rate', 130)
        engineio.setProperty('voice',voices[0].id)
        speak("What do you want me to say?")

while True:             # Event Loop
    event, values = window.read()
    print(values)
    speak(values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')
window.close()