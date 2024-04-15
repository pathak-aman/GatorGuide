import streamlit as st
from navigation import make_sidebar

import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html

make_sidebar()

st.write(
    """
# Patient Guide

"""
)

chat_placeholder = st.empty()

def on_input_change():
    user_input = st.session_state.get("user_input","")
    st.session_state.user_input = ""

    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")


def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]



st.session_state.setdefault(
    'past', []
)

st.session_state.setdefault(
    'generated', []
)


with chat_placeholder.container():
    message("Hi there, I'm a patient guide app", is_user = False)
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(st.session_state['generated'][i], is_user=False, key=f"{i}", allow_html=True)

    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")