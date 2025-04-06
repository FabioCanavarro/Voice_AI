import speech_recognition as sr
import os

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print(r.recognize_wit(audio,os.environ.get("WIT_API_KEY")))
except E:
    print("ERROR",e)
