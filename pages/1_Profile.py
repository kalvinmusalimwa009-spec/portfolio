import streamlit as st
from PIL import Image
st.title("Home / About Me")
st.write("---")
st.subheader("Profile Details")
st.write("Full Name: Musalimwa Kalvin")
st.write("Role: Aspiring Data Scientist & Web Developer")
st.write("Location: Kenya")
st.write("Email: kalvinmusalimwa009@email.com")
st.write("---")

col1, col2 = st.columns([1, 2])
with col1:
    profile_image = Image.open("calton.jpg")
    st.image(profile_image, caption="Welcome to my portfolio!")
with col2:
    st.subheader("Hello, I'm Musalimwa Kalvin")
    st.write("""
    I am a passionate developer interested in **Data Science, Web Development, Machine Learning, and AI.  
    Explore my portfolio to learn more about my education, projects, and professional references.
    """)

    st.subheader("Core Values")
    st.write("""
    - Integrity: I always strive to do the right thing.  
    - Innovation: I enjoy solving problems creatively.  
    - Excellence: I aim for high-quality results in every project.
    """)
    st.subheader("Summary")
    st.write(
        "I am dedicated to learning new technologies, building meaningful projects, "
        "and contributing to innovative solutions in the fields of Data Science, AI, and Web Development."
    )
st.subheader("Fun About Me")
st.write(
    "I love coding, solving challenges in Python and R, exploring AI tools, and building mini-projects."
)
st.subheader("Hobbies & Interests")
st.write("- Reading about Data Science, AI, and Machine Learning")
st.write("- Web Development and interactive apps")
st.write("- Listening to music and exploring tech blogs")
st.subheader("Motivational Quote")
st.write(
    "\"Success is not final, failure is not fatal: It is the courage to continue that counts.\" - Winston Churchill"
)
