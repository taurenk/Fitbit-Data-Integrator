__author__ = 'Tauren'

from integrator.models import User, HeartRate
from integrator import db
from sqlalchemy.orm import sessionmaker

class Warehouse:

    def __init__(self):
        self.Session = sessionmaker(bind=db)

    def store_heart_rate_data(self, heart_rate_result):
        pass

    def update_refresh_token(self, user_id, new_refresh_token):
        pass

