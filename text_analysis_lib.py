from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from preprocessing import preprocess_text

def text_analyzer(text1,text2,text3):
    articles = [text1, text2, text3]
    preprocessed_articles = [preprocess_text(text) for text in articles]
    vec = TfidfVectorizer(norm = None)
    scores = vec.fit_transform(preprocessed_articles)
    articles_index = [f"Article {i+1}" for i in range(len(articles))]
    feature_names = vec.get_feature_names_out()
    df = pd.DataFrame(scores.T.todense(), index = feature_names, columns = articles_index)
    result = []
    for i in range(len(articles)):
        r =(df[[f"Article {i+1}"]].idxmax()).to_string()
        result.append(r)
    return str(result[0])+"\n"+str(result[1])+"\n"+str(result[2])

