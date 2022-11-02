from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def Login():
    return "Login"

@auth.route("/sign-up")
def SignIn():
    return "SignUp"

@auth.route("/sign-out")
def SignOut():
    return "SignOut"
