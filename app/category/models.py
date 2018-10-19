from app import db

class Category(db.Model):
	__tablename__ = "category"
	
	categoryid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	description = db.Column(db.String(1000), nullable=False)
	def __init__(self, name, description = ""):
		self.name = name
		self.description = description
