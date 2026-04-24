import streamlit as st
import os

st.set_page_config(page_title="Skills", page_icon="🛠️")


try:
    style_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
    with open(style_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not load styles: {e}")

st.title("🛠️ Skills")

# Helper function for aesthetic skill bars
def skill_bar(name, level):
    st.markdown(f"""
        <div class="skill-card">
            <div class="skill-name">
                <span>{name}</span>
                <span>{level}%</span>
            </div>
            <div class="skill-bar-bg">
                <div style="background-color: #2c5364; width: {level}%; height: 100%; border-radius: 10px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💻 Programming")
    skill_bar("HTML", 85)
    skill_bar("CSS", 80)
    skill_bar("JavaScript", 70)
    skill_bar("Python", 75)

with col2:
    st.markdown("### 🎨 Design")
    skill_bar("Canva", 90)
    skill_bar("UI Design", 60)
    
    st.markdown("### 🛠️ Tools")
    st.markdown("""
        <div style="display: flex; flex-wrap: wrap; gap: 12px;">
            <div style="background: rgba(255,255,255,0.08); padding: 8px 16px; border-radius: 12px; display: flex; align-items: center; gap: 10px; border: 1px solid rgba(255,255,255,0.15);">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="22" style="filter: invert(1);">
                <span style="font-weight: 500;">GitHub</span>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 8px 16px; border-radius: 12px; display: flex; align-items: center; gap: 10px; border: 1px solid rgba(255,255,255,0.15);">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="22">
                <span style="font-weight: 500;">VS Code</span>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 8px 16px; border-radius: 12px; display: flex; align-items: center; gap: 10px; border: 1px solid rgba(255,255,255,0.15);">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-plain.svg" width="22">
                <span style="font-weight: 500;">Streamlit</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("💡 Always learning and expanding my tech stack!")
