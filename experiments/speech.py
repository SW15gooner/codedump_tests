import pyttsx3
# import engineio #engineio module is not needed.

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')

while(1):
    def speak(text):
        engineio.say(text)
        engineio.runAndWait()
    engineio.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
    engineio.setProperty('voice',voices[0].id)
    speak("What do you want me to say?")
    phrase = input("--> ")
    if (phrase == "exit"):
        exit(0)

    engineio.setProperty('rate', 180)    # Aquí puedes seleccionar la velocidad de la voz
    engineio.setProperty('voice',voices[1].id)
    speak(phrase)
    print(voices)

