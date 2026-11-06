from dattime import datetime, timezone

from .extensions import db

class Book (db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    public_year = db.Column(db.Integer)
    isbn = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime, default=lambda:datetime.now(timezone.utc))
    
