import os
from flask import Flask
from flask import request
import json
import requests

import config

app = Flask(__name__)

def send_message(sender_id, text):
    json_data = {
        "recipient": {"id": sender_id},
        "message": {"text": text + " to you!"}
    }
    params = {
        "access_token": config.FB_MESSENGER_TOKEN
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', json=json_data, params=params)
    print(r, r.status_code, r.text)


@app.route("/", methods=['POST', 'GET'])
def main():
	if request.method == 'GET':
		verification_code = 'bot_this_is_of_yoda'
		verify_token = request.args.get("hub.verify_token")
		if verification_code == verify_token:
			return request.args.get("hub.challenge")
		else:
			return 'hello world'

	elif request.method == 'POST':
		print 'hello'
		body = request.data
		print "BODY" + body
        messaging_events = json.loads(body)['entry'][0]['messaging']
        sender = messaging_events[0]['sender']['id']
        text = messaging_events['message']['text']
        # for event in messaging_events:
        # 	sender = event['sender']['id']
        # 	if event['message'] and event['message']['text']:
        # 		text = event['message']['text']
        send_message(sender, text)
		return 'received'

	else:
		return 'Error'


if __name__ == "__main__":
	# The default port of 5000 that a Flask app starts on does not work
	# for a Heroku deployment. Instead, you need to get the PORT environment
	# variable (that is set in each Heroku deployment environment, or dyno) 
	# and start the app listening on that port
	# Read http://virantha.com/2013/11/14/starting-a-simple-flask-app-with-heroku/
	app.debug = True
	port = int(os.environ.get("PORT", 8000))
	app.run(host='0.0.0.0', port=port)
