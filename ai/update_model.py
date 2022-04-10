
from text_lib import preprocessing
from functions import db_connecttion


from gensim.models import KeyedVectors
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np


d2v = Doc2Vec.load('d2v_pretreined')

# conn = db_connect()
# query = ''
# db_consume(conn, query)

# df = 
# keywords = df['keywords]

#matriz de documentos com as tags, cada linha é um vetor dos tokens de cada doc
tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
d2v.build_vocab(documents=tagged_posts, update=True)

total = d2v.corpus_count
d2v.train(tagged_posts, total_examples=total, epochs=100)
docs_vecs = np.array([d2v.docvecs[i] for i in range(len(tagged_posts))])

# df['doc_vec'] = docs_vecs


sims_table = []


def get_sims(model, user):    
    sims = np.array(model.docvecs.most_similar([user['doc_vec']]))
    idx = sims[:,0].astype(int)
    most_sims = np.array(post_ids(idx))df[]

    sims_table.append([user['user_id'], most_sims], date.today().strftime("%d/%m/%Y"))

table = list(map(get_sims, data))

new_df = pd.DataFrame(data=table, columns=['post_id', 'user_id', 'post'])




sims = np.array(d2v.docvecs.most_similar([new_vector]))
idx = sims[:,0].astype(int)
data[idx]