import streamlit as st
import whisper
from pytube import YouTube
from pydub import AudioSegment
import pandas as pd
import anthropic
import io
from elevenlabs import generate, set_api_key
import os
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as me
import re

st.title("Youtube Saver")

link = st.text_input("Link to Youtube Video", key="link")

to_mp3 = st.sidebar.checkbox('to_mp3')
    

if st.button("Download!"):
    folder_path = "Videos"
    print(f"downloading from link: {link}")
    model = whisper.load_model("base")
    yt = YouTube(link)

    if yt is not None:
        st.subheader(yt.title)
        temp_name = re.sub('[^A-Za-z0-9\s]+', '', yt.title)
        st.image(yt.thumbnail_url)
        audio_name = st.caption("Streaming from the cloud to your silicon empire...")
        streams = yt.streams.filter()
        filename = streams.first().download(output_path=folder_path)
        if to_mp3:
            audio = me.AudioFileClip(filename)
            audio.write_audiofile(f"{temp_name}.mp3")