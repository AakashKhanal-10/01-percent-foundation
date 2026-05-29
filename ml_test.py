from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


sample_jobs=[
   "python developer fastapi",
    "web developer node react",
    "python and ai engineer" 
]

#1 Create a instance of the text-to-number machine
vectorizer = TfidfVectorizer(stop_words='english') # stop_words='english' will remove common words like 'and', 'the', etc. from the analysis

# 2 Teach the machine the vocabulary and convert the text into numbers
X= vectorizer.fit_transform(sample_jobs)

#3 Get the exact list of 9 words the machine learned
vocabulary= vectorizer.get_feature_names_out()

# 4 Convert the math matrix into beautiful table
df=pd.DataFrame(X.toarray(), columns=vocabulary)

print("\n THE MACHINE'S VIEW(FEATURES VECTORS)----)")
print(df)