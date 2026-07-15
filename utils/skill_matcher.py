def match_skills(resume_skills, jd_skills):

    resume_set = {skill.lower() for skill in resume_skills}
    jd_set = {skill.lower() for skill in jd_skills}

    matched = []
    missing = []

    for skill in jd_skills:

        if skill.lower() in resume_set:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(jd_set) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_set)) * 100)

    return matched, missing, score