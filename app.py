import os
import json
import io
import streamlit as st

from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel

from model import *

# Config :
# To launch : streamlit run app.py

st.set_page_config(
    page_title="Image universal classifier",
    page_icon="🦉",
)
st.title("🦢 Classify any image ")
st.header("")

with st.expander("ℹ️ - Information on this app", expanded=True):

    st.write(
        """     
-   The *Image universal classifier* allow you to classify any images you want between a chosen list of classes
-   It was built to be easy to use with nominal performance 
	    """
    )

    st.markdown("")


st.header('🦆 Insert the classes')

if not "text_list" in st.session_state:
    st.session_state.text_list = []

def add_classe_callback():
    st.session_state["text_field"] = ""
    st.session_state.text_list.append(text_field)
def clear_classes_callback():
    st.session_state.text_list = []

text_field = st.text_input("Add a classe", key="text_field")

c1, c2, c3 = st.columns([1, 1, 12])

with c1 :
    add_button = st.button('Add', on_click=add_classe_callback)
with c2 :
    clear_button = st.button('Clear', on_click=clear_classes_callback)

st.header("🗺️ Check your list of classes ")
st.write(st.session_state.text_list) 

st.header("📷 Upload your images ")

with st.form(key="my_form"):

    c29, c30, c31 = st.columns([0.08, 6, 0.18])

    with c30:

        files = st.file_uploader(
            "",
            key="1",
            help="",
            accept_multiple_files=True
        )

        if files is None:
            st.info(
                f"""
                    🖼️ Upload your images. Sample to try: [image_of_two_cats.jpg](http://images.cocodataset.org/val2017/000000039769.jpg)
                    """
            )

        submit_button = st.form_submit_button(label="🌌 Classify !")


if not submit_button:
    st.stop()
if submit_button:
    st.markdown("🗿 Show the results :  ")
    # st.image(files)
    for i in range(len(files)):
        st.image(files[i], width=100, caption=classify_image_in_text_file_version(files[i],text_possibilities=st.session_state.text_list))

st.markdown("🌼 Thanks for running me 😊")