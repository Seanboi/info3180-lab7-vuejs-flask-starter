from . import db
from datetime import datetime


class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime,default=db.func.current_timestamp())
    
    def __repr__(self):
        return f'<Movie {self.title}>'
    