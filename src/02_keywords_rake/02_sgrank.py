import huspacy
import pandas as pd
from textacy.extract.keyterms.sgrank import sgrank as keywords

nlp = huspacy.load()
df = pd.read_csv("data/interim/cleaned_articles.csv", sep=";")

keyphrases = []

for _, row in df.iterrows():
    doc = nlp(row["Article"])
    terms = keywords(doc, topn=10, include_pos=("NOUN", "PROPN"), ngrams=(1, 2, 3))
    print(terms)
    break
