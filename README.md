## Resume Reviewer using CrewAI

This is a multi-agent AI system that automates resume screening for a given job description.

## What It Does

- Takes a **Job Description (JD)** as input.
- Takes a **folder of candidate resumes (PDFs)** applying for that job.
- Analyzes how well each resume matches the JD.
- **Ranks** all resumes based on their fitness score.
- Generates two reports:
  - `analysis_report.md`: detailed feedback on each resume.
  - `grading_report.md`: overall rankings and summary.

## Agents Involved

- **Researcher Agent** – Understands the job description in depth.
- **Resume Analyzer Agent** – Reviews each resume and evaluates relevant experience, skills, etc.
- **Grader Agent** – Scores and ranks the resumes based on their fit for the JD.

## How to Use

1. Clone the repo and install dependencies
2. Add your Gemini API key to a `.env` file
3. Place resumes in a folder (e.g., `resumes/`).
4. Add job description in job_description.txt
5. Run


## Built With

- Python
- [CrewAI](https://docs.crewai.com/)
- Gemini LLM
- Serper.dev (for web search)



