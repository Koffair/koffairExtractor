import pandas as pd
from rake_nltk import Rake

with open("data/external/stopword.txt", "r") as infile:
    stopwords = set(infile.read().split("\n"))

df = pd.read_csv("data/interim/cleaned_articles.csv", sep=";")
r = Rake(stopwords=stopwords, language="hungarian")

for _, row in df.iterrows():
    r = Rake(stopwords=stopwords, language="hungarian")
    r.extract_keywords_from_text(row["Article"])
    print(r.get_ranked_phrases_with_scores())
