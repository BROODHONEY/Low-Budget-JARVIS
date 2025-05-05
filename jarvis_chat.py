from voice_input import listen
from voice_output import speak
from ollama_response import chat_with_ollama
from gpt_response import chat_with_gpt
from wakeup import listen_for_wake_word
import time
import random

random_on_wake_phrases = ["Sir!", "Yes sir?", "How can I assist you sir?", "At your service sir!", "I am Listening sir!"]
random_off_wake_phrases = ["Goodbye, sir!", "See you later, sir!", "Take care, sir!", "Until next time, sir!", "Farewell, sir!"]
random_thank_you_phrases = ["You're welcome, sir!", "No problem, sir!", "Anytime, sir!", "Glad to help, sir!", "My pleasure, sir!"]

def on_wake_word_detected():
    speak(random.choice(random_on_wake_phrases))  # Greet

    while True:
        try:
            query = listen()
            if query:
                if query.lower() in ["exit", "quit", "goodbye", "bye"]:
                    response = chat_with_ollama(query)
                    break
                response = chat_with_ollama(query)
                speak(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("I'm sorry, I couldn't process your request. Please try again.")
        user_input = listen()

        if not user_input:
            speak("I didn't quite catch that, sir.")
            continue

        user_input = user_input.lower()

        if any(exit_word in user_input for exit_word in ["bye", "exit", "quit", "shutdown"]):
            speak(random.choice(random_off_wake_phrases))
            exit(0)

        elif any(greet in user_input for greet in ["hello", "hi", "hey"]):
            speak("Hello, sir! How can I assist you today?")

        elif any(word in user_input for word in ["nevermind", "nothing", "not anything at the moment"]):
            speak("Alright, sir! If you need anything, just say my name.")
            break

        elif any(word in user_input for word in ["thank you", "thanks"]):
            speak(random.choice(random_thank_you_phrases))
            break

        else:
            response = chat_with_ollama(user_input)
            speak(response)

        user_input = listen()

        if not user_input:
            speak("I didn't quite catch that, sir.")
            continue

        user_input = user_input.lower()

        if any(exit_word in user_input for exit_word in ["bye", "exit", "quit", "shutdown"]):
            speak(random.choice(random_off_wake_phrases))
            exit(0)

        elif any(greet in user_input for greet in ["hello", "hi", "hey"]):
            speak("Hello, sir! How can I assist you today?")

        elif any(word in user_input for word in ["nevermind", "nothing", "not anything at the moment"]):
            speak("Alright, sir! If you need anything, just say my name.")
            break

        elif any(word in user_input for word in ["thank you", "thanks"]):
            speak(random.choice(random_thank_you_phrases))
            break

        else:
            response = chat_with_ollama(user_input)
            speak(response)

if __name__ == "__main__":
    while True:
        print("Jarvis is sleeping. Say 'Jarvis' to wake him up.")
        listen_for_wake_word(on_wake_word_detected)