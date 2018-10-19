from flask import render_template, request, session, redirect, url_for

from app.user.forms import LoginForm, SignupForm
from app.user.models import User

from app import app
from app import db

@app.route('/user/login/', methods=['GET', 'POST'])
def user_login():
	return_url = request.args.get('return_url', default = None)	
	form = LoginForm()

	if request.method == 'POST' and form.validate() == True:
			session['userid'] = form.user.userid
			session['username'] = form.user.username
			session['email'] = form.user.email
			session['reg_date'] = form.user.reg_date
			session['avatar'] = form.user.avatar
			
	if 'userid' in session:
		try:
			url = url_for(return_url)
		except:
			url = ""
		return redirect(url)			

	return render_template('user/login.html', form = form, return_url = return_url)


@app.route('/user/signup/', methods=['GET', 'POST'])
def user_signup():
	return_url = request.args.get('return_url', default = None)
	form = SignupForm()
	
	if request.method == 'POST' and form.validate() == True:
			user = User(form.username.data, form.email.data, form.password.data)
			db.session.add(user)
			db.session.commit()
			
			session['userid'] = user.userid
			session['username'] = user.username
			session['email'] = user.email
			session['reg_date'] = user.reg_date
			session['avatar'] = user.avatar
	
	if 'userid' in session:
		try:
			url = url_for(return_url)
		except:
			url = ""
		return redirect(url)
			
	return render_template('user/signup.html', form = form, return_url = return_url)
		
@app.route('/user/logout/')
def user_logout():
	session.pop('userid', None)
	session.pop('username', None)
	session.pop('email', None)
	session.pop('reg_date', None)
	session.pop('avatar', None)
	return redirect(url_for("index"))
	
@app.route('/user/profile/')
@app.route('/user/profile/<int:userid>')
def user_profile(userid = None):
	if userid == None:
			userid = session.get('userid', None)
	
	if userid == None:
		return redirect(url_for('user_login') + '?return_url=profile')
	
	user = User.query.filter_by(userid = userid).first()
	return render_template('user/profile.html', user = user)
			
		
		
		
		
		
		
		
		
		
		
		
		
