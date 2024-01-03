from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
client = OpenAI(api_key=OPENAI_API_KEY)

yama = r"C:\Users\lance\Desktop\Programming\Youtuber\1  Japanese Yakuza Documentary 5th Regime Yamaguchi Family.mp3"
eng = r"C:\Users\lance\Desktop\Programming\Youtuber\Chrome Shelled Regios  Ep 03.mp3"
latin = r"C:\Users\lance\Desktop\Programming\Youtuber\Le Chant des Templiers V Antiphona Media vita in morte sumus  Nunc dimittis.mp3"

audio_file = open(latin, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

print(transcript)

def write_text_to_file(text, filename):
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

write_text_to_file(transcript, "latin")