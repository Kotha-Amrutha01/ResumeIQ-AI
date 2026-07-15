import streamlit as st


def sidebar():

    with st.sidebar:

        st.title("📄 ResumeIQ")

        st.markdown("---")

        st.success("ResumeIQ AI")

        st.write("### Features")

        st.write("✅ Resume Parsing")
        st.write("✅ ATS Score")
        st.write("✅ Skill Matching")
        st.write("✅ AI Suggestions")
        st.write("✅ Resume Report")

        st.markdown("---")

        st.info("Version 1.0")