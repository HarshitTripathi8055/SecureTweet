import streamlit as st
from PIL import Image

hide_menu = """ 
<style>
#MainMenu{
    visibility:hidden;
    background-color: #1c1c1c;
    color: #ffffff;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')


st.set_page_config(page_title = "SecureTweet", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.markdown("<h1 style='text-align: center; font-size: 24px;'>SecureTweet - Defend against cyberbullying in the Twitterverse</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2023 | SecureTweet </h1>", unsafe_allow_html=True)

st.image(image , use_column_width=True)
