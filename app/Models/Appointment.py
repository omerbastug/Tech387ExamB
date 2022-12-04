from app import db

class Appointment(db.Model):
    """Categories for users"""

    id = db.Column(db.Integer(), primary_key=True) # auto increment on default
    time = db.Column(db.DateTime, nullable= False, unique= True)
    doctorId = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    patientId = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    issue = db.Column(db.String(length=64), nullable=False)

