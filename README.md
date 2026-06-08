# AI-Scout: AI-Powered Internship Discovery & Ranking System (v1.0.0)

AI-Scout is an end-to-end backend system that automates internship discovery by scraping real job postings and ranking them using machine learning techniques.

The goal is to reduce manual effort in finding relevant opportunities and provide data-driven matching between a candidate profile and available job listings.

---

## 🏗️ System Architecture

The system is divided into two core components:

### 1. Data Ingestion Service (FastAPI)
- Built using FastAPI and Uvicorn
- Scrapes internship/job postings from company websites
- Extracts job-related information using BeautifulSoup
- Stores structured data into an SQLite database using SQLAlchemy ORM

### 2. Machine Learning Ranking Engine
- Reads stored job data from the database
- Converts text into numerical vectors using TF-IDF
- Uses Cosine Similarity to compare candidate profile with job descriptions
- Generates match scores for ranking opportunities

---

## 🎯 Key Features

- Automated job scraping system
- Structured data storage (SQLite)
- AI-based ranking of opportunities
- REST API for execution and data retrieval
- Dockerized deployment for portability
- Real-world job matching system

---

## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Scikit-learn (TF-IDF, Cosine Similarity)
- Pandas, NumPy
- Docker & Docker Compose

---

## 🚀 How to Run

### 🔹 Using Docker (Recommended)

```bash
docker-compose up --build
```

Then open:
http://127.0.0.1:8000/docs

🔹 Local Setup (Without Docker)

python -m venv venv
# On Windows:
venv\Scripts\activate 

pip install -r requirements.txt
uvicorn app:app --reload


Then open:
http://127.0.0.1:8000/docs

📡 API Endpoints

- POST /scout/run → Starts scraping + ML ranking pipeline

- GET /matches → Returns ranked job opportunities

- /docs → Swagger UI for testing APIs

📊 How It Works

User triggers /scout/run

System scrapes internship/job websites

Extracts skills and job descriptions

Stores data in SQLite database

TF-IDF converts text into vectors

Cosine similarity compares jobs with user profile

Jobs are ranked by match score

Results are returned via API

📈 Example Output

Higher score → better match with candidate profile

Lower score → less relevant opportunity

Example:

- CloudFactory   → 15.79%
- LF Technology  → 11.56%
- Logpoint       → 0.00%


🔮 Future Improvements

Replace TF-IDF with embeddings (Sentence Transformers / BERT)

Improve scraping reliability and anti-bot handling

Add feedback-based learning system

Deploy to cloud (Azure / AWS)

Add frontend dashboard for visualization

Improve ranking personalization

## 🌐 Live Usage (Optional Enhancement)

After running the system, users can access:
- API testing via Swagger UI
- Real-time job ranking results via `/matches`

👨‍💻 Author

Built as a personal AI engineering project exploring:

Machine learning pipelines

Backend system design

Web scraping systems

Practical AI applications for career discovery