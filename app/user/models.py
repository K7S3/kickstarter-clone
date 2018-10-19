from flask import session
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash

import random

from app import db

password_min_length = 8
password_max_length = 32

avatar_url = "images/avatars/default{}.png"

class User(db.Model):
	__tablename__ = "users"
	
	userid = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password_hash = db.Column(db.String(54), nullable=False)
	reg_date = db.Column(db.DateTime, nullable=False)
	avatar = db.Column(db.String(256), nullable=False)
	balance = db.Column(db.Integer(), nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email.lower()
		self.set_password(password)
		self.reg_date = datetime.now()
		self.avatar = avatar_url.format(random.randrange(0, 7))
		self.balance = 0

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def serialize(self):
		return { 'userid' : int(self.userid), 'username' : str(self.username), 'email' : str(self.email), 'reg_date' : str(self.reg_date.isoformat()), 'avatar' : str(self.avatar) }
		
	def __repr__(self):
		return self.serialize().__repr__()		
