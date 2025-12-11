from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello FlaskBook!"

@app.route("/name/<int:age>")
def show_name(age):
    return render_template("index_old.html",age=age)


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete",methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

# ## url확인용이다.
# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("show_name",name='AK'))
