import streamlit as st
from PIL import Image
import pandas as pd
# PAGE CONFIG

st.set_page_config(
    page_title="Musalimwa Charity",
    page_icon="❤️",
    layout="wide"
)


# BACKGROUND IMAGE (CSS)

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://images.unsplash.com/photo-1509099836639-18ba1795216d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
# SIDEBAR NAVIGATION
st.sidebar.title("Navigation")

pages = [
    "Home", "About", "Programs", "Volunteer", "Impact",
    "Donate", "Donor List", "Vision & Mission",
    "Team", "Testimonials", "FAQ", "Contact"
]

page = st.sidebar.radio("Go to Page:", pages)
# HOME PAGE
if page == "Home":
    st.title("❤️ Musalimwa Charity")
    st.subheader("Helping Communities. Changing Lives.")

    st.write("---")
    st.write("### ⭐ Quick Impact Highlights")

    col1, col2, col3 = st.columns(3)
    col1.metric("Meals Provided", "14,200+", "+300 this week")
    col2.metric("Clean Water Access", "5,100+", "+120 this week")
    col3.metric("Students Sponsored", "350+", "+9 this month")

    st.success("✨ Scroll through the sidebar to explore all pages!")
# ABOUT PAGE
elif page == "About":
    st.header("About Us")
    st.write("""
    Musalimwa Charity is dedicated to improving lives through food relief,
    clean water, education support, and community empowerment.
    """)
# PROGRAMS PAGE
elif page == "Programs":
    st.header("Our Programs")

    gallery_images = {
        "Food Support": "C:/Users/Admin/Downloads/food.jpg",
        "Clean Water": "C:/Users/Admin/Downloads/water.jpg",
        "Education Help": "C:/Users/Admin/Downloads/volunteer.jpg"
    }

    selected = st.selectbox("Select Program", gallery_images.keys())
    st.image(gallery_images[selected], use_column_width=True)
# VOLUNTEER PAGE
elif page == "Volunteer":
    st.header("Volunteer With Us")
    st.write("""
    Be part of the change. Volunteer in food drives, teaching, water projects, 
    or community outreach.
    """)

    name = st.text_input("Full Name")
    skill = st.text_input("Your Skills")
    days = st.multiselect("Available Days", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
    btn = st.button("Submit Application")

    if btn:
        st.success("🎉 Thank you! Our team will contact you soon.")

# IMPACT PAGE
elif page == "Impact":
    st.header("Our Impact")

    data = pd.DataFrame({
        "Category": ["Food", "Water", "Education", "Shelter"],
        "People Helped": [14200, 5100, 350, 1200]
    })

    st.bar_chart(data.set_index("Category"))
    st.caption("📊 Updated Weekly")

# DONATE PAGE
elif page == "Donate":
    st.header("Make a Donation")

    with st.form("donate_form"):
        donor = st.text_input("Name")
        amount = st.slider("Amount (Ksh.)", 1, 300)
        send = st.form_submit_button("Donate ❤️")

        if send:
            st.balloons()
            st.success(f"Thank you {donor} for donating Ksh{amount} ❤️")

# DONOR LIST PAGE
elif page == "Donor List":
    st.header("Recent Donors")

    donors = pd.DataFrame({
        "Name": ["Mary A.", "Brian K.", "Joy L.", "Sammy T."],
        "Amount": ["220", "Sh.850", "Sh.1000", "Sh.100"]
    })

    st.table(donors)


# VISION & MISSION

elif page == "Vision & Mission":
    st.header("Our Vision & Mission")

    st.write("""
    **Vision:** A world where every child has access to food, water, and education.  
    **Mission:** To empower communities through sustainable development.
    """)


# TEAM PAGE
st.set_page_config(page_title="Our Team", layout="wide")

st.title("Meet Our Team")
st.write("These are the amazing people working behind Musalimwa Charity.")
st.write("---")

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Our Team", page_icon="👥")

st.header("Meet Our Team")
st.write("----")

# ---- TEAM DATA (EDIT HERE) ----
team_members = [
    {
        "name": "Musalimwa Kalvin",
        "role": "Founder & Director",
        "img": "C:/Users/Admin/Downloads/tue good son.jpg"
    },
    {
        "name": "Sarah Makena",
        "role": "Project Manager",
        "img": "C:/Users/Admin/Downloads/referee 1.jpg"
    },
    {
        "name": "James Otieno",
        "role": "Field Officer",
        "img": "C:/Users/Admin/Downloads/referee 4.jpg"
    },
    {
        "name": "Grace Njeri",
        "role": "Community Coordinator",
        "img": "C:/Users/Admin/Downloads/black son.jpg"
    }
]

# ---- DISPLAY TEAM IN GRID ----
cols = st.columns(2)  # Two columns

for index, member in enumerate(team_members):
    with cols[index % 2]:  # Automatically switches between left & right column
        st.write("----")

        # Load and show image
        try:
            img = Image.open(member["img"])
            st.image(img, width=220)
        except:
            st.error(f"Image not found: {member['img']}")

        # Show member details
        st.subheader(member["name"])
        st.write(f"**Role:** {member['role']}")

st.write("----")
st.caption("© 2025 Musalimwa Charity ")


#testimonials
st.set_page_config(page_title="Testimonials", page_icon="🗣")

st.header("What People Say")
st.write("---")

st.info("“This charity changed my entire community — God bless them!” – Mama Achieng")
st.success("“My children are now back in school thanks to Musalimwa Charity.” – Peter K.")
st.warning("“The clean water project saved many families from disease.” – Fatuma M.")

st.write("---")
st.caption("© 2025 Musalimwa Charity ")


# FAQ PAGE

st.set_page_config(page_title="FAQ", page_icon="❓")

st.header("Frequently Asked Questions")
st.write("---")

with st.expander("How can I volunteer?"):
    st.write("Go to the Volunteer page and fill the form.")

with st.expander("Where does my donation go?"):
    st.write("To food support, water projects, and education programs.")

with st.expander("Is this organization registered?"):
    st.write("Yes, fully licensed and compliant in Kenya.")

st.write("---")
st.caption("© 2025 Musalimwa Charity ")


# FOOTER
st.write("---")
st.caption("© 2025 Musalimwa Charity")

