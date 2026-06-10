import pandas as pd
from sentence_transformers import SentenceTransformer, util
import PyPDF2

model = SentenceTransformer('all-MiniLM-L6-v2')

ROLE_SKILLS = {
    "Data Scientist": ["python", "machine learning", "pandas", "numpy"],
    "ML Engineer": ["deep learning", "tensorflow", "python"],
    "Web Developer": ["html", "css", "javascript"],
    "Finance Analyst": ["excel", "finance", "analysis"],
    "HR Manager": ["communication", "recruitment"],
    "Marketing Executive": ["marketing", "seo", "sales"]
}

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.lower()
    else:
        return str(file.read(), "utf-8").lower()

def process_resumes(files, role):
    job_skills = ROLE_SKILLS.get(role, [])

    job_text = " ".join(job_skills)
    job_embedding = model.encode(job_text, convert_to_tensor=True)

    results = []

    for file in files:
        text = extract_text(file)

        resume_embedding = model.encode(text, convert_to_tensor=True)
        score = util.cos_sim(job_embedding, resume_embedding).item()

        matched = [s for s in job_skills if s in text]
        missing = list(set(job_skills) - set(matched))

        match_percentage = (len(matched) / len(job_skills)) * 100 if job_skills else 0

        results.append({
            "resume_file": file.name,
            "bert_match_score": score,
            "match_percentage": match_percentage,
            "matched_skills": matched,
            "missing_skills": missing,
            "recommendation": "Selected" if match_percentage > 40 else "Rejected",
            "explanation": f"Matched {len(matched)} skills, missing {len(missing)}"
        })

    df = pd.DataFrame(results)
    return df.sort_values(by="match_percentage", ascending=False)