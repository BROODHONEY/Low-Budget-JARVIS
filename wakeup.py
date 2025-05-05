import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import json
import threading

model = Model("models/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
audio_q = queue.Queue()

def _audio_callback(indata, frames, time_info, status):
    if status:
        print(f"[Audio Status]: {status}")
    audio_q.put(bytes(indata))

def listen_for_wake_word(callback):
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=_audio_callback):
        print("Passive mode: Say 'Jarvis' to activate.")
        while True:
            data = audio_q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").lower()
                if "jarvis" in text:
                    print("[Wakeup Heard]:", text)
                    callback()  # Run Jarvis interaction
                    break  # Return to jarvis_chat.py to re-enter passive mode

        