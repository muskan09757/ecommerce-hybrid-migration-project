import pymysql
from pymongo import MongoClient

mysql = pymysql.connect(host='localhost', user='root', password='password', db='legacy_app_db')
mongo = MongoClient('mongodb://localhost:27017')
mdb = mongo.hybrid_db

with mysql.cursor() as cur:
    cur.execute("""SELECT o.id, o.user_id, o.total, o.date, u.name
                    FROM orders o JOIN users u ON o.user_id = u.id""")
    for row in cur.fetchall():
        doc = {
            "_id": row[0],
            "user_id": row[1],
            "total": row[2],
            "date": row[3].strftime('%Y-%m-%d'),
            "user_name": row[4]
        }
        mdb.orders.replace_one({"_id": doc["_id"]}, doc, upsert=True)
print("✅ Migrated orders from MySQL to MongoDB")
