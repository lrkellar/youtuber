from openai import OpenAI
import os
#from dotenv import load_dotenv
import streamlit as st
#load_dotenv()

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
client = OpenAI(api_key=st.secrets[OPENAI_API_KEY])

yama = r"C:\Users\lance\Desktop\Programming\Youtuber\1  Japanese Yakuza Documentary 5th Regime Yamaguchi Family.mp3"
eng = r"C:\Users\lance\Desktop\Programming\Youtuber\Chrome Shelled Regios  Ep 03.mp3"
latin = r"C:\Users\lance\Desktop\Programming\Youtuber\Le Chant des Templiers V Antiphona Media vita in morte sumus  Nunc dimittis.mp3"
checkpoint = 1


def transcribe(audio):
  transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio, 
    response_format="text"
  )
  return transcript

if checkpoint == 1:
  audio_file = open(latin, "rb")
  transcript = transcribe(audio_file)

  print(transcript)

def write_text_to_file(text, filename):
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

if checkpoint == 2:
  audio_file = open(latin, "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
  )
  write_text_to_file(transcript, "latin")

from collections import Counter

def vocab(text: str) -> dict:
 """
 Returns a dictionary mapping unique words in the text to their occurrence count.

 Args:
     text: The input string.

 Returns:
     A dictionary where keys are unique words and values are their occurrence counts.
 """
 # Lowercase the text and split it into words.
 words = text.lower().split()

 # Use collections.Counter to count word occurrences.
 word_counts = Counter(words)

 # Return the dictionary of word counts.
 return word_counts

# Example usage
text = "This is a a a sample text with repeated words."
word_counts = vocab(text)

print(f"Word counts: {word_counts}")