import ollama

def chat_with_ollama(prompt, model="llama2"):
    response = ollama.chat(model=model, messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']
