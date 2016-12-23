import os

# MONGODB_URI = os.getenv('MONGOHQ_URL', 'mongodb://localhost')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
FROM_EMAIL = os.getenv('FROM_EMAIL', 'no-reply@unholster.com')
SMTP_TIMEOUT = int(os.getenv('SMTP_TIMEOUT', 10))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
