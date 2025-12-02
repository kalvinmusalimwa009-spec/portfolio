import streamlit as st

st.title("Certificates")
st.write("---")
st.subheader("Project Certificates")
project_certificates = st.file_uploader(
    "Upload your project certificates (PDFs)",
    type=["pdf"],
    accept_multiple_files=True
)

if project_certificates:
    st.write("Uploaded Project Certificates:")
    for cert in project_certificates:
        st.write(cert.name)
st.write("---")

st.subheader("KCSE Certificate")
kcse_cert = st.file_uploader(
    "Upload your KCSE certificate (PDF)")
if kcse_cert is not None:
    st.write("Uploaded KCSE Certificate:", kcse_cert.name)
st.write("---")
