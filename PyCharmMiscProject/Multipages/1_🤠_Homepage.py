import streamlit as st

st.set_page_config(
    page_title = 'Homepage',
)

# Introduction
st.title('Homepage')
st.subheader('What is this project about?')
st.write('This is my very first Python project for data analysis, and the aim for this project is to deepen '
         'my understanding for Python and its various uses, as well as making use of its many libraries to create '
         'data dashboards.')

# Explain Each Page
st.subheader('🗳️ GE2025 Results')
st.write('This page displays the following:\n- Elected party by Constituency'
         '\n- Vote share + Percentage bar'
         '\n- Hover text displaying Constituency name'
         '\n- Basic numerical election data\n')
st.write("Note 1: *** Due to limitations with the Streamlit library, I am unable to customize the percentage bar colour"
         "without using raw HTML. I don't wanna risk anything, so the progress bar will remain blue regardless for all"
         " parties. ***")
st.write('Note 2: *** When first loading this page, you might sometimes find that the Percentage bar would load'
         ' at the bottom of the page, and you would have to scroll to access the bar. If so, simply reload the page.***')

st.subheader('📊 Basic Metrics')
st.write('This page displays the following:\n- Metric Data of the election'
         '\n- Piecharts using matplotlib')

# Reflections
st.subheader('Page Creation Process')
st.write('I first started with the GE2025 Results Page. Initially, I relied a fair bit on ChatGPT for learning and troubleshooting '
         'as I was very new to Python in the beginning. \n\nOverall, I made an effort to use ChatGPT whenever I am stuck on a feature by '
         'using the 40/60 rule. This meant that 40% of my time will be used to ask ChatGPT, and the remaining 60% of my time will be used '
         'creating and self-troubleshooting basic programs with whatever I have learned from ChatGPT.\nThrough this project, I have learnt a few valuable '
         'fundamentals of Python & Programming etiquette:')
st.subheader('1. Hard skills learnt')
st.write('- Python code etiquette for easier reading/troubleshooting'
         '\n- Various Python libraries like Streamlit, Folium, Pandas, Branca'
         '\n- Python arrays, dictionaries and how to extract & display index (very useful for this project)'
         '\n- CSV data cleanup and organization (underestimated how much time it took for this haha)'
         '\n- Deducing structured and unstructured data (Elected Party in each Constituency vs Determining '
         'which party contest in a Constituency)'
         '\n- Exploring geospatial datasets using Folium-Leaflet'
         '\n- Types of data visualization (Metrics, Piecharts, Categorical geospatial data)'
         '\n- Dashboard creation'
         '\n- Brush up HTML + CSS and embedding using Branca Element')
st.subheader('2. Soft skills learnt')
st.write('\n- Time Management'
         '\n- Project management and planning'
         '\n- Being more curious'
         '\n- Creativity'
         '\n- Research and self-driven learning')

st.write('Project started on 13 May 2025 by Timothy.')