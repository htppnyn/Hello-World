import streamlit as st
import pandas as pd

st.title("🎈 Hello World 57! 🎈")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header(
    "Hello! I'm from Thailand. 🚀"
)

st.write(
    "Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.\
Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos."
)

st.subheader("Years")
col1,col2 = st.columns(2)
with col1:
    year = st.slider("Years",min_value=2010,max_value=2025)
with col2:
    st.write("This is year", year)

st.subheader("Pickme and Star")
col3,col4 = st.columns(2)
with col3:
    pickme = st.selectbox("Pick me one...",["a","b"])
with col4:    
    star = st.feedback("stars")

st.subheader("Movie Genre")
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

st.write(f"You selected {genre}")
if genre == 'Comedy':
    img_comedy = st.image("Picture/comedy.jpg", caption="Comedy")
elif genre == 'Drama':
    img_comedy = st.image("Picture/drama.jpg", caption="Drama")
else:
    img_doc = st.image("Picture/documentary.png", caption="Documentary")