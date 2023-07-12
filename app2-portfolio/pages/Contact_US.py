import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email add")
    raw_message = st.text_area("Your message")
    #message = message + "\n" + user_email
    message = f"""\
Subject: New email from {user_email}

from: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully")