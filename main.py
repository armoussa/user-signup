from flask import Flask, request, render_template
import re


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")

def index():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])

def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error = '' 
    verify_error = ''
    email_error = ''

    if username == "":
        user_error = "Please enter a valid username."
    elif len(username) < 3 or len(username) > 20:
        user_error = "Username invalid. Please enter a username between 3 and 20 characters."
        #username = ""
    elif " " in username:
        user_error = "Username invalid. Username cannot contain spaces."
        username = ""
    
    if password == "":
        pass_error = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        pass_error = "Password invalid. Please enter a password between 3 and 20 characters."
        password = ""
    elif " " in password:
        pass_error = "Password invalid. Password cannot contain spaces."
        password = ""
    
    if verify == "" or verify != password:
        verify_error = "Passwords do not match.Please re-enter."
        verify = ""
    
    if email != "":

        if len(email) < 3 or len(email) > 20:
            email_error="Email address is not valid."    
        elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
            email_error= "Email address is not valid."
    
    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html', username = username, user_error = user_error, pass_error = pass_error, verify_error = verify_error,email = email, email_error = email_error)

app.run()