def generate_ai_suggestions(score, matched, missing, sections):

    suggestions = []

    # ATS Score Suggestions
    if score < 60:
        suggestions.append(
            "Your resume has a low ATS score. Add more job-specific keywords from the Job Description."
        )

    elif score < 80:
        suggestions.append(
            "Your resume is fairly good. Adding a few missing skills can significantly improve your ATS score."
        )

    else:
        suggestions.append(
            "Excellent ATS score! Your resume matches the Job Description well."
        )

    # Missing Skills
    if missing:
        suggestions.append(
            f"Consider adding these skills (if you genuinely have them): {', '.join(missing)}."
        )

    # Projects
    if len(sections.get("Projects", [])) == 0:
        suggestions.append(
            "Add at least 2–3 projects showcasing your technical skills."
        )

    # Certifications
    if len(sections.get("Certifications", [])) == 0:
        suggestions.append(
            "Include relevant certifications to strengthen your profile."
        )

    # Education
    if len(sections.get("Education", [])) == 0:
        suggestions.append(
            "Include your educational qualifications."
        )

    return suggestions