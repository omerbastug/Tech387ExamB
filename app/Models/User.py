from app import db
import bcrypt
from flask_login import UserMixin
class User(db.Model,UserMixin):
    """User model"""

    id = db.Column(db.Integer(), primary_key=True) # auto increment on default
    fullName = db.Column(db.String(length = 30), nullable=False)
    email = db.Column(db.String(length = 200), nullable=False, unique=True)
    hash = db.Column(db.String(length=64), nullable=False)
    salt = db.Column(db.String(length=64), nullable=False)
    userCategoryId = db.Column(db.Integer(), db.ForeignKey("user_category.id"), nullable=False)
    profilePictureLink = db.Column(db.String(length=250), nullable=True, default='https://www.kindpng.com/picc/m/22-223965_no-profile-picture-icon-circle-member-icon-png.png')
    prefix = db.Column(db.String(length=15), nullable=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plainpw):
        bytepassword = plainpw.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytepassword, salt)
        self.hash = hash
        self.salt = salt
    
    @property
    def title(self):
        return self.prefix+ " " + self.fullName


    def truePassword(self, passwordToCheck):
        bytepassword = passwordToCheck.encode('utf-8')
        salt = self.salt.encode('utf-8')

        hash = bcrypt.hashpw(bytepassword, salt)

        userhash = self.hash.encode('utf-8')

        return hash == userhash

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}