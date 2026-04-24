import streamlit as st
import os

st.set_page_config(page_title="Contact", page_icon="📬")


try:
    style_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
    with open(style_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not load styles: {e}")

st.title("📬 Contact")

st.markdown("""
    <div class="info-card">
        <p>I'm always open to discussing new projects, creative ideas, or opportunities to be part of your visions.</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### ✉️ Send a Message")
    name = st.text_input("Name", placeholder="Your Name")
    email = st.text_input("Email", placeholder="Your Email Address")
    message = st.text_area("Message", placeholder="How can I help you?", height=150)

    if st.button("Send Message"):
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been sent.")
        else:
            st.error("Please fill in all fields before sending.")

with col2:
    st.markdown("### 🌐 Socials")
    st.markdown("""
        <div class="social-container">
            <a href="https://github.com/champagneamatos6-boop" target="_blank" class="social-badge">🐙 GitHub</a>
            <a href="https://www.facebook.com/amatos.champagne" target="_blank" class="social-badge">👥 Facebook</a>
            <a href="mailto:champagneamatos6@gmail.com" class="social-badge">📧 Email Me</a>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("📍 Based in Philippines")
