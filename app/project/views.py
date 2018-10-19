from flask import render_template, request, session, redirect, url_for

from app.user.forms import LoginForm, SignupForm
from app.user.models import User

from app import app
from app import db

@app.route('/project/', methods=['GET'])
def project():
	return render_template('user/login.html')
