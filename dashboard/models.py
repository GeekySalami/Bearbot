from django.db import models
from googleapiclient.discovery import build

# Create your models here.

def yt():
	key = 'AIzaSyBxmOeg_wm7NAkTfr9Fv3iWSMTyk7VEWRI'
	youtube = build('youtube', 'v3', developerKey = key)
	req = youtube.channels().list(
		part= 'statistics',
		forUsername= 'schafer5'
		)

	res = req.execute

	return res