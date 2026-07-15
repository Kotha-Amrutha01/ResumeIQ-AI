# 🤖 ResumeIQ AI

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blueviolet)
![License](https://img.shields.io/badge/License-Educational-green)

<div align="center">

### AI-Powered Resume Analyzer using Google Gemini

Analyze your resume against a Job Description, calculate ATS compatibility, identify missing skills, receive AI-powered resume suggestions, and generate a professional PDF report.

</div>

---

# 📌 Overview

ResumeIQ AI is an AI-powered Resume Analyzer developed to help job seekers improve their resumes by comparing them with a Job Description (JD). The application calculates an ATS score, extracts technical skills, identifies missing keywords, provides personalized AI-powered suggestions using Google Gemini, and generates a professional PDF report.

---
# 🌟 Key Highlights

- Modular Project Architecture
- Google Gemini AI Integration
- ATS Score Calculation
- Resume vs Job Description Matching
- Professional PDF Report Generation
- Interactive Streamlit Dashboard

----

# ✨ Features

### 📄 Resume Analysis

- Upload Resume (PDF / DOCX)
- Extract Resume Sections
- Extract Contact Information
- Extract Technical Skills
- Resume Statistics Dashboard

---

### 💼 Job Description Analysis

- Upload or Paste Job Description
- Extract Required Skills
- Compare Resume with JD
- Find Missing Skills

---

### 📊 ATS Dashboard

- ATS Score
- Resume Skills Count
- Job Description Skills Count
- Resume Statistics

---

### 🤖 AI Resume Assistant

Powered by **Google Gemini AI**

Features include:

- ✨ Improve Resume Summary
- 🚀 Improve Project Descriptions
- 🎯 ATS Keyword Suggestions
- 💼 Career Advice
- 🎤 Generate Interview Questions

---

### 📄 Professional PDF Report

Generates a downloadable report containing:

- Candidate Information
- ATS Score
- Resume Skills
- JD Skills
- Matched Skills
- Missing Skills
- AI Suggestions
- Report Generation Time

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Application |
| Google Gemini API | AI Assistant |
| ReportLab | PDF Generation |
| PyPDF2 | PDF Parsing |
| python-docx | DOCX Parsing |
| Pandas | Data Processing |
| NumPy | Data Handling |

---

# 📂 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── assets/
│   └── style.css
│
├── services/
│   ├── ai_service.py
│   ├── jd_service.py
│   ├── pdf_service.py
│   ├── report_services.py
│   └── resume_service.py
│
├── ui/
│   ├── hero.py
│   ├── sidebar.py
│   ├── upload_section.py
│   ├── dashboard.py
│   ├── cards.py
│   └── ai_panel.py
│
├── utils/
│   ├── contact_extractor.py
│   ├── jd_skill_extractor.py
│   ├── resume_extractor.py
│   ├── skill_extractor.py
│   ├── skill_matcher.py
│   ├── ai_suggestions.py
│   └── skills_db.py
│
├── resume_parser.py
└── jd_parser.py
```

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Kotha-Amrutha01/ResumeIQ-AI.git
```

---

### Move into the Project Folder

```bash
cd ResumeIQ-AI
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Create Environment File

Create a file named:

```text
.env
```

Add your Gemini API Key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Run the Application

```bash
streamlit run app.py
```

---

# 📊 Workflow

```text
Upload Resume
       │
       ▼
Resume Parsing
       │
       ▼
Upload Job Description
       │
       ▼
Skill Extraction
       │
       ▼
ATS Score Calculation
       │
       ▼
Matched & Missing Skills
       │
       ▼
AI Resume Suggestions
       │
       ▼
Professional PDF Report
```

---

# 📸 Screenshots

The following screenshots will be added after deployment:

- Home Page
- Resume Upload
- ATS Dashboard
- AI Assistant
- PDF Report

---

# 🎯 Future Enhancements

- Resume Ranking
- AI Cover Letter Generator
- Resume Templates
- Resume Improvement Score
- Multiple Resume Comparison
- Resume Download in DOCX
- LinkedIn Profile Analysis

---

# 👩‍💻 Developer

**Amrutha Kotha**

B.Tech CSE Student | VIT-AP University

Passionate about Artificial Intelligence, Machine Learning, and Full Stack Development.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is created for educational and portfolio purposes.