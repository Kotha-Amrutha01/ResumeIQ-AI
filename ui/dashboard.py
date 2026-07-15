import streamlit as st


def ats_dashboard(score, resume_skills, jd_skills):

    st.markdown("## 📈 ATS Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🎯 ATS Score", f"{score}%")

    with c2:
        st.metric("🛠 Resume Skills", len(resume_skills))

    with c3:
        st.metric("💼 JD Skills", len(jd_skills))

    st.progress(score / 100)


def contact_dashboard(contact):

    st.markdown("## 👤 Contact Information")

    c1, c2 = st.columns(2)

    with c1:
        st.info(f"👤 Name : {contact.get('Name','')}")
        st.info(f"📧 Email : {contact.get('Email','')}")

    with c2:
        st.info(f"📱 Phone : {contact.get('Phone','')}")
        st.info(f"💻 GitHub : {contact.get('GitHub','')}")


def statistics_dashboard(resume_skills, sections):

    st.markdown("## 📊 Resume Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🛠 Skills", len(resume_skills))

    with c2:
        st.metric("📂 Projects", len(sections.get("Projects", [])))

    with c3:
        st.metric("🎓 Education", len(sections.get("Education", [])))

    with c4:
        st.metric("📜 Certifications", len(sections.get("Certifications", [])))


def skills_dashboard(matched, missing):

    left, right = st.columns(2)

    with left:

        st.markdown("## 🟢 Matched Skills")

        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.info("No matched skills found.")

    with right:

        st.markdown("## 🔴 Missing Skills")

        if missing:
            for skill in missing:
                st.error(skill)
        else:
            st.success("No missing skills 🎉")