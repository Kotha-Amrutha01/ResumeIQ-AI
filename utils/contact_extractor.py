import re


def extract_contact_info(resume_text):

    contact = {
        "Name": "",
        "Email": "",
        "Phone": "",
        "GitHub": "",
        "LinkedIn": ""
    }

    # Name (First non-empty line)
    lines = resume_text.split("\n")

    for line in lines:
        line = line.strip()
        if line:
            contact["Name"] = line
            break

    # Email
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    if email:
        contact["Email"] = email.group()

    # Phone Number
    phone = re.search(
        r"(\+91[- ]?)?[6-9]\d{9}",
        resume_text
    )

    if phone:
        contact["Phone"] = phone.group()

    # GitHub
    github = re.search(
        r"(github\.com/[A-Za-z0-9_-]+)",
        resume_text
    )

    if github:
        contact["GitHub"] = github.group()

    # LinkedIn
    linkedin = re.search(
        r"(linkedin\.com/in/[A-Za-z0-9_-]+)",
        resume_text
    )

    if linkedin:
        contact["LinkedIn"] = linkedin.group()

    return contact