# AI Resume Matcher

A bilingual web application for resume analysis and job matching.  
This project supports **Chinese/English interface switching** and matches resume text with suitable technical roles based on extracted skills.

## Features

- Chinese / English UI switching
- Resume text input and job matching
- Ranked job recommendations
- Match percentage calculation
- Matched skills and missing skills analysis
- Improvement suggestions for each role
- Multiple technical job categories supported

## Demo Preview

### Chinese Interface
![Chinese Home](screenshots/home-zh.png)

### Chinese Matching Result
![Chinese Result](screenshots/result-zh.png)

### English Matching Result
![English Result](screenshots/result-en.png)

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Data:** JSON
- **Other:** spaCy, scikit-learn

## Project Structure

```text
resume-matcher/
├── backend/
│   ├── app.py
│   └── analyzer.py
├── data/
│   └── jobs.json
├── frontend/
│   └── index.html
├── screenshots/
│   ├── home-zh.png
│   ├── result-zh.png
│   └── result-en.png
├── requirements.txt
├── .gitignore
└── README.md