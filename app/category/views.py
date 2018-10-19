from flask import render_template, request, session, redirect, url_for

from app import app
from app import db

@app.route('/category/', methods=['GET'])
def category():
	return render_template('category/index.html')
