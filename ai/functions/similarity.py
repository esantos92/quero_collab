
from text_lib import preprocessing
from datetime import date
import pandas as pd


from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np


def get_post_sims(model, row, post_ids):
    tokens = preprocessing(row['post'])
    vec = model.infer_vector(tokens) 
    sims = np.array(model.docvecs.most_similar([vec]))
    idx = sims[:,0].astype(int)
    most_sims = np.array(post_ids(idx))
    return [row['user_id'], most_sims, date.today().strftime("%d/%m/%Y")]

def get_user_sims(model, id, tokens, users_ids):
    vec = model.infer_vector(tokens) 
    sims = np.array(model.docvecs.most_similar([vec]))
    idx = sims[:,0].astype(int)
    most_sims = np.array(users_ids(idx))
    return [id, most_sims]    



def get_posts_sims(df):
    d2v = Doc2Vec.load('d2v_pretreined')
    keywords = list(map(preprocessing, df['post']))
    tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
    d2v.build_vocab(documents=tagged_posts, update=True)
    total = d2v.corpus_count
    d2v.train(tagged_posts, total_examples=total, epochs=100)

    post_ids = list(df['post_id'])

    table_posts = list(map(get_post_sims, d2v, df, post_ids))
    table_posts_df = pd.DataFrame(data=table_posts, columns=['user_id', 'date', 'most_similaritys'])
    return table_posts_df


def get_users_sims(df):
    d2v = Doc2Vec.load('d2v_pretreined')
    keywords = df['tokens']
    tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
    d2v.build_vocab(documents=tagged_posts, update=True)
    total = d2v.corpus_count
    d2v.train(tagged_posts, total_examples=total, epochs=100)

    users_id = list(df['user_ids'])

    table_posts = list(map(get_post_sims, d2v, df, users_id))

    table_users_df = pd.DataFrame(data=table_posts, columns=['user_id', 'most_similaritys'])
    return table_users_df


    


    
