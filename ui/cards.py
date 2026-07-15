import streamlit as st


def skill_badges(title, skills, color):

    st.markdown(f"### {title}")

    if not skills:
        st.info("No skills found.")
        return

    html = ""

    for skill in skills:

        html += f"""
        <span style="
            display:inline-block;
            background:{color};
            color:white;
            padding:8px 15px;
            margin:6px;
            border-radius:20px;
            font-size:15px;
            font-weight:bold;">
            {skill}
        </span>
        """

    st.markdown(html, unsafe_allow_html=True)