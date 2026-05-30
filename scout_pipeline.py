import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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

db_job_texts = [row[2] for row in rows] # This is the bridge between your database and the machine learning part. It takes the 'keywords' column from each job record and creates a list of text strings that the TF-IDF vectorizer can learn from.
job_labels=[f"Job {row[0]}: {row[1]}" for row in rows] # To label rows in Pandas

# 3. Initialize your text-to-number machine (Your exact logic from yesterday)
vectorizer = TfidfVectorizer(stop_words='english')

#4 Teaching the machine the live vocabulaty and convert DB text into numbers
X=vectorizer.fit_transform(db_job_texts)
vocabulary=vectorizer.get_feature_names_out()

#5 Convert the math  matrix into a beautiful Pandas Dataframe
df=pd.DataFrame(X.toarray(), columns=vocabulary, index=job_labels)


print(" THE MACHINE'S VIEW OF YOUR DATABASE RECORDS ---")
print(df.head(10)) # Show the first few rows of the DataFrame


# Clean up connection
connection.close()