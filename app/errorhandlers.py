from flask import render_template
from app import app

@app.errorhandler(403)
def forbidden_page(error):
	error_details = {
		"error_title" : "Forbidden Page",
		"error_code" : 403,
		"error_description" : "You aren't supposed to be here."
	};
	return render_template("errors/error.html", **error_details), 403

@app.errorhandler(404)
def page_not_found(error):
	error_details = {
		"error_title" : "Page Not Found",
		"error_code" : 404,
		"error_description" : "You shouldn't have landed here."
	};
	return render_template("errors/error.html", **error_details), 404

@app.errorhandler(500)
def server_error_page(error):
	error_details = {
		"error_title" : "Internal Error",
		"error_code" : 500,
		"error_description" : "This is our fault; this shouldn't be happening."
	};
	return render_template("errors/error.html", **error_details), 500
