import pandas as pd

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("cite_updated.csv")
def similar(searchword):
    if searchword == '':
        author_lst = []
        index_lst = []
        title_lst = []
        for title, index in zip(data['title'],data['index']):
            title_lst.append(title)
            index_lst.append(index)
            author_lst.append(author)

        return index_lst, title_lst,author_lst

    else:
        author_lst = []
        index_lst = []
        title_lst = []
        for title, index, author in zip(data['title'],data['index'],data['author']):
            if searchword in title.lower():
                title_lst.append(title)
                index_lst.append(index)
                author_lst.append(author)

        return index_lst, title_lst,author_lst

def similar_papers(title_selected):
    tfidfvec = TfidfVectorizer()
    tfidf = tfidfvec.fit_transform((data["title_authors"]))
    cos_sim = cosine_similarity(tfidf, tfidf)
    indices = pd.Series(data.title)
    recommended = []
    titles = []
    authors = []
    index = indices[indices == title_selected].index[0]
    similarity_scores = pd.Series(cos_sim[index]).sort_values(ascending = False)
    top_10_movies = list(similarity_scores.iloc[1:11].index)

    for i in top_10_movies:
        recommended.append(list(data.index)[i])

    for i in recommended:
        titles.append(data.loc[i].title)
    for i in recommended:
        authors.append(data.loc[i].author)



    return recommended,titles,authors
