# Page for groups analysis

import streamlit as st
import EDA
from PIL import Image

# Title for webpage
st.title('Groups information')

# Some info
st.write("* The world cup consists of 8 groups each group has 4 teams")
st.write("* The top 2 teams in each group qualifies for knockout stage")

# Show Groups 
image = Image.open("FIFA-World-Cup-Qatar-2022-Final-groups.webp")
st.image(image, caption='World Cup Groups',width = 500)

# Groups info
st.plotly_chart(EDA.groups_info_goals())

# Box to select Group
st.write("* Choose a group to show more information about it")
x = st.selectbox("Choose Group",('A','B','C','D','E','F','G','H'))

# Show plot 
st.write(EDA.qualify(x))
st.plotly_chart(EDA.group_info_points(x))
st.plotly_chart(EDA.group_info_matches(x))

 