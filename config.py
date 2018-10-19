WEBSITE_NAME = "FundMePlease"

jinja2_globals = {
	"WEBSITE_NAME" : WEBSITE_NAME
};

flask_config = {
	"SQLALCHEMY_DATABASE_URI" : "sqlite:///../database/main.db",
	"SQLALCHEMY_TRACK_MODIFICATIONS" : False,
	"SECRET_KEY" : "supersecureawesomeapp",
	"DEBUG" : True
};
