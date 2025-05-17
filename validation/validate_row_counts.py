import pymysql
from pymongo import MongoClient

def count_mysql_rows(table):
    with pymysql.connect(host='localhost', user='root', password='password', db='legacy_app_db').cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        return cur.fetchone()[0]

def count_mongo_docs(collection):
    return MongoClient('mongodb://localhost:27017').hybrid_db[collection].count_documents({})

for table in ['users', 'orders']:
    mysql_count = count_mysql_rows(table)
    mongo_count = count_mongo_docs(table)
    print(f"{table.capitalize()} - MySQL: {mysql_count}, MongoDB: {mongo_count}")
