from flask import Flask,render_template,url_for,redirect,requests

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello FlaskBook!"

@app.route("/jenny")
def jenny():
    return "hello black pink!"

@app.route("/hello/<int:age>")
def hello_jenny(age):
    return render_template("index.html",age=age)

@app.route("/jennyage/<int:age>",methods=["GET"])
def jennyage(age):
    return f"old {age}"


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete",methods=["GET","POST"])
def contact_complete():
    if requests.method=="POST":
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

## url확인용 이다.
with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello_jenny",age="12"))