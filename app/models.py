from . import db
from datetime import datetime


class Movie(db.Model):
    __tablename__ = 'movies'  # This line is important
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    
    def __repr__(self):
        return f'<Movie {self.title}>'
    