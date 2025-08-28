import streamlit as st

from app.services.chat import orchestrator
from app.services.tts import synthesize_tts


st.set_page_config(page_title="Tamizhi BOT", page_icon="🗣️", layout="centered")
st.title("Tamizhi BOT · Tamil–English Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []
if "user_id" not in st.session_state:
    st.session_state.user_id = "web"

with st.sidebar:
    st.header("Settings")
    st.text_input("User ID", key="user_id")
    tts_enabled = st.checkbox("Enable TTS", value=False)

user_message = st.text_input("Type your message:", value="Vanakkam", key="input")
send = st.button("Send")

if send and user_message.strip():
    reply, lang = orchestrator.respond(user_message, user_id=st.session_state.user_id)
    st.session_state.history.append((user_message, reply, lang))

for umsg, rmsg, lang in reversed(st.session_state.history):
    st.markdown(f"**You:** {umsg}")
    st.markdown(f"**Tamizhi BOT ({lang}):** {rmsg}")
    if tts_enabled:
        audio = synthesize_tts(rmsg, lang="ta" if lang in {"ta", "mix"} else "en")
        st.audio(audio, format="audio/mp3")

