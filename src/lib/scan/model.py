import pymongo

conn = pymongo.MongoClient(ip, port)
dbname = conn.database_names()
