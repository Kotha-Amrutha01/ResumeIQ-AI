import PyPDF2
from docx import Document


def extract_jd_text(uploaded_file):

    filename = uploaded_file.name.lower()

    # PDF
    if filename.endswith(".pdf"):

        reader = PyPDF2.PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    # DOCX
    elif filename.endswith(".docx"):

        doc = Document(uploaded_file)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    # TXT
    elif filename.endswith(".txt"):

        return uploaded_file.read().decode("utf-8")

    return ""