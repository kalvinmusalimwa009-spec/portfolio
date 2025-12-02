import streamlit as st
from PIL import Image

st.title("Referees")
st.write("---")
col1, col2 = st.columns([1, 3])
with col1:
    referee1_image = Image.open("referee 1.jpg")
    st.image(referee1_image, width=100)
with col2:
    st.subheader("Dr. Jane Nafula")
    st.write("Position: Senior Lecturer")
    st.write("Organization: University of Nairobi")
    st.write("Email: jane.nafula@uon.ac.ke")
st.write("---")

col1, col2 = st.columns([1, 3])
with col1:
    referee2_image = Image.open("referee 2.jpg")
    st.image(referee2_image, width=100)
with col2:
    st.subheader("Mr. John Otieno")
    st.write("Position: Chief Principal ")
    st.write("Organization: St. Mary's Kibabii National School")
    st.write("Email: johnotieno@stmaryskibabii.sc.ke")
st.write("---")

col1, col2 = st.columns([1, 3])
with col1:
    referee3_image = Image.open("referee 3.jpg")
    st.image(referee3_image, width=100)
with col2:
    st.subheader("Ms. Alice Mwende")
    st.write("Position: HeadTeacher")
    st.write("Organization: Lugulu Primary School")
    st.write("Email: alicemwende@luguluprimary.sc.ke")
st.write("---")
col1, col2 = st.columns([1, 3])
with col1:
    referee4_image = Image.open("referee 4.jpg")
    st.image(referee4_image, width=100)
with col2:
    st.subheader("Mr. Fred Nyachomo")
    st.write("Position: Data Analyst")
    st.write("Organization: Nairobi Analytics Ltd.")
    st.write("Email: frednyachomo@nairobianalytics.co.ke")
st.write("---")
