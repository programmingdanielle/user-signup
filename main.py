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
    if whitespace(username) or whitespace(password) or whitespace(email) == True:
        error = "Please use no white spaces."
        return render_template("index.html", error=error, username=username, email=email)
    if verify_password(password, verify) == False:
        pwerror = "Your passwords don't match."
        return render_template("index.html", error=pwerror, username=username, email=email)
    if verify_password(password, verify) == True:
        if len(password) < 3:
            pw_short_error = "Your password must be longer then 3 characters."
            return render_template("index.html", error=pw_short_error, username=username, email=email)
        if len(password) > 20:
            pw_long_error = "Your password must be less then 20 characters."
            return render_template("index.html", error=pw_long_error, username=username, email=email)
    if email is not "":
        if verify_email(email) == False:
            missing_email_error = "You're missing a @ or a . in your email."
            return render_template("index.html", error=missing_email_error, username=username, email=email)
        if verify_email(email) == True:
            if ifemail(email) == True:
                return redirect("/welcome?username={0}".format(username))
            if ifemail(email) == False:
                extra_email_error = "You can only have one @ or . in your email."
                return render_template("index.html", error=extra_email_error, username=username, email=email)
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