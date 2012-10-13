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

oauth_hook = OAuthHook(ACCESS_TOKEN,
	ACCESS_TOKEN_SECRET,
	 CONSUMER_KEY,
	 CONSUMER_SECRET,
	  header_auth=True)

client = requests.session(hooks={'pre_request': oauth_hook})

# response = client.get('http://api.twitter.com/1/account/rate_limit_status.json')
# results = json.loads(response.content)

# print results

# POST a new tweet
# response = client.post('http://api.twitter.com/1.1/statuses/update.json',
# 	{'status': "Yep! Testin 1.1...", 'wrap_links': True})
# print response.json

# create a twitter list from the file of investors (stalking.csv)

# for each target in stalk list
# find last known location, using geo tweet
fname = "stalking.csv"

usernames = [line.strip() for line in open(fname)]

username_string = create_string_from_usernames(usernames)

response = client.post('http://api.twitter.com/1.1/lists/members/create_all.json',
	{
	'slug': LIST_NAME,
	'screen_name': username_string,
	'owner_screen_name': USER_NAME,

	}, config=LOG_CONFIG)

print response.request.data_and_params

print response.text
