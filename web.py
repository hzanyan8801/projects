import streamlit as st
import functionss

todos = functionss.get_todos()

st.title("My todo")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

st.checkbox("Buy grocery")
st.checkbox("Fix the floor")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")