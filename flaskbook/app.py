from email_validator import EmailNotValidError, validate_email
from flask import (Flask, 
                   current_app, 
                   make_response, 
                   redirect, 
                   render_template, 
                   request, 
                   session, 
                   url_for, 
                   flash)

import os
from flask_mail import Mail,Message
# flask 클래스를 인스턴스화한다
app = Flask(__name__)


app.config["SECREY_KEY"]=os.urandom(24)
app.config["MAIL_SERVER"]=os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"]=os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"]=os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"]
# URL과 실행할 함수를 매핑한다
@app.route("/")
def index():
    return "Hello, World!"
   
