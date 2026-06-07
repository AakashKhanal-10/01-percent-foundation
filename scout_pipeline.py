import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#1 Connection to our livedatabase
connection = sqlite3.connect('scout_memory.db')
cursor = connection.cursor()

print("Fetching job records from database...")
# Pulling the ID, company, and the text keywords from the jobs table
cursor.execute("SELECT id, company, keywords_found FROM job_matches")
rows=cursor.fetchall()

if not rows:
    print(" Your database is currently empty. Run your scraper or injector first!")
    connection.close()
    exit()
#2 Extrating text strings for our TF-IDF machine
# This replaces our 'sample_jobs' list from yesterday with real DB data!


# DEFINING YOUR PERSONAL PROFILE ANCHOR

my_profile = """
Aakash Khanal. Student and Data Science Intern focused on  Artificial Intelligence.
Core Technical Skills: Python, Pandas, NumPy, Scikit-Learn, BeautifulSoup.
Tools and Infrastructure: Docker containers, Git, Bash, environment configuration, system design, API integration.
Key Completed Projects: Built a containerized AI-Scout scraping pipeline. Developed a Student Performance Prediction system utilizing machine learning models.
"""


db_job_texts = [row[2] for row in rows] # This is the bridge between your database and the machine learning part. It takes the 'keywords' column from each job record and creates a list of text strings that the TF-IDF vectorizer can learn from.
all_texts = [my_profile] + db_job_texts # Combine your profile with the job texts to create a comprehensive dataset for the machine learning model to learn from.
job_labels=[f"Job {row[0]}: {row[1]}" for row in rows] # To label rows in Pandas


# 3. Initialize your text-to-number machine
vectorizer = TfidfVectorizer(stop_words='english')
#4 Teaching the machine the live vocabulaty and convert DB text into numbers
X=vectorizer.fit_transform(all_texts)
vocabulary=vectorizer.get_feature_names_out()


# X[0:1] extracts profile vector (Row 0)
# X[1:] extracts all the scraped job vectors (Row 1 to the end)
# cosine_similarity measures the geometric angle between them instantly
raw_scores= cosine_similarity(X[0:1], X[1:] )# This computes the cosine similarity between profile vector and each of the job vectors, giving  a score for how closely each job matches profile.
scores=raw_scores.flatten() # Flattens a nested matrix into a simple list of numbers




#5 Convert the math  matrix into a beautiful Pandas Dataframe
df=pd.DataFrame(X.toarray()[1:],columns=vocabulary, index=job_labels)

df['MATCH_SCORE_%'] = [round(score * 100, 2) for score in scores]


print("\n=== THE AI-SCOUT MATCH RANKINGS ===")
# Sort the dataframe so the highest matching jobs appear at the very top
df_sorted = df.sort_values(by='MATCH_SCORE_%', ascending=False)


print(df_sorted[['MATCH_SCORE_%']])
# Clean up connection
connection.close()