import yaml
import psycopg2

def db_connect():
    with open("data/credentials.yaml", "r") as stream:
        try:
            credentials = yaml.safe_load(stream)['quero_collab']
        except yaml.YAMLError as exc:
            print(exc)

    conn = psycopg2.connect(
        host=credentials['host'],
        database=credentials['database'],
        user=credentials['user'],
        password=credentials['password'],
        port=credentials['port']
    )

    cursor = conn.cursor()
    return cursor