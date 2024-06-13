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

    ###### Step 2: Real-Time Transcription with AssemblyAI ######
        
    def start_transcription(self):
      print(f"\nReal-time transcription: ", end="\r\n")
      self.transcriber = aai.RealtimeTranscriber(
          sample_rate=16_000,
          on_data=self.on_data,
          on_error=self.on_error,
          on_open=self.on_open,
          on_close=self.on_close,
      )

      self.transcriber.connect()

      microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_000)
      self.transcriber.stream(microphone_stream)

    def stop_transcription(self):
      if self.transcriber:
          self.transcriber.close()
          self.transcriber = None
      

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        #print("Session ID:", session_opened.session_id)
        return


    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            print(transcript.text)
            self.generate_ai_response(transcript)
        else:
            print(transcript.text, end="\r")


    def on_error(self, error: aai.RealtimeError):
        #print("An error occured:", error)
        return


    def on_close(self):
        #print("Closing Session")
        return
    
    
    

