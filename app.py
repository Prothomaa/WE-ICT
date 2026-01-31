import streamlit as st

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="WE-ICT 2014",
    page_icon="🎓",
    layout="centered"
)

# -----------------------
# Header
# -----------------------
st.image("logo.jpeg", width=160)
st.title("Workshop on Women Empowerment through ICT")
st.subheader("Higher Studies, Research and Career")
st.markdown("**📅 June 7, 2014 | 📍 Dhaka, Bangladesh**")

st.markdown("---")

# -----------------------
# About
# -----------------------
st.header("About the Workshop")
st.write("""
The Workshop on Women Empowerment through ICT (WE-ICT 2014)
aims to provide a forum for researchers, faculty members,
industry professionals, and students to exchange ideas,
experience, and success stories to encourage and motivate
women in computing.
""")

# -----------------------
# Speakers
# -----------------------
st.header("Key Speakers")
st.markdown("""
- **Dr. Mahmuda Naznin** – Associate Professor, CSE, BUET  
- **Dr. Shamsi Tamara Iqbal** – Microsoft Research, USA  
- **Sumaiya Nazeen** – Fulbright Fellow, MIT, USA
""")

# -----------------------
# Schedule
# -----------------------
st.header("Program Schedule")
st.markdown("""
- 08:30 – Entry and Registration  
- 09:00 – Opening Ceremony  
- 09:15 – Chief Guest Speech  
- 10:00 – Keynote & Invited Talks  
- 04:30 – Poster Presentation  
- 05:30 – Award & Closing Ceremony
""")

# -----------------------
# Venue
# -----------------------
st.header("Venue")
st.write("Graduate Complex, Department of CSE, BUET, Dhaka")

# -----------------------
# Flyer (PDF download)
# -----------------------
st.header("Workshop Flyer")

with open("flyer.pdf", "rb") as pdf_file:
    st.download_button(
        label="📄 Download Workshop Flyer (PDF)",
        data=pdf_file,
        file_name="WE-ICT-2014-Flyer.pdf",
        mime="application/pdf"
    )

# -----------------------
# Registration
# -----------------------
st.header("Registration")
st.write("Participation is **FREE**. Please register online.")
st.markdown("[👉 Register Now](https://forms.gle/your_form_link)")

st.markdown("---")
st.caption("Organized by Department of CSE, BUET")
