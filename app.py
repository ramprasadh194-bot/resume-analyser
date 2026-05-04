from flask import Flask, request, jsonify
from resume_parser import extract_text_from_file
from matcher import calculate_match_score, extract_skills, find_missing_skills
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Resume Analyzer API Running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        if "resume" not in request.files:
            return jsonify({"error": "No resume file uploaded"})

        file = request.files["resume"]
        job_description = request.form.get("job_description", "")

        # Extract text
        resume_text = extract_text_from_file(file)

        # Extract skills
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        # Match score
        score = calculate_match_score(resume_text, job_description)

        # Missing skills
        missing = find_missing_skills(resume_skills, job_skills)

        return jsonify({
            "match_score": round(score * 100, 2),
            "resume_skills": list(resume_skills),
            "job_skills": list(job_skills),
            "missing_skills": list(missing)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

