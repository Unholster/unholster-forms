import os

MONGODB_URI = os.getenv('MONGOHQ_URL', 'mongodb://localhost')

MANDRILL_APIKEY = os.getenv('MANDRILL_APIKEY', None)
MANDRILL_ENDPOINT = "https://mandrillapp.com/api/1.0/"

AWS_USER = os.getenv('AWS_USER', '') 
AWS_PASSWORD = os.getenv('AWS_PASSWORD', '')
SMTP_SERVER = 'email-smtp.us-west-2.amazonaws.com'
SMTP_PORT = '587'
FROM_EMAIL = ''
DEFAULT_TIMEOUT = 10
ATTACH_FILE = 'unholster.jpg'

DEFAULT_CONTENT = '<html><body>This is a text body. <strong>Foo bar.</strong></body></html>'
