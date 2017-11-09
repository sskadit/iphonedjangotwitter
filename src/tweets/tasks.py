from celery.task.schedules import crontab
from celery.decorators import periodic_task
# from bs4 import BeautifulSoup
from .models import AppleTrendingHastags,IphoneX
import requests
import re
import urllib.request
import uuid
import datetime
import base64
from django.db import transaction
import os

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@periodic_task(run_every=crontab(minute="*/5"))
def test():
	@transaction.atomic
	def twitterApi():
		print("Twitter API Started")
		# slack.chat.post_message('#testing', 'Twitter Has Started')
		
		import tweepy
		dit = {}
		CONSUMER_KEY = 
		CONSUMER_SECRET = 
		OAUTH_TOKEN = 
		OAUTH_TOKEN_SECRET = 
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		api = tweepy.API(auth)
		MAX_TWEETS = 500
		AppleTrendingHastags.objects.all().delete()
		for status in tweepy.Cursor(api.search, q='#apple', rpp=100).items(MAX_TWEETS):
			text = status.text
			status_created_at = status.created_at
			source = status.source
			author = status.user.screen_name
			name = status.user.name
			time_zone = status.user.time_zone
			user_language = status.user.lang
			followers = status.user.followers_count
			user_description = status.user.description
			geo_enabled = status.user.geo_enabled
			friends = status.user.friends_count
			retweets = status.retweet_count
			location = status.user.location
			user_id = status.user.id_str
			coordinates = status.coordinates
			place = status.place
			pattern = re.findall(r'(https?://[^\s]+)', text)
			pattern = str(pattern)
			string = pattern[1:-1]
			string = string[1:-1]
			AppleTrendingHastags.objects.create(text = text,status_created=status_created_at,source=source,author=author,name=name,
				time_zone=time_zone,user_language=user_language,followers=followers,user_description=user_description,geo_enabled=geo_enabled,friends=friends,
				retweets=retweets,location=location,user_id=user_id,coordinates=coordinates,place=place,link= string)
		print("Added the Apple HashTag Trendings")
	twitterApi();

	@transaction.atomic
	def twittertwo():
		import tweepy
		dit = {}
		CONSUMER_KEY = 
		CONSUMER_SECRET = 
		OAUTH_TOKEN = 
		OAUTH_TOKEN_SECRET = 
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		api = tweepy.API(auth)
		MAX_TWEETS = 500
		IphoneX.objects.all().delete()
		for status in tweepy.Cursor(api.search, q='#iPhoneX', rpp=100).items(MAX_TWEETS):
			text = status.text
			status_created_at = status.created_at
			source = status.source
			author = status.user.screen_name
			name = status.user.name
			time_zone = status.user.time_zone
			user_language = status.user.lang
			followers = status.user.followers_count
			user_description = status.user.description
			geo_enabled = status.user.geo_enabled
			friends = status.user.friends_count
			retweets = status.retweet_count
			location = status.user.location
			user_id = status.user.id_str
			coordinates = status.coordinates
			place = status.place
			pattern = re.findall(r'(https?://[^\s]+)', text)
			pattern = str(pattern)
			string = pattern[1:-1]
			string = string[1:-1]
			IphoneX.objects.create(text = text,status_created=status_created_at,source=source,author=author,name=name,
				time_zone=time_zone,user_language=user_language,followers=followers,user_description=user_description,geo_enabled=geo_enabled,friends=friends,
				retweets=retweets,location=location,user_id=user_id,coordinates=coordinates,place=place,link=string)
		print("Added the Apple iPhoneX Trendings")
	twittertwo();

