import streamlit as st
import time

st.title("Projects")
st.subheader("Loading Projects...")
with st.spinner("Fetching your projects..."):
    time.sleep(5)



st.write("---")

st.subheader("Project 1: Data Analysis")
st.write("Description: Participated in mosquito data analysis ")
st.write("Technologies used: Rstudio")
if st.button("View Project 1"):
    st.write("Link:https://github.com/musalimwakalvin/mosquitodataanalysis")
st.write("---")

st.subheader("Project 2: My portfolio ")
st.write("Description: Developed a responsive website using Pycharm")
st.write("Technologies used:  Streamlit")
if st.button("View Project 2"):
    st.write("Link:https://github.com/musalimwakalvin/myportfolio")
st.write("---")

st.subheader("Project 3: Project 3: Beginner Python Project")
st.write("Description: Created a simple Python program to perform basic arithmetic operations (addition, subtraction, multiplication, division)")
st.write("Technologies used: collab")
if st.button("View Project 3"):
    st.write("Link:https://github.com/kalvinmusalimwa009-spec/Python")
st.write("---")

