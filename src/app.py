from embedchain import App
from api import get_api_key
import os
import streamlit as st
import base64

api_key=get_api_key()
app=App()

st.title("Nifty 50 data")