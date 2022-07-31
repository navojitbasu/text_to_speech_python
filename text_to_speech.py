from cgitb import text
import pyttsx3

engine = pyttsx3.init()

#Checking the number of voices in our computer
for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

#Creating a function to convert Text to Speech
def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

#Ask the user to enter the speech
text = input("Enter your text now: ")

#Call the function
Speak(text)

