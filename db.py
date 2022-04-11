import pymongo

dbClient = pymongo.MongoClient("mongodb://localhost:27017/")
dbName = dbClient["Restaurant"]
