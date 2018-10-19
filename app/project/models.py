from app import db

class Project(db.Model):
	__tablename__ = "projects"
	
	projectid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	description = db.Column(db.String(1024), nullable=False)
	target_fund = db.Column(db.Integer(), nullable=False)
	current_fund = db.Column(db.Integer())
	cover = db.Column(db.String(100))

	def __init__(self, name, description, target_fund):
		self.name = name
		self.description = description
		self.target_fund = target_fund
		self.cover = None
		self.current_fund = 0
