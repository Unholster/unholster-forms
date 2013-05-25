from pymongo import MongoClient
from settings import MONGODB_URI
from urlparse import urlparse

db_name = getattr(urlparse(MONGODB_URI), 'path') or  'unholster'
client = MongoClient(MONGODB_URI)
db = client[db_name]