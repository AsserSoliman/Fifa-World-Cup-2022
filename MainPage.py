# Main Page for Website

import streamlit as st
import EDA
from PIL import Image

# Title for webpage
st.title('World Cup Qatar Data Analysis')

# Some info
st.write("* This is a website to analyse information from Qatar Football World Cup 2022")
st.write("* The data is provided by kaggle website")
st.write("* Link: https://www.kaggle.com/datasets/swaptr/fifa-world-cup-2022-statistics ")

# Load Data
dt = EDA.load_data()

# Show image
image = Image.open("World-Cup-2022-Blog.jpg")
st.image(image)

# Show qualified teams
image = Image.open("FIFa-world-cup-teams-2022.jpg")
st.image(image,caption='Qualified Teams for World Cup Qatar 2022')

# Show Groups 
image = Image.open("FIFA-World-Cup-Qatar-2022-Final-groups.webp")
st.image(image, caption='World Cup Groups',width = 500)

# Show data
if st.checkbox('Show Data Provided by Kaggle'):
    st.write(dt)

