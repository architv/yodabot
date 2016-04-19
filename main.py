import cgi
import urllib2, urllib
import json
from google.appengine.ext import ndb
from google.appengine.ext import db
from google.appengine.api import memcache
import webapp2
import logging
import requests
import config

def send_message(sender_id, text):
	logging.debug('started debugging')
	url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + config.FB_MESSENGER_TOKEN
	print url

	json_data = {
		"recipient": {"id": sender_id},
		"message": {"text": text + " to you!"}
	}

	data = urllib.urlencode(json_data)
	params = {
    	"access_token": config.FB_MESSENGER_TOKEN
    }
	u = urllib.urlopen(url, data)

	# r = requests.post('https://graph.facebook.com/v2.6/me/messages', json=json_data, params=params)
	# logging.debug(str(r.status_code) + " " + r.text)

class MainHandler(webapp2.RequestHandler):

	def get(self):
		verification_code = 'bot_this_is_of_yoda'
		verify_token = self.request.get("hub.verify_token")
		if verification_code == verify_token:
			self.response.write(self.request.get("hub.challenge"))
		else:
			self.response.write(self.request)

	def post(self):
		logging.debug('started debugging')
		logging.debug(self.request)
		# print json.loads(self.request.body)['entry'][0]['messaging']
		messaging_events = json.loads(self.request.body)['entry'][0]['messaging']
		for event in messaging_events:
			sender = event['sender']['id']
			if event['message'] and event['message']['text']:
				text = event['message']['text']
				send_message(sender, text)
		self.response.http_status_message(200)


application = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
