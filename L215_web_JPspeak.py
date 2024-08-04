import streamlit as st
import gtts

fname='sound.mp3'

inp=st.text_input('テキスト入力：')

if st.button('Speak'):
    gtts.gTTS(inp, lang='jp').save(fname)
    st.audio(fname)
