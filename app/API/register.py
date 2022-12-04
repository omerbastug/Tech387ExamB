from app import app,db
from flask import jsonify, request
from app.Models.User import User

@app.route("/api/register", methods=["POST"])
def register():
    body = request.get_json()
    try:
        newuser = User(fullName=body['fullname'],email=body['email'],password = body['password'], prefix = body.get("preferredTitle"),userCategoryId=1)
        db.session.add(newuser)
        db.session.commit()
        respUser = newuser.as_dict()
        print(respUser)
        del respUser['hash']
        del respUser['salt']  
    except BaseException as err:
        print(err)
        return jsonify({"error":err}), 400

    return jsonify({"success":"account created", "user" : respUser}) , 201
