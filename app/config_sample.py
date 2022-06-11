import os

import logging

from app.config_common import *


# DEBUG has to be to False in a production environment for security reasons
DEBUG = False

# App environment
# ['development', 'demo', 'production']
APP_ENV = 'development'

# Secret key for generating tokens
SECRET_KEY = 'houdini'

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'pa$$word')

# Database choice
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'flask.boilerplate'
MAIL_PASSWORD = 'flaskboilerplate123'
MAIL_DEFAULT_SENDER = 'donotreply@gmail.com'
MAIL_DEFAULT_SENDER_DISPLAY_NAME = 'DO NOT REPLY'
ADMINS = ['flask.boilerplate@gmail.com']


# Development destinations
DEVELOPMENT_TESTING_EMAIL = 'test@gmail.com'

# Logging
LOG_LEVEL = logging.INFO


