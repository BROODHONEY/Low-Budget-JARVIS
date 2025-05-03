import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

