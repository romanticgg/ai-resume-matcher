import json

def load_jobs():
    with open("../data/jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)

def match_resume(resume_text):
    jobs = load_jobs()
    results = []

    resume_text = resume_text.lower()

    for job in jobs:
        matched_skills = []
        missing_skills = []

        for skill in job["skills"]:
            if skill.lower() in resume_text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        total_skills = len(job["skills"])
        score = len(matched_skills)
        match_percentage = int((score / total_skills) * 100) if total_skills > 0 else 0

        if match_percentage >= 75:
            suggestion_key = "strong"
        elif match_percentage >= 40:
            suggestion_key = "moderate"
        else:
            suggestion_key = "low"

        results.append({
            "job": job["title"],
            "score": score,
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "suggestion_key": suggestion_key
        })

    return sorted(results, key=lambda x: x["match_percentage"], reverse=True)


if __name__ == "__main__":
    test_text = "熟悉Python、SQL、数据分析，了解Flask开发和MySQL数据库"
    result = match_resume(test_text)
    print(result)