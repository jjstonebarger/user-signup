from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)

app.config['DEBUG'] = True #displays runtime  errors


@app.route('/')
def display_signup_form():
    template = jinja_env.get_template('index.html')
    return template.render()


@app.route('/', methods=['POST'])
def validate_signup():
    
    username = request.form['username']
    password = request.form['password']
    pwverify = request.form['pwverify']
    email = request.form['email']

    username_error=''
    password_error=''
    pwverify_error=''
    email_error=''
    
    #username validation
    if len(username) < 3:
        if username =='':
            username_error='Please enter a username.'
        else:
            username_error='Username must have more than 3 characters.'
    for i in username:
        if i == ' ':
            username_error='Spaces are not allowed in username'
    if len(username) > 20:
            username_error='User name must be less than 20 characters.'  

    #password validation
    if len(password) < 3:
        if password =='':
            password_error='Please enter a password.'
        else:
            password_error='Password must have more than 3 characters.'
    for i in password:
        if i == ' ':
            password_error='Spaces are not allowed in password.'
    if len(password) > 20:
            password_error='Password  must be less than 20 characters.'

    #pwverify validation

    if pwverify != password:
        pwverify_error = "Passwords don't match."

    password=''
    pwverify=''

    #email validation
    chars = '@'
    char2 = '.'
    for char in email:
        count = email.count(chars)
        if count > 1 or count < 1:
            email_error = "This is not a valid email."
        count = email.count(char2)
        if count > 1 or count < 1:
            email_error = "This is not a valid email."
        else:
            if len(email) < 3 or len(email) > 20:
                email_error = "This is not a valid email."
            else:
                if char in email == ' ':
                    email_error = "This is not a valid email."

    if not username_error and not password_error and not pwverify_error and not email_error:
        template = jinja_env.get_template('welcome.html')
        return template.render(username=username)
        
    else:
        template = jinja_env.get_template('index.html')
        return template.render(username_error=username_error, password_error=password_error, username=username,
            password=password, pwverify=pwverify, pwverify_error=pwverify_error, email=email, email_error=email_error) 
         

    

app.run()