from pymongo import MongoClient
from settings import MONGODB_URI
from urlparse import urlparse

db_name = getattr(urlparse(MONGODB_URI), 'path') or  'unholster'
db_name = db_name.lstrip("/")
client = MongoClient(MONGODB_URI)
db = client[db_name]