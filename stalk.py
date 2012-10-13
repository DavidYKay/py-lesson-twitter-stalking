import requests
import json
import sys

from oauth_hook import OAuthHook

from name_string import create_string_from_usernames

LIST_NAME = 'my-list-here'
USER_NAME = 'my-twitter-handle'

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
CONSUMER_KEY=""
CONSUMER_SECRET=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

LOG_CONFIG = {'verbose': sys.stderr}


class Tweet:
	def __init__(self, user_dict):
		self.username = user_dict['screen_name']
		try:
			status = user_dict['status']

		except KeyError:
			print "Lame. The user has never tweeted."
			self.tweet_time = None
			self.text = None
			self.last_known_location = None
			return

		try:
			self.last_known_location = user_dict['status']['coordinates']

			time = status['created_at']
			self.tweet_time = time
			# or!!!
			# self.tweet_time = user_dict['status']['created_at']

			self.text = user_dict['status']['text']
		except KeyError:
			print "Lame. The user was missing data."

	def __unicode__(self):
		return """%s said "%s" at %s near %s""" % (
			self.username, self.text, self.tweet_time, self.last_known_location
		)

oauth_hook = OAuthHook(ACCESS_TOKEN,
	ACCESS_TOKEN_SECRET,
	 CONSUMER_KEY,
	 CONSUMER_SECRET,
	  header_auth=True)

client = requests.session(hooks={'pre_request': oauth_hook})

response = client.get('https://api.twitter.com/1.1/lists/members.json',
	params={
	'slug': LIST_NAME,
	'owner_screen_name': USER_NAME,
	})

#print response.text

user_dicts = response.json['users']

tweets = []
for user_dict in user_dicts:
	tweet = Tweet(user_dict)
	tweets.append(tweet)

print tweets

'''
Four things:
* screen_name
* status.coordinates
* status.created_at
* status.text
'''
