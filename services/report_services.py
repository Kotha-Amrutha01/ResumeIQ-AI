from datetime import datetime


def generate_report_data(
    contact,
    score,
    resume_skills,
    jd_skills,
    matched,
    missing,
    suggestions
):

    report = {
        "Name": contact.get("Name", "N/A"),
        "Email": contact.get("Email", "N/A"),
        "Phone": contact.get("Phone", "N/A"),
        "GitHub": contact.get("GitHub", "N/A"),
        "LinkedIn": contact.get("LinkedIn", "N/A"),
        "ATS Score": score,
        "Resume Skills": resume_skills,
        "JD Skills": jd_skills,
        "Matched Skills": matched,
        "Missing Skills": missing,
        "AI Suggestions": suggestions,
        "Generated On": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    return report