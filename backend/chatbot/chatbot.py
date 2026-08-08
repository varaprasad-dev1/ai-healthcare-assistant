import ollama
from .prompts import SYSTEM_PROMPT

def ask_chatbot(message):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":message
            }
        ]
    )

    return response["message"]["content"]