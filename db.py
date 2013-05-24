from pymongo import MongoClient
from settings import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client['unholster']