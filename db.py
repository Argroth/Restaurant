import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

dbUser = os.getenv('MONGO_ROOT_USER')
dbUserPass = os.environ.get('MONGO_ROOT_PASSWORD')
dbServer = os.environ.get('MONGO_CONNECTION_ADDRESS')

dbClient = pymongo.MongoClient(f"mongodb://{dbUser}:{dbUserPass}@{dbServer}:27020")
dbName = dbClient["Restaurant"]
