
from app import db


class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    words = db.Column(db.String, unique=False, nullable=False)



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)





class Sentiment(db.Model):
    __tablename__ = 'sentiments'

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer)
    tweet_id = db.Column(db.Integer)
    score = db.Column(db.Float)
    date = db.Column(db.String, unique=False, nullable=False)



class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer)
    root_id = db.Column(db.Integer)
    tweet_id = db.Column(db.Integer)
    is_public = db.Column(db.Boolean)
    created_at = db.Column(db.String, unique=False, nullable=False)
    full_text = db.Column(db.String, unique=False, nullable=False)