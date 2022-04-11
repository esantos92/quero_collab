from datetime import date
import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from text_lib import preprocessing



def get_post_most_sims(model, row, post_ids):
    tokens = preprocessing(row['text_data'])
    vec = model.infer_vector(tokens) 
    sims = np.array(model.docvecs.most_similar([vec]))
    idx = sims[:,0].astype(int)
    most_sims = np.array(post_ids(idx))
    return [row['post_id'], date.today().strftime("%d/%m/%Y"), most_sims]

def get_user_sims(model, id, tokens, users_ids):
    vec = model.infer_vector(tokens) 
    sims = np.array(model.docvecs.most_similar([vec]))
    idx = sims[:,0].astype(int)
    most_sims = np.array(users_ids(idx))
    return [id, most_sims]    

def get_model(posts):
    d2v = Doc2Vec.load('d2v_pretreined')
    keywords = list(map(preprocessing, posts))
    tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
    d2v.build_vocab(documents=tagged_posts, update=True)
    total = d2v.corpus_count
    d2v.train(tagged_posts, total_examples=total, epochs=100)    

def get_posts_sims(model, df):
    post_ids = list(df['post_id'])
    table_posts = list(map(get_post_most_sims, model, df, post_ids))
    table_posts_df = pd.DataFrame(data=table_posts, columns=['post_id', 'most_ranked', 'date'])
    return table_posts_df


def get_users_sims(df):
    d2v = Doc2Vec.load('d2v_pretreined')
    keywords = df['interests']
    tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
    d2v.build_vocab(documents=tagged_posts, update=True)
    total = d2v.corpus_count
    d2v.train(tagged_posts, total_examples=total, epochs=100)

    users_id = list(df['user_ids'])

    table_posts = list(map(get_user_sims, d2v, df, users_id))

    table_users_df = pd.DataFrame(data=table_posts, columns=['author_id', 'most_similaritys'])
    return table_users_df


    


    
