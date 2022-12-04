from app import db

class UserCategory(db.Model):
    """Categories for users"""

    id = db.Column(db.Integer(), primary_key=True) # auto increment on default
    categoryName = db.Column(db.String(length=20), nullable=False, unique=True)