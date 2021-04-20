import speech_recognition as sr
import os
import serial
from time import sleep

rec = sr.Recognizer()  # starts voice recognition


def listen():
    with sr.Microphone() as source:  # simplifies to source
        audio = rec.listen(source)  # listens to microphone
        voice = ""  # nothing was said
        try:
            voice = rec.recognize_google(audio)  # uses google for speech-to-text
        except:
            print("WHAT?")  # prints this if nothing is heard
    print("You said: ", voice)  # prints what the microphone heard
    return voice


if __name__ == '__main__':
    ser = serial.Serial('COM4', 9600)   # starts serial com
    sleep(2)    # waits 2 seconds

    while True:
        comm = listen()     # calls function to get what was said
        if comm == 'on':
            ser.write(b'H')     # sends encoded 'H' to serial
        elif comm == 'off':
            ser.write(b'L')     # sends encoded 'H' to serial
    ser.close()     # cleanup
