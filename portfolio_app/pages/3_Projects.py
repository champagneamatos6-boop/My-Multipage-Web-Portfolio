import streamlit as st
import os


st.set_page_config(page_title="Projects", page_icon="🚀")

# Injecting the CSS from style.css
try:
    style_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
    with open(style_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not load styles: {e}")

st.title("🚀 Projects")


projects = {
    "📚 StudyMate": "A simple homework tracker that helps students organize their school tasks effectively.",
    "🏠 Female Dormitory Management System": "Designed to manage and organize dormitory operations, including room assignments and resident records, efficiently.",
    "⚡ Bus Data Transfer Demo": "A technical simulation demonstrating how data is transferred across a system bus."
}

st.markdown('<div class="project-grid">', unsafe_allow_html=True)

for name, desc in projects.items():
    st.markdown(f"""
        <div class="project-card">
            <h3>{name}</h3>
            <p>{desc}</p>
        </div>
    """, unsafe_allow_html=True)

   
st.markdown("---")

st.subheader("🏆 Certification & Achievements")

st.markdown('<div class="certificate-gallery">', unsafe_allow_html=True)
cert_col1, cert_col2, cert_col3, cert_col4, cert_col5 = st.columns(5, gap="small")

with cert_col1:
    try:
        st.image("portfolio_app/Images/introduction to cyber security.jpg", use_container_width=True)
        st.caption("Introduction to Cyber Security")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <p> Introduction to Cyber Security</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col2:
    try:
        st.image("portfolio_app/Images/JavaScript for Beginners.jpg", use_container_width=True)
        st.caption("JavaScript for Beginners")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <p>JavaScript for Beginners</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col3:
    try:
        st.image("portfolio_app/Images/Python for Beginners.jpg", use_container_width=True)
        st.caption("Pyhton for Beginners")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <p>Python for Beginners</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col4:
    try:
        st.image("portfolio_app/Images/PythonEssentials1.jpg", use_container_width=True)
        st.caption("Cisco Python Essentials 1")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <p>PythonEssentials1</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col5:
    try:
        st.image("portfolio_app/Images/Web development for beginners.jpg", use_container_width=True)
        st.caption("Web Development for Beginners")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <p>Web development for beginners</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
