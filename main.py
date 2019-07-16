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
    user_blank = "Please enter a username."
    field_blank = "Please fill in the required fields."
    error = "Please use no white spaces in your username."
    pwerror = "Your passwords don't match."
    pass_blank = "Please fill in your password."
    pw_short_error = "Your password must be longer then 3 characters."
    pw_long_error = "Your password must be less then 20 characters."
    extra_email_error = "You can only have one @ or . in your email."
    missing_email_error = "You're missing a @ or a . in your email."
    user_short_error = "Your username must be longer then 3 characters."
    user_long_error = "Your username name must be less then 20 characters."
    pwwerror = "Please use no white spaces in your password."
    emerror = "Please use no white spaces in your email."
    em_too_short = "Your email must be at least 3 characters long."
    em_too_long = "Your email must be at least 20 characters long."
    if whitespace(username) == True:
        return render_template("index.html", error=error, username=username, email=email)
    if whitespace(password) == True:
        return render_template("index.html", pwwerror=pwwerror, username=username, email=email)
    if whitespace(email) == True:
        return render_template("index.html", emerror=emerror, username=username, email=email)
    if username == "" and password == "":
        return render_template("index.html", field_blank=field_blank, username=username, email=email)
    if username == "":
        return render_template("index.html", user_blank=user_blank, username=username, email=email)
    if password == "":
        return render_template("index.html", pass_blank=pass_blank, username=username, email=email)
    if len(username) < 3:
        return render_template("index.html", user_short_error=user_short_error, username=username, email=email)
    if len(username) > 20:
        return render_template("index.html", user_long_error=user_long_error, username=username, email=email)
    if verify_password(password, verify) == False:
        return render_template("index.html", pwerror=pwerror, username=username, email=email)
    if verify_password(password, verify) == True:
        if len(password) < 3:
            return render_template("index.html", pw_short_error=pw_short_error, username=username, email=email)
        if len(password) > 20:
            return render_template("index.html", pw_long_error=pw_long_error, username=username, email=email)
    if email is not "":
        if verify_email(email) == False:
            return render_template("index.html", missing_email_error=missing_email_error, username=username, email=email)
        if len(email) < 3:
            return render_template("index.html", em_too_short=em_too_short, username=username, email=email)
        if len(email) > 20:
            return render_template("index.html", em_too_long=em_too_long, username=username, email=email)
        if verify_email(email) == True:
            if ifemail(email) == True:
                return redirect("/welcome?username={0}".format(username))
            if ifemail(email) == False:
                return render_template("index.html", extra_email_error=extra_email_error, username=username, email=email)
    else:
        return redirect("/welcome?username={0}".format(username))
    

@app.route("/", methods=["POST"])
def whitespace(test_for_space):
    if " " in test_for_space:
        return True
    else:
        return False

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

@app.route("/", methods=["POST"])
def ifemail(emailvar2):
  e_count = 0
  p_count = 0
  for i in emailvar2:
    if i == "@":
      e_count += 1
    if i == ".":
      p_count += 1
  if e_count == 1 and p_count == 1:
    return True
  if e_count or p_count > 1:
    return False

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)



app.run()