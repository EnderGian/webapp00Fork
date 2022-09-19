# myFirstStreamlitApp.py
  
#import the library
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("AAUUUGH")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("AAAAAUUUUGH")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("augh")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("FALA DERICK HAHAHAHAHAHAHAHAHAHA")

video_file = open('https://youtu.be/3SCBYUE_X1U', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
