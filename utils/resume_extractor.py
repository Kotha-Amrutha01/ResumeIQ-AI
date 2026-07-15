# Mapping different resume headings to standard section names
SECTION_MAP = {
    "Summary": "Summary",
    "Professional Summary": "Summary",
    "Profile": "Summary",

    "Skills": "Skills",
    "Technical Skills": "Skills",
    "Programming Languages": "Skills",

    "Experience": "Experience",
    "Work Experience": "Experience",
    "Professional Experience": "Experience",
    "Employment History": "Experience",

    "Education": "Education",
    "Academic Background": "Education",

    "Projects": "Projects",
    "Academic Projects": "Projects",

    "Certifications": "Certifications",
    "Certificates": "Certifications"
}

def extract_sections(resume_text):

    lines = resume_text.split("\n")

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    sections = {
        "Summary": [],
        "Skills": [],
        "Experience": [],
        "Education": [],
        "Projects": [],
        "Certifications": []
    }

    current_section = None

    for line in cleaned_lines:

        if line in SECTION_MAP:
            current_section = SECTION_MAP[line]

        elif current_section:
            sections[current_section].append(line)

    return sections