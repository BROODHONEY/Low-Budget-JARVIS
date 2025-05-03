import speech_recognition as sr
import pyaudio 

print("Libraries imported successfully!")

recognizer = sr.Recognizer()
mic = sr.Microphone()
print("Microphone initialized successfully!")   

def listen():
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        print("Audio captured!")

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")


