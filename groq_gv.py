import os
from dotenv import load_dotenv
from groq import Groq
import json

class Bot:
    def __init__(self):
        load_dotenv()
        self.language = "en"
        with open("./languages.json", "r", encoding = "utf-8") as f:
            self.lanugauges = json.load(f)
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key = self.api_key)
        self.conversation_histories = []
        self.model = "llama-3.3-70b-versatile" # default
        self.models = { # https://console.groq.com/docs/models
            "text": ["gemma2-9b-it", "llama-3.3-70b-versatile", "llama-guard-3-8b", "llama3-70b-8192", "llama3-8b-8192"],
            "voice": ["distil-whisper-large-v3-en", "whisper-large-v3", "whisper-large-v3-turbo"]
        }
    
    def set_model(self, model:str = "llama-3.3-70b-versatile"):
        self.model = model
    
    def reset(self):
        self.conversation_histories = []
    
    def set_inputs(self, role:str, content:str):
        self.conversation_histories.append({"role": role, "content": content})

    def get_response(self):
        return self.client.chat.completions.create(messages = self.conversation_histories, model = self.model)