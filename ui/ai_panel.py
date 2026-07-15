import streamlit as st
from services.ai_service import ask_gemini


def ai_panel(resume_text, jd_text):

    st.markdown("## 🤖 AI Resume Assistant")

    st.write("Select an AI feature to improve your resume.")

    option = st.selectbox(
        "Choose AI Task",
        [
            "Improve Resume Summary",
            "Improve Projects",
            "ATS Keyword Suggestions",
            "Career Advice",
            "Generate Interview Questions"
        ]
    )

    if st.button("✨ Generate AI Response", use_container_width=True):

        with st.spinner("🤖 Gemini is thinking..."):

            if option == "Improve Resume Summary":

                prompt = f"""
You are a professional ATS Resume Expert.

Improve the following resume summary.

Requirements:
- ATS friendly
- Professional
- Concise
- Strong action words
- Around 80-120 words

Resume:

{resume_text}
"""

            elif option == "Improve Projects":

                prompt = f"""
You are an experienced Software Engineering Recruiter.

Rewrite the projects in this resume.

Requirements:
- ATS friendly
- Strong action verbs
- Highlight achievements
- Professional bullet points
- Mention measurable impact whenever possible

Resume:

{resume_text}
"""

            elif option == "ATS Keyword Suggestions":

                prompt = f"""
You are an ATS Resume Analyzer.

Compare the Resume and Job Description.

Resume:

{resume_text}

Job Description:

{jd_text}

Provide:

1. ATS Score Improvement Suggestions
2. Missing Keywords
3. Missing Technical Skills
4. Resume Improvement Tips

Return the answer in bullet points.
"""

            elif option == "Career Advice":

                prompt = f"""
You are an experienced Career Mentor.

Based on the Resume and Job Description, provide:

1. Career Advice
2. Skills to Learn
3. Certifications to Complete
4. Projects to Build
5. Tips to Crack the Interview

Resume:

{resume_text}

Job Description:

{jd_text}
"""

            elif option == "Generate Interview Questions":

                prompt = f"""
You are a Senior Technical Interviewer.

Using the Resume and Job Description below,

Generate:

- 10 Technical Interview Questions
- 5 HR Interview Questions
- Provide a short expected answer for each.

Resume:

{resume_text}

Job Description:

{jd_text}
"""

            response = ask_gemini(prompt)

        st.success("✅ AI Response Generated")

        st.markdown("---")

        st.markdown("### 🤖 Gemini Response")

        st.markdown(
            f"""
<div style="
background-color:#eef7ff;
padding:18px;
border-radius:12px;
border-left:6px solid #4F46E5;
font-size:16px;
line-height:1.7;
">

{response}

</div>
""",
            unsafe_allow_html=True,
        )