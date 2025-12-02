import streamlit
import streamlit as st
from streamlit import select_slider

st.title("My Website")
st.header("Test Header")
st.subheader("Test Subheader")
st.caption("The quick brown fox jumps over the lazy ")
st.write("Hello world")
st.write("something else")
st.code("""st.title("My Website")
st.header("Test Header")
st.subheader("Test Subheader")
st.caption("The quick brown fox jumps over the lazy ")
st.write("Hello world")
st.write("something else")
""")
st.divider()
st.subheader("Test subheader")
st.divider()

st.metric("Rainfall mm", 1200,"10%")
st.metric("temperature",20,-4)

user_feedback=st.feedback()
if user_feedback==1:
    st.write("Thank You for you positive feedback")
elif user_feedback==0:
    st.write("Sorry you did not like our services")
user_stars=st.feedback("stars")
if user_stars==0:
    st.write("1 star")
elif user_stars==1:
    st.write("2 stars")
elif user_stars==2:
    st.write("3 stars")
elif user_stars==3:
    st.write("4 stars")
elif user_stars==4:
    st.write("5 stars")
user_check = st.checkbox("I agree")
if user_check:
    st.write("Thanyou for agreeing to our terms")
st.toggle("Dark Mode")
gender = st.radio("select your gender",["Male","Female","Prefer not to say"])

st.select_slider("select the size you wear for clothes",["x","xx","xl","XXL","XXXL"])

st.number_input("Enter your age",min_value=0,max_value=100,value=30)
st.date_input("select your preferred date for the appointment")
st.time_input("select time for the appointment")