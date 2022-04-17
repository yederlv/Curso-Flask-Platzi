from glob import escape
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    user_ip = escape(user_ip)   # escape() is used to prevent XSS attacks
    #return("Welcome to Yedi Flask App! Your IP is: {}".format(user_ip))
    return render_template('hello.html', user_ip=user_ip)
