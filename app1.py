import streamlit as st
import nest_asyncio
nest_asyncio.apply()
from ai4free import BLACKBOXAI
import time
nest_asyncio.apply()


# Initialize the AI Provider (No API Key needed!)
ai = BLACKBOXAI(is_conversation=True)

# Page Setup
st.set_page_config(page_title="MoodLens AI", page_icon="✨", layout="wide")

# ... (Keep your previous CSS for Black Background and Animations here) ...

# Logic for transitions
if 'stage' not in st.session_state: st.session_state.stage = 'hi'

if st.session_state.stage == 'hi':
    st.markdown('<div class="fade-in-hi">HI.</div>', unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.stage = 'input'
    st.rerun()

elif st.session_state.stage == 'input':
    st.markdown("<h2 style='text-align: center; color: #00dbde;'>MoodLens AI Pro</h2>", unsafe_allow_html=True)
    user_input = st.text_area("Tell me everything. How are you really feeling?", height=150)

    if st.button("Consult MoodLens AI"):
        if user_input.strip():
            with st.spinner("AI is reading your soul..."):
                # Professional Prompt for higher accuracy
                prompt = f"Analyze this mood deeply: '{user_input}'. Act as a supportive friend."
                
                # Call AI4Free
                response = ai.chat(prompt)
                
                st.write("---")
                st.markdown(f"### {response}")
                st.balloons()
        else:
            st.warning("Please share your thoughts first.")
