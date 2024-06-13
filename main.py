import assemblyai as aai
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
import ollama
import os
from dotenv import load_dotenv
load_dotenv()

class AI_Assistant:

    def __init__(self):
        aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        self.client = ElevenLabs(
            api_key=os.getenv("ELEVENLABS_API_KEY")
        )

        self.transcriber = None

        self.full_transcript = [
            {"role":"system", "content":"You are a language model called Llama 3 created by Meta, answer the questions being asked in less than 300 characters. Do not bold or asterix anything because this will be passed to a text to speech service."},
        ]
    

