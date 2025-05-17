import pymysql
from pymongo import MongoClient

mysql = pymysql.connect(host='localhost', user='root', password='password', db='legacy_app_db')
mongo = MongoClient('mongodb://localhost:27017')
mdb = mongo.hybrid_db

with mysql.cursor() as cur:
    cur.execute("SELECT id, name, email FROM users")
    for row in cur.fetchall():
        mdb.users.replace_one(
            {"_id": row[0]},
            {"_id": row[0], "name": row[1], "email": row[2]},
            upsert=True
        )
print("✅ Migrated users from MySQL to MongoDB")
