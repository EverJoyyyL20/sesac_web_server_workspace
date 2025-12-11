from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/<string:username>")
def index(username):
    return render_template("index.html",username=username)

@app.route("/<int:gugudan>")
def gugudan(gugudan):
    return render_template("gugudan.html",gugudan=gugudan)

if __name__=="__main__":
    app.run()