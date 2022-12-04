from app import app
from flask import send_file

@app.route("/logo/login/ProductArena", methods=['get'])
def login_logo():
    return send_file("./images/ProductArenaLogo-login.png")