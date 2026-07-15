import re
from utils.skills_db import KNOWN_SKILLS


def extract_jd_skills(jd_text):

    jd_lower = jd_text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, jd_lower):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))