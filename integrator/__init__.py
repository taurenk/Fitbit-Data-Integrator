__author__ = 'Tauren'

import os
from sqlalchemy.engine import create_engine

SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s' % (
    os.getenv('DB_USERNAME'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_URL'),
    os.getenv('DB_NAME')
)

db = create_engine(SQLALCHEMY_DATABASE_URI)
