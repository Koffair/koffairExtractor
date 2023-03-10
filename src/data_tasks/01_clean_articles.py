import html
import re

import pandas as pd

df = pd.read_csv("data/raw/contents.zip", sep=";")
df.fillna('', inplace=True)


CLEANR = re.compile('<.*?>')
CDATA = re.compile('\/\/\s&lt;!\[CDATA\[\n.*\n\/\/\s*\]\]&gt;')


def clean_txt(txt):
    """Postprocess txt, removes unescaped html entities"""
    txt = txt.replace("&amp;gt;", " ").replace("&amp;nbsp;", " ").replace("&quot;", " ")
    txt = txt.replace("&#x27", " ").replace("::adbox::7::", "").replace("&amp;lt;", " ")
    txt = txt.replace("&amp;amp;", " ")
    return txt


def cleanhtml(raw_html):
    """Clean raw html page"""
    cleaned_txt = clean_txt(html.escape(re.sub(CLEANR, ' ', raw_html)))
    return re.sub(CDATA, ' ', cleaned_txt)


titles = []
leads = []
articles = []

for _, row in df.iterrows():
    title = cleanhtml(row[0])
    lead = cleanhtml(row[3])
    text = cleanhtml(row[4])
    titles.append(title)
    leads.append(lead)
    articles.append(text)

df_cleaned = pd.DataFrame()
df_cleaned["Title"] = titles
df_cleaned["Lead"] = leads
df_cleaned["Article"] = articles

df_cleaned.to_csv("data/interim/cleaned_articles.csv", sep=";", index=False)
