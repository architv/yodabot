import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
	return "Hello World!"

if __name__ == "__main__":
	# The default port of 5000 that a Flask app starts on does not work
	# for a Heroku deployment. Instead, you need to get the PORT environment
	# variable (that is set in each Heroku deployment environment, or dyno) 
	# and start the app listening on that port
	# Read http://virantha.com/2013/11/14/starting-a-simple-flask-app-with-heroku/
	# port = int(os.environ.get("PORT", 8000))
	app.run(host='0.0.0.0', port=8000)
