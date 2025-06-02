import streamlit as st

# Page config
st.set_page_config(page_title="Job Application Form", page_icon="🧾", layout="centered")

# Styling
st.markdown("""
    <style>
        .main {
            background-color: #f8fcff;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #003366;
            text-align: center;
        }
        label {
            font-weight: bold;
        }
        .footer {
            text-align: center;
            color: gray;
            margin-top: 40px;
            font-size: 14px;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Start main container
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown("<h1>🧾 Job Application Form</h1>", unsafe_allow_html=True)

# Input fields
name = st.text_input("👤 Full Name")
email = st.text_input("📧 Email Address")
phone = st.text_input("📱 Phone Number")
position = st.selectbox("💼 Position Applying For", ["Software Engineer", "Data Analyst", "UI/UX Designer", "Product Manager"])
experience = st.slider("📊 Years of Experience", 0, 30, 1)
cover_letter = st.text_area("📝 Cover Letter", height=150)

# Submit button
if st.button("Submit Application"):
    if name.strip() and email.strip() and phone.strip():
        st.success("✅ Your application has been submitted successfully!")
        st.markdown("### 📄 Application Summary")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Position:** {position}")
        st.write(f"**Experience:** {experience} year(s)")
        st.write(f"**Cover Letter:** {cover_letter if cover_letter.strip() else 'Not provided'}")
    else:
        st.warning("⚠️ Please fill out Name, Email, and Phone Number.")

# Footer with HTTP link
st.markdown("---")
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown('🔗 Visit <a href="https://careers.google.com/jobs/" target="_blank">Google Jobs</a>', unsafe_allow_html=True)
st.markdown("</div></div>", unsafe_allow_html=True)



