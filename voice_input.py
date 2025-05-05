import speech_recognition as sr
import pyaudio 

print("Libraries imported successfully!")

recognizer = sr.Recognizer()
mic = sr.Microphone()
print("Microphone initialized successfully!")   

def listen():
    with mic as source:
        print("[DEBUG]Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        recognizer.pause_threshold = 0.8

        try:
            audio = recognizer.listen(source, timeout=5)
            print("[DEBUG]Audio captured!")
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You: {text}")
            return text
        except sr.WaitTimeoutError:
            print("[DEBUG]Listening timed out.")
            return None
        except sr.UnknownValueError:
            print("[DEBUG]Could not understand.")
            return None
        except sr.RequestError as e:
            print(f"[DEBUG]Speech recognition error: {e}")
            return None



