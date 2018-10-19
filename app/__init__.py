from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import flask_config, jinja2_globals

app = Flask(__name__)
db = SQLAlchemy()
   
from app.user.models import User
 
def start_app():
	app.config.update(flask_config);
	app.jinja_env.globals.update(jinja2_globals);
	
	db.init_app(app=app)
	db.create_all(app=app)	
	
	from app import errorhandlers
	from app import routes
	return app
