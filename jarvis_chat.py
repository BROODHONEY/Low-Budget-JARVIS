from voice_input import listen
from voice_output import speak
from gpt_response import chat_with_gpt
from ollama_response import chat_with_ollama

def main():
    speak("Jarvis online. How can I assist you today?")    
    while True:
        try:
            query = listen()
            if query:
                if query.lower() in ["exit", "quit", "goodbye"]:
                    speak("Goodbye. See you soon.")
                    break
                response = chat_with_ollama(query)
                speak(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("I'm sorry, I couldn't process your request. Please try again.")

if __name__ == "__main__":
    main()