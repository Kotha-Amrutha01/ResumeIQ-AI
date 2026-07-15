import streamlit as st
import time
import ui.hero

from services.resume_service import process_resume
from services.jd_service import process_job_description
from utils.ai_suggestions import generate_ai_suggestions
from services.report_services import generate_report_data
from services.pdf_service import generate_pdf
from services.ai_service import ask_gemini

# UI Imports
from ui.sidebar import sidebar
from ui.upload_section import upload_section
from ui.cards import skill_badges
from ui.ai_panel import ai_panel
from ui.dashboard import (
    ats_dashboard,
    contact_dashboard,
    statistics_dashboard
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="📄",
    layout="wide"
)

# Load CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------- RESUME UPLOAD ---------------- #

# Sidebar (if you added it)

sidebar()
#hero_section()
ui.hero.hero_section()

# ==========================================================
#                    INPUT SECTION
# ==========================================================

uploaded_file, jd_text_input, jd_file, analyze = upload_section()

# ---------------- RESUME PROCESSING ---------------- #

resume_text = ""
sections = {}
skills = {}
contact = {}
resume_skills = []

if st.session_state.analyzed:

    if uploaded_file is None:
        st.error("⚠ Please upload your Resume.")
        st.stop()

    if not jd_text_input.strip() and jd_file is None:
        st.error("⚠ Please paste or upload a Job Description.")
        st.stop()

    with st.spinner("🔍 Analyzing Resume..."):
        time.sleep(2)

        (
            resume_text,
            sections,
            skills,
            contact,
            resume_skills
        ) = process_resume(uploaded_file)
    st.success("✅ Resume uploaded successfully!")
    with st.expander("📄 Resume Preview"):
        st.text_area(
            "Resume Content",
            resume_text,
            height=250
        )

    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Resume",
        "📂 Sections",
        "🛠 Skills",
        "👤 Contact"
    ])

    with tab1:
       st.text_area(
          "Resume Content",
           resume_text,
           height=300
        )
    with tab2:
        st.json(sections)
    with tab3:
        skill_badges(
            "🛠 Resume Skills",
            resume_skills,
          "#4F46E5"
        )
    with tab4:
        contact_dashboard(contact)
    statistics_dashboard(
        resume_skills,
        sections
    )

# ---------------- JOB DESCRIPTION PROCESSING ---------------- #

    (
        jd_text,
        jd_skills,
        matched,
        missing,
        score
    ) = process_job_description(
        jd_text_input,
        jd_file,
        resume_skills
    )
    ats_dashboard(
        score,
        resume_skills,
        jd_skills
    )
    st.markdown("## 🎯 Skill Matching")

    left, right = st.columns(2)
    with left:
        skill_badges(
            "🟢 Matched Skills",
            matched,
          "#22c55e"
        )

    with right:

        skill_badges(
            "🔴 Missing Skills",
            missing,
          "#ef4444"
    )

    if jd_text:
      suggestions = generate_ai_suggestions(
            score,
            matched,
            missing,
            sections
        )

      tab5, tab6, tab7, tab8 = st.tabs([
            "💼 Job Description",
            "🛠 JD Skills",
            "🤖 AI Suggestions",
            "✨ AI Assistant"
        ])

      with tab5:
        st.text_area(
            "JD Content",
            jd_text,
            height=300
        )

      with tab6:
        skill_badges(
            "💼 JD Skills",
            jd_skills,
          "#2563eb"
        )

      with tab7:

        st.markdown("## 🤖 AI Suggestions")

        for suggestion in suggestions:
            st.markdown(
                f"""
                <div style="
                    background-color:#eef7ff;
                    padding:12px;
                    border-radius:10px;
                    margin-bottom:10px;
                    border-left:5px solid #4F46E5;">
                    💡 {suggestion}
                </div>
                """,
                unsafe_allow_html=True
            )
      with tab8:
        ai_panel(
            resume_text,
            jd_text
        )

    report = generate_report_data(
        contact,
        score,
        resume_skills,
        jd_skills,
        matched,
        missing,
        suggestions
    )
    pdf_file = generate_pdf(report)
    with open(pdf_file, "rb") as pdf:
       st.download_button(
           label="📄 Download ResumeIQ Report",
           data=pdf,
           file_name="ResumeIQ_Report.pdf",
           mime="application/pdf",
           use_container_width=True
        )
    

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#6B7280;padding:20px;">

<b>ResumeIQ AI</b><br>

AI-Powered Resume Analyzer

<br><br>

Made with ❤️ by <b>Amrutha Kotha</b>

</div>
""", unsafe_allow_html=True)