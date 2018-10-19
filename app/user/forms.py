from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import *
from wtforms.fields.html5 import EmailField

from app.user.models import User, password_min_length, password_max_length 

class LoginForm(Form):
	title = "Login"
	name = TextField("Username/Email",  [Required()], render_kw={ "placeholder" : "Enter your username/email", "required" : "required" })
	password = PasswordField("Password",  [Required()], render_kw={ "placeholder" : "Enter your password", "required" : "required" })
	rememberme = BooleanField("Remember Me")
	submit = SubmitField("Login")
	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.name.data.lower()).first()
		if user == None:
			user = User.query.filter_by(username = self.name.data).first()
			
		if user == None:
			self.name.errors.append("The account with the given username/email does not exist.")
			return False
			
		if user.check_password(self.password.data) == False:
			self.password.errors.append("Wrong password.")
			return False
		
		self.user = user
		return True

class SignupForm(Form):
	title = "Sign Up"
	username = TextField("Username",  [Required()], render_kw={ "placeholder" : "Enter your username", "required" : "required" })
	email = EmailField("Email",  [Required(), Email()], render_kw={ "placeholder" : "Enter your email", "required" : "required" })
	password = PasswordField("Password",  [Required(), Length(password_min_length, password_max_length)], render_kw={ "placeholder" : "Enter your password", "required" : "required"})
	password_retype = PasswordField("Re-type Password",  [Required(), EqualTo("password", "Passwords do not match.")], render_kw={ "placeholder" : "Enter your password again", "required" : "required" })
	agreement = "By signing up, you agree to our terms of use, privacy policy and cookie policy."
	submit = SubmitField("Signup")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False

		user_by_username = User.query.filter_by(username = self.username.data).first()
		if user_by_username:
			self.username.errors.append("This username is already taken.")

		user_by_email = User.query.filter_by(email = self.email.data.lower()).first()
		if user_by_email:
			self.email.errors.append("That email is already in use.")

		return not(user_by_username or user_by_email)
