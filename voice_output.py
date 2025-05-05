import pyttsx3

def speak(text):
    try:
        print(f"Jarvis: {text}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"[ERROR in speak()]: {e}")
