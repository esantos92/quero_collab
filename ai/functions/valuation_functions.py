from db_connection import *
import datetime
import pandas

def get_ranked_posts_from_tokens(user_id, tokens):
    #TODO
    pass

def get_tokens_from_posts(user_id, dataframe):
    #TODO
    pass

def metrics_per_posts(user_id):
    
    conn = db_connect()
    
    delta_time = (datetime.datetime.today() - datetime.timedelta(7)).strftime('%Y-%m-%d')    
    response = db_consume(conn, f"SELECT * FROM quero_collab.posts where date(created_at) >= '{delta_time}' and author_id != {user_id}")
    
    postsDF = pandas.DataFrame(response, columns=['post_id', 'author_id', 'text_data', 'created_at'])
    
    tokens = get_tokens_from_posts(user_id, postsDF)    
    metricsDF = get_ranked_posts_from_tokens(user_id, tokens)
    
    sql = """INSERT INTO quero_collab.ranked_posts (author_id, most_ranked, date) VALUES (%s, %s, %s)"""
    db_insert(conn, sql, metricsDF)   
        
    conn.close()
    
def metrics_per_interests(user_id):
    
    conn = db_connect()
    
    query_interests = f"""select 
                            profiles.interests 
                        from quero_collab.authors 
                            left join quero_collab.profiles on (authors.profile_id = profiles.profile_id)
                        where
                            author_id = {user_id};"""
    
    tokens = db_consume(conn, query_interests)[0][0]
    metricsDF = get_ranked_posts_from_tokens(user_id, tokens)
    
    sql = """INSERT INTO quero_collab.ranked_posts (author_id, most_ranked, date) VALUES (%s, %s, %s)"""
    db_insert(conn, sql, metricsDF)   
        
    conn.close()