import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeAudioInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ...")
        r.pause_threshold = 1  # seconds before sentence is said to be completed
        r.energy_threshold = 300  # to remove background noise
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio)
        print(f"User said :  {query}\n")

    except Exception as e:
        print(e)
        print("Say that again .. ")
        return "None"

    return query


if __name__ == '__main__':
    # speak("Good morning again")
    takeAudioInput()


# from gtts import gTTS
# import os


# To use message txt file and convert into mp3 file
# filehandler = open("test.txt", "r")
# myText = filehandler.read().replace("\n", " ")

# myText = "Text to speech conversion using python"
# language = 'en'
# output = gTTS(text=myText, lang=language, slow=False)
# output.save("out.mp3")
# os.system("start out.mp3")
