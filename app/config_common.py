import os

# Working directory of project
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# Application Version #
VERSION = '0.1.1'

TIMEZONE = 'America/Los_Angeles'

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

# Logging
LOG_FILE = True
LOG_FILENAME = os.path.join(PROJECT_DIR,'error.log')
LOG_MAXBYTES = 1024
LOG_BACKUPS = 2
