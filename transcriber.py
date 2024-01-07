from openai import OpenAI
from pytube import YouTube
import os
import streamlit as st
import nltk
nltk.download('words')
from nltk.corpus import words
from textstat import flesch_kincaid_grade
import textstat


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

yama = r"C:\Users\lance\Desktop\Programming\Youtuber\1  Japanese Yakuza Documentary 5th Regime Yamaguchi Family.mp3"
eng = r"C:\Users\lance\Desktop\Programming\Youtuber\Chrome Shelled Regios  Ep 03.mp3"
latin = r"C:\Users\lance\Desktop\Programming\Youtuber\Le Chant des Templiers V Antiphona Media vita in morte sumus  Nunc dimittis.mp3"
checkpoint = 5

text = "This is a a a sample text with repeated words. Ever shalt thee complexity and opacity of the communicque"
text2 = """
To date, the hot Jupiter WASP-12 b has been the only planet with confirmed orbital decay. The late F-type host star has been hypothesized to be surrounded by a large structure of circumstellar material evaporated from the planet. We obtained two high-resolution spectral transit time series with CARMENES and extensively searched for absorption signals by the atomic species Na, H, Ca, and He using transmission spectroscopy, thereby covering the He I triplet with high resolution for the first time. We apply SYSREM for atomic line transmission spectroscopy, introduce the technique of signal protection to improve the results for individual absorption lines, and compare the outcomes to those of established methods. No transmission signals were detected and the most stringent upper limits as of yet were derived for the individual indicators. Nonetheless, we found variation in the stellar Halpha and He I lines, the origin of which remains uncertain but is unlikely to be activity. To constrain the enigmatic activity state of WASP-12, we analyzed XMM-Newton X-ray data and found the star to be moderately active at most. We deduced an upper limit for the X-ray luminosity and the irradiating X-ray and extreme ultraviolet (XUV) flux of WASP-12 b. Based on the XUV flux upper limit and the lack of the He I signal, our hydrodynamic models slightly favor a moderately irradiated planet with a thermospheric temperature of <= 12,000 K, and a conservative upper limit of <= 4e12 g/s on the mass-loss rate. Our study does not provide evidence for an extended planetary atmosphere or absorption by circumstellar material close to the planetary orbit.
"""
germantext = """
Um dir eine optimale Website der ZDFmediathek, ZDFheute und ZDFtivi präsentieren zu können, setzen wir Cookies und vergleichbare Techniken ein.
"""
translatedgermantext = """
In order to be able to present you with an optimal ZDFmediathek, ZDFheute and ZDFtivi website, we use cookies and similar technologies.
"""

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

if checkpoint == 3:
  # Example usage
  text = "This is a a a sample text with repeated words."
  word_counts = vocab(text)

  print(f"Word counts: {word_counts}")

def download_video(link, output_folder="Videos"):
    try:
        yt = YouTube(link)
        title = yt.title
        st.subheader(title)
        st.image(yt.thumbnail_url)

        with st.spinner("Downloading..."):
            streams = yt.streams.filter()
            stream = streams.first()  # Or allow user to choose stream
            stream.download(output_path=output_folder)
        st.success("Download complete!")
    except Exception as e:
        st.error(f"Error downloading: {e}")

def grader(text):
   from textstat import flesch_kincaid_grade
   grade = flesch_kincaid_grade(text)
   return grade

if checkpoint == 4:
   grade = grader(germantext)
   print(f"SimpleGerman rating: {grade}")
   grade2 = grader(translatedgermantext)
   print(f"Translated rating: {grade2}")

def vocab_with_cli(text: str) -> list[tuple[str, int, float]]:
    words = text.lower().split()
    word_counts = Counter(words)

    return [(word, count, textstat.coleman_liau_index(word)) for word, count in word_counts.items()]

if checkpoint == 5:
   example = vocab_with_cli(text2)
   print(example)