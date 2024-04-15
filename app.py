import streamlit as st
from time import sleep
from navigation import make_sidebar

# make_sidebar()

st.title("Welcome to GatorGuide")

st.write("Please log in to continue")
st.write('''clinician_username `dr_test`, password `test'
patient_username `dr_test`, password `test`''')

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "test" and password == "test":
        st.session_state.logged_in = True
        st.success("Patient logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/patient.py")
    elif username == "dr_test" and password == "test":
        st.session_state.logged_in = True
        st.success("Clinician logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/clinician.py")
    else:
        st.error("Incorrect username or password!")