from openai import OpenAI
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
client = OpenAI(api_key="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")

yama = r"C:\Users\lance\Desktop\Programming\Youtuber\1  Japanese Yakuza Documentary 5th Regime Yamaguchi Family.mp3"
eng = r"C:\Users\lance\Desktop\Programming\Youtuber\Chrome Shelled Regios  Ep 03.mp3"

audio_file = open(yama, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

print(transcript)

def write_text_to_file(text, filename):
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

write_text_to_file(transcript, "Yamaguchi")