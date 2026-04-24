import streamlit as st
import os
import base64

st.set_page_config(page_title="Portfolio", page_icon="🏠")


style_path = os.path.join(os.path.dirname(__file__), 'style.css')

try:
    with open(style_path, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not load styles: {e}")


st.markdown('<h1 class="main-title">🏠 Home</h1>', unsafe_allow_html=True)

image_path = os.path.join(os.path.dirname(__file__), "photo.jpg")

if os.path.exists(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    profile_html = f'<img src="data:image/jpeg;base64,{encoded_image}" alt="Profile photo" class="hero-profile-image">'
else:
    profile_html = '<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white;">Photo Not Found</div>'

col1, col2 = st.columns([1, 1.8], gap="medium")

with col1:
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <div class="hero-image-shell">
                <div class="hero-image-glow"></div>
                {profile_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="info-card">
            <p class="hero-eyebrow">Hello, It's Me <span class="wave">👋</span></p>
            <h2 style="color: #ffffff; margin: 0; font-size: 2.2rem;">Champagne Jemaima Amatos</h2>
            <h3 style="margin-top: 0.5rem; margin-bottom: 1rem; color: #4ca1af;">
                And I'm an <span style="color: #e67e22;">Aspiring Web Developer</span>
            </h3>
            <p style="color: #dfe6e9; font-size: 1.1rem; line-height: 1.6;">
                Welcome to my digital space, where I build clean, simple and intuitive designs
                and turn creative ideas into thoughtful digital work.
            </p>
        </div>
    """, unsafe_allow_html=True)