from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index ():
    return render_template("index.html", title="User Login")

@app.route("/", methods=["POST"])
def verify_info():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    username_error = ""
    password_error = ""
    email_error = ""
    if username.strip() == "" or password.strip() == "" or verify.strip() == "":
        error = "Please use no white spaces."
        return render_template("index.html", error=error)
    if verify_password(password, verify) == False:
        return "Your passwords don't match."
    if verify_password(password, verify) == True:
        if len(password) < 3:
            return "Make your password longer."
        if len(password) > 20:
            return "Make your password shorter."
    if email is not "":
        if verify_email(email) == False:
            return "You're missing a @ or a . in your email."
        if verify_email(email) == True:
            return "You pass everything!$!@$!@$$!"
    else:
        return "You pass everything!"
    

@app.route("/", methods=["POST"])
def verify_password(passw, ver):
    if passw == ver:
        return True
    else:
        return False

@app.route("/", methods=["POST"])
def verify_email(emailvar):
    if "@" and "." in emailvar:
        return True
    else:
        return False



app.run()