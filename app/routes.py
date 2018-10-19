from flask import render_template, session
from app import app

from app.user import views
from app.category import views
from app.project import views

@app.route('/')
def index():
	return render_template('index.html')
