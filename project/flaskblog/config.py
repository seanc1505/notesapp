import os


class Config:
    SECRET_KEY = '33f1ae20b4a0d78c4d3eb6ecdce3fb1a' # move to environment var
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # move to environment var
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')