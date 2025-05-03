import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# List to keep track of conversation history
conversation_history = [
    {"role": "system", "content": "You are Jarvis, a helpful assistant."}
]

def chat_with_gpt(prompt):
    try:
        if not api_key:
            return "API key is missing. Please check your .env file."
        
        # Add the user's message to the conversation history
        conversation_history.append({"role": "user", "content": prompt})

        # Get a response from the model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )

        # Get the assistant's response
        assistant_response = response.choices[0].message.content.strip()

        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": assistant_response})

        return assistant_response

    except Exception as e:
        return f"I'm sorry, I couldn't connect to the server. Reason: {e}"
