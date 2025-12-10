from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello FlaskBook!"

@app.route("/jenny")
def jenny():
    return "hello black pink!"

@app.route("/hello/<name>",methods=["GET"],endpoint="hello-endpoint")
def hello_jenny(name):
    return f"hello {name}"

@app.route("/jennyage/<int:age>",methods=["GET"])
def jennyage(age):
    return f"old {age}"

