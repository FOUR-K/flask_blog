import os

class Config:
    SECRET_KEY = '4ba307f9992d3170d84ad354e7f5183b'
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or \
        'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('email_user')
    MAIL_PASSWORD = os.environ.get('email_pass')