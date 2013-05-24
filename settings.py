import os

MONGODB_URI = os.getenv('MONGOHQ_URL', 'mongodb://localhost')

MANDRILL_APIKEY = os.getenv('MANDRILL_APIKEY', None)
MANDRILL_ENDPOINT = "https://mandrillapp.com/api/1.0/"