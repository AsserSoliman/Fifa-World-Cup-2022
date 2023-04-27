# Page for Teams analysis

import streamlit as st
import EDA_Team
from PIL import Image

# Title for webpage
st.title('Teams information')

# Some info
st.write("* The world cup consists of 32 team")
st.write("* Europe(13), Asia(6), Africa(5), North America(4), South America(4)")

# Show qualified teams
image = Image.open("FIFa-world-cup-teams-2022.jpg")
st.image(image,caption='Qualified Teams for World Cup Qatar 2022')

# Box to select team 
teams = EDA_Team.show_unique()
st.write("* Choose a team to show more information about it")
x = st.multiselect("Choose Team or more ",teams)

# Show insights
if x:
    st.plotly_chart(EDA_Team.players(x))