import pyttsx3
engine = pyttsx3.init()
name = input("whats your name?")
engine.say(f"hello ,  {name}" )
engine.say("!welcome to this programme of text to speech conversion using pyttsx3 library of python.")
engine.runAndWait()