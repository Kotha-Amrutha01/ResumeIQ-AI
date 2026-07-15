import streamlit as st


def upload_section():

    st.markdown("## 📂 Upload Your Files")

    st.write(
        "Upload your Resume and Job Description to analyze ATS compatibility."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="medium")

    # ---------------- Resume ---------------- #

    with col1:

        with st.container(border=True):

            st.markdown("### 📄 Resume")

            uploaded_file = st.file_uploader(
                "Choose your Resume",
                type=["pdf", "docx"],
                help="Supported formats: PDF, DOCX"
            )

    # ---------------- JD ---------------- #

    with col2:

        with st.container(border=True):

            st.markdown("### 💼 Job Description")

            jd_text = st.text_area(
                "Paste Job Description",
                height=170,
                placeholder="Paste the Job Description here..."
            )

            st.markdown(
                "<center><b>OR</b></center>",
                unsafe_allow_html=True
            )

            jd_file = st.file_uploader(
                "Upload Job Description",
                type=["pdf", "docx", "txt"],
                key="jd",
                help="Supported formats: PDF, DOCX, TXT"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        )

    if "analyzed" not in st.session_state:
        st.session_state.analyzed = False

    if analyze:
        st.session_state.analyzed = True

    st.markdown("---")

    return uploaded_file, jd_text, jd_file, analyze