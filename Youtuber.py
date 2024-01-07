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
import transcriber
import collections


st.title("Youtube Saver")

link = st.text_input("Link to Youtube Video", key="link")

to_mp3 = st.sidebar.checkbox('to_mp3')
to_script = st.sidebar.checkbox('to_script')

    

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
        if to_script:
            audio = me.AudioFileClip(filename)
            audio_file = open(filename, "rb")
            transcript = transcriber.transcribe(audio_file)
            wordcount = transcriber.vocab_with_cli(transcript)
            # Sort the wordcount items by the third element (float value) in decreasing order
            sorted_wordcount = sorted(list(wordcount.items()), key=lambda x: x[2], reverse=True)


            col1, col2 = st.columns(2)

            # Calculate column height based on screen height
            screen_height = 600
            column_height = screen_height // 2

            with col1:
                st.text_area(
                    "",
                    "\n".join([f"{word}: {count}" for word, count in list(wordcount.items())[:len(wordcount)//2]]),
                    height=column_height,
                )

            with col2: 
                st.text_area(
                    "",
                    "\n".join([f"{word}: {count}" for word, count in list(wordcount.items())[len(wordcount)//2:]]),
                    height=column_height,
                )
            st.text_area("Transcript", transcript, height=400)