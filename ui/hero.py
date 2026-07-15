import streamlit as st

def hero_section():

    st.markdown("""
<div style="
    text-align:center;
    padding:25px 10px 15px 10px;
">

<h1 style="
    color:#4F46E5;
    font-size:52px;
    font-weight:700;
    margin-bottom:10px;
">
📋 ResumeIQ AI
</h1>

<h3 style="
    color:#6B7280;
    font-size:24px;
    font-weight:500;
    margin-top:0px;
    margin-bottom:12px;
">
Smart ATS + AI Career Assistant
</h3>

<p style="
    color:#4B5563;
    font-size:18px;
    line-height:1.7;
    max-width:850px;
    margin:auto;
">
Analyze your resume against a Job Description, calculate your ATS score,
identify missing skills, receive AI-powered recommendations using Google Gemini,
and generate a professional PDF report — all in one place.
</p>

</div>
""", unsafe_allow_html=True)