import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email add")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed!")