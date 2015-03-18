from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import json

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(String(50), primary_key=True)
    firstname = Column(String(45))
    gender = Column(String(45))
    photo = Column(String(200))

    def __repr__(self):
        return self.user_id + " " + self.firstname

    def as_dict(self):
        user_dict = {}
        user_dict['id'] = self.user_id
        user_dict['firstname'] = self.firstname
        user_dict['gender'] = self.gender
        user_dict['photo'] = json.loads(self.photo)
        return user_dict


class Venue(Base):
    __tablename__ = 'venues'

    venue_id = Column(String(60), primary_key=True)
    name = Column(String(45))
    location = Column(String(1000))
    menu = Column(String(1000))
    stats = Column(String(1000))
    categories = Column(String(1000))

    def __repr__(self):
        return self.venue_id + " " + self.name


class Tip(Base):
    __tablename__ = 'tips'

    tip_id = Column(String(50), primary_key=True)
    canonicalurl = Column(String(300), key='canonicalUrl')
    likes = Column(Integer, nullable=True)
    likes_content = Column(String(2000))
    text = Column(String(2000))
    user = models.ForeignKey(User, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)



