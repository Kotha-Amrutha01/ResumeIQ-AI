from resume_parser import extract_text_from_pdf, extract_text_from_docx

from utils.resume_extractor import extract_sections
from utils.skill_extractor import extract_skills
from utils.contact_extractor import extract_contact_info


def process_resume(uploaded_file):

    resume_text = ""

    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        resume_text = extract_text_from_docx(uploaded_file)

    sections = extract_sections(resume_text)

    skills = extract_skills(
        sections.get("Skills", [])
    )

    contact = extract_contact_info(
        resume_text
    )

    resume_skills = (
        skills.get("Technical Skills", []) +
        skills.get("Tools", [])
    )

    return (
        resume_text,
        sections,
        skills,
        contact,
        resume_skills
    )