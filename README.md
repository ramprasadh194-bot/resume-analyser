# resume-analyser
# 🚀 AI Resume Analyzer & Job Matcher

An AI-powered web application that analyzes resumes against job descriptions and provides a **match score, skill insights, and missing skills** using semantic understanding.

---

## 🔥 Features

* 📄 Upload Resume (PDF / DOCX)
* 🧠 Semantic Matching using AI (Sentence Transformers)
* 📊 Match Score Calculation
* 🧩 Skill Extraction
* ❗ Missing Skills Detection
* 🌐 Full-stack (Flask + Frontend UI)

---

## 🧠 How It Works

1. User uploads a resume
2. Pastes a job description
3. System:

   * Extracts text from resume
   * Identifies skills
   * Uses **AI embeddings** to compare meaning
4. Outputs:

   * Match score (%)
   * Resume skills
   * Job skills
   * Missing skills

---

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **AI/NLP:** Sentence Transformers
* **Libraries:**

  * PyPDF2
  * python-docx
  * scikit-learn
  * torch

---

## 📁 Project Structure

```
resume_analyzer/
│
├── app.py
├── matcher.py
├── resume_parser.py
├── requirements.txt
├── Procfile
└── index.html
```

---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/ramprasadh194-bot/resume-analyser.git
cd resume-analyser

pip install -r requirements.txt
python app.py
```

---

## 🌐 Usage

1. Open frontend (`index.html`)
2. Upload your resume
3. Paste job description
4. Click **Analyze**

---

## 📊 Example Output

```
Match Score: 78%

Resume Skills: Python, SQL
Job Skills: Python, AWS, Docker
Missing Skills: AWS, Docker
```

---

## 🚀 Deployment

* Backend deployed on Render
* Frontend can be hosted on Netlify / Vercel

---

## ⚠️ Notes

* First request may be slow (model loading)
* Free hosting may have cold start delays

---

## 🔮 Future Improvements

* AI resume suggestions (rewrite bullet points)
* Better UI/UX
* Multi-language support
* Real-time job scraping
* ATS compatibility scoring

---

## 👨‍💻 Author

**Ram Prasadh M K**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
