import streamlit as st
st.title("Contact ")
st.write("Feel free to reach out via email or social media.")
st.write("Email: kalvinmusalimwa009@email.com")
st.write("LinkedIn:https://www.linkedin.com/in/kalvin-musalimwa-6233b2395/")
st.write("GitHub: https://github.com/kalvinmusalimwa009-spec")
st.write("Phone no: 0795280980")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")
if st.button("Send"):
    st.success("Thank you! Your message has been sent.")
