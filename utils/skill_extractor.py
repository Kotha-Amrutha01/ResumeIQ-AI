import re
from utils.skills_db import KNOWN_SKILLS

# Common Tools
KNOWN_TOOLS = [
    "Git",
    "GitHub",
    "Docker",
    "VS Code",
    "Jupyter",
    "Postman",
    "Power BI",
    "Excel"
]


def extract_skills(skill_section):

    extracted_skills = {
        "Technical Skills": [],
        "Tools": [],
        "Soft Skills": []
    }

    # Convert all skill lines into one string
    text = " ".join(skill_section).lower()

    # Extract Technical Skills
    for skill in KNOWN_SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            extracted_skills["Technical Skills"].append(skill)

    # Extract Tools
    for tool in KNOWN_TOOLS:
        pattern = r"\b" + re.escape(tool.lower()) + r"\b"
        if re.search(pattern, text):
            extracted_skills["Tools"].append(tool)

    # Remove duplicates
    extracted_skills["Technical Skills"] = sorted(
        list(set(extracted_skills["Technical Skills"]))
    )

    extracted_skills["Tools"] = sorted(
        list(set(extracted_skills["Tools"]))
    )

    return extracted_skills