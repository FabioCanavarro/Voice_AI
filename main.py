import speech_recognition as sr
import os

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("You said " + r.recognize_wit(audio,os.environ.get("WIT_API_KEY")))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Wit error; {0}".format(e))
