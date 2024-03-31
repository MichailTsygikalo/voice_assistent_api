from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.linear_model import LogisticRegression

from src import words
from src.func import *
from core import get_session, get_person_d, get_monument_d, get_pers_dataset, get_mon_dataset

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

async def person_ai(text:str):

    async for session in get_session():
        dataset = await get_pers_dataset(session)
    dataset_person = {}
    for d in dataset:
        dataset_person[d.key] = d.value

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(dataset_person.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(dataset_person.values()))

    text_vector = vectorizer.transform([text]).toarray()[0]
    predict = clf.predict([text_vector])[0]

    return await get_person_d(await get_session().__anext__(), predict)

async def monument_ai(text:str):

    async for session in get_session():
        dataset = await get_mon_dataset(session)
    dataset_monument = {}
    for d in dataset:
        dataset_monument[d.key] = d.value

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(dataset_monument.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(dataset_monument.values()))

    text_vector = vectorizer.transform([text]).toarray()[0]
    predict = clf.predict([text_vector])[0]

    return await get_monument_d(await get_session().__anext__(), predict)

