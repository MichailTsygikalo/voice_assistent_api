from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.linear_model import LogisticRegression

from src import words
from src.func import *

def main_src(data:str):

    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values())) 

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    answer = answer.replace(func_name, '')

    full_answer = globals()[func_name]()

    return {'data':answer,'db_':full_answer}