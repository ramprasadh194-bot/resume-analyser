from sentence_transformers import SentenceTransformer, util

# Load model once (important)
model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS_DB = {
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning",
    "flask", "django", "react", "node",
    "aws", "docker", "kubernetes", "git"
}


def extract_skills(text):
    text = text.lower()
    found = set()

    for skill in SKILLS_DB:
        if skill in text:
            found.add(skill)

    return found


def calculate_match_score(resume_text, job_description):
    # Convert to embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    # Cosine similarity
    similarity = util.cos_sim(resume_embedding, job_embedding)

    return float(similarity[0][0])


def find_missing_skills(resume_skills, job_skills):
    return job_skills - resume_skills

