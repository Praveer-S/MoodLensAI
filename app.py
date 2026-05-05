import streamlit as st
from textblob import TextBlob
import time

# Page setup
st.set_page_config(page_title="MoodLens AI", page_icon="✨", layout="wide")

# Aesthetic Styling (Black Background & Neon Text)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .fade-in-hi {
        font-size: 100px; font-weight: bold; text-align: center;
        margin-top: 15%; animation: fadeInOut 3s forwards;
        background: linear-gradient(to right, #ff00cc, #3333ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .question-text {
        font-size: 50px; text-align: center; margin-top: 10%;
        background: linear-gradient(to right, #00dbde, #fc00ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    @keyframes fadeInOut { 0% { opacity: 0; } 50% { opacity: 1; } 100% { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# State Management for Transitions
if 'stage' not in st.session_state: st.session_state.stage = 'hi'

if st.session_state.stage == 'hi':
    st.markdown('<div class="fade-in-hi">HI.</div>', unsafe_allow_html=True)
    time.sleep(2.5)
    st.session_state.stage = 'question'
    st.rerun()

elif st.session_state.stage == 'question':
    st.markdown('<div class="question-text">Want to know how your mood is?</div>', unsafe_allow_html=True)
    if st.button("Yes, Analyze Me ✨"):
        st.session_state.stage = 'input'
        st.rerun()

elif st.session_state.stage == 'input':
    st.markdown("<h2 style='text-align: center;'>MoodLens AI Analyzer</h2>", unsafe_allow_html=True)
    user_input = st.text_area("How are you feeling?", placeholder="Type here...")
    if st.button("Reveal Mood"):
        score = TextBlob(user_input).sentiment.polarity
        if score > 0.2: st.success("Radiant! 🌟")
        elif score < -0.2: st.error("A bit heavy. 😟")
        else: st.info("Calm & Neutral. 😐")
