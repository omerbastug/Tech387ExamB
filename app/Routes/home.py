from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from app.Models.Appointment import Appointment
from app.Models.User import User
import datetime
@app.route("/home")
def home():
    if not current_user.is_authenticated:
        flash("Potrebna je prijava")
        return redirect(url_for("login_page"))

    x = datetime.datetime.now()
    appointments = Appointment.query\
                        .join(User, User.id == Appointment.patientId)\
                        .filter(Appointment.time > x, Appointment.doctorId == current_user.id)\
                        .add_columns(Appointment.time,Appointment.issue,User.fullName, User.profilePictureLink)\
                        .order_by(Appointment.time)\
                        .all()

    days  = [] # response object
    temp =  datetime.date(2019, 4, 13) # any past date
    day= {} # tracking variable for grouping by days
    day['appointments'] = []
    for ap in appointments:
        if ap.time.strftime("%x") != temp.strftime("%x"):
            days.append(day)
            temp = ap.time
            day={}
            day['heading'] = ap.time.strftime("%A")
            day['appointments'] = []
        i = ap.fullName.find(" ")
        day['appointments'].append({
            "name" : ap.fullName[:(i+2)]+".",
            "time" : ap.time.strftime("%H:%M"),
            "issue" : ap.issue,
            'date' : ap.time,
            "ppSrc": ap.profilePictureLink
        })
    days.append(day)
    days.pop(0)


    days[0]['heading'] ='Patient list for today' if days[0]['appointments'][0]['date'].strftime("%x") == x.strftime("%x") else days[0]['heading']
    x = x + datetime.timedelta(days=1)
    days[1]['heading'] ='Tomorrow' if days[1]['appointments'][0]['date'].strftime("%x") == x.strftime("%x") else days[0]['heading']
    days[0]['heading'] ='Tomorrow' if days[0]['appointments'][0]['date'].strftime("%x") == x.strftime("%x") else days[0]['heading']

    return render_template("home.html", days = days)
    return render_template("home.html")