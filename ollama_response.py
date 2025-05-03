import requests


conversation = [
    {"role": "system", "content": "You are Jarvis, a concise, helpful assistant. Keep responses humanlike and under 4 sentences."}
]

def format_conversation(convo):
    system_msg = convo[0]["content"] if convo and convo[0]["role"] == "system" else ""
    prompt = f"{system_msg}\n\n"
    
    for msg in convo[1:]:  # Skip the system prompt
        if msg["role"] == "user":
            prompt += f"{msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"Jarvis: {msg['content']}\n"
    
    prompt += "Jarvis: "
    return prompt



def chat_with_ollama(user_input):
    global conversation

    conversation.append({"role": "user", "content": user_input})

    prompt = format_conversation(conversation)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    assistant_reply = data["response"].strip()

    conversation.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply
