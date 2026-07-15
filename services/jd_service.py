from jd_parser import extract_jd_text

from utils.jd_skill_extractor import extract_jd_skills
from utils.skill_matcher import match_skills


def process_job_description(
    jd_text_input,
    jd_file,
    resume_skills
):

    jd_text = ""

    # First Preference → Text Box
    if jd_text_input.strip():

        jd_text = jd_text_input

    # Second Preference → Upload
    elif jd_file is not None:

        jd_text = extract_jd_text(jd_file)

    if not jd_text:

        return (
            "",
            [],
            [],
            [],
            0
        )

    # Extract Skills
    jd_skills = extract_jd_skills(
        jd_text
    )

    # Match Skills
    matched, missing, score = match_skills(
        resume_skills,
        jd_skills
    )

    return (
        jd_text,
        jd_skills,
        matched,
        missing,
        score
    )