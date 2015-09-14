__author__ = 'Tauren'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(64))
    email = Column(String(64))
    refresh_token = Column(String(128))
    last_refresh = Column(Date)
    children = relationship('HeartRate')

    def __repr__(self):
        return '<User %r>' % self.fullname

class HeartRate(Base):

    __tablename__ = 'hrdata'

    id = Column(Integer, primary_key=True)

    date = Column(Date)
    time = Column(Time)
    heart_rate = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
