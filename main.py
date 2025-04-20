import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png")

with col2:
    st.title("Aaran")
    content = """ 
    Hi, I am Aaran! I am a Python Programmer. My projects developed using python shall be available in this github repository
    """
    st.info(content)
