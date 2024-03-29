from django.conf import settings
import requests
import json
import os

import googleapiclient.discovery
import googleapiclient.errors

def format_title(title):
	if len(title)>20:
		return f'{title[0:20]}...'
	else:
		return title

class Youtube:
	def __init__(self, *args, **kwargs):
		self.vidid = kwargs.get('vid_id')
		self.api_service_name = settings.API_SERVICE_NAME
		self.api_version = settings.API_VERSION
		self.dev_key = settings.GOOGLE_API_KEY
		
		self.youtube =googleapiclient.discovery.build(
			self.api_service_name,
			self.api_version,
			developerKey = self.dev_key
			)


	def get_playlist(self):

		video_request = self.youtube.search().list(
			part="snippet",
			q="python tutorial",
			type="playlist",
			maxResults=4,
			).execute()

		playlists = []

		for item in video_request["items"]:
			playlist_id = item["id"]["playlistId"]
			playlist_details = self.youtube.playlists().list(
        	part="snippet",
        	id=playlist_id
    		).execute()
			playlist_title = playlist_details["items"][0]["snippet"]["title"]
			playlist_thumbnail_url = playlist_details["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
			playlists.append({
				"id": playlist_id,
				"title": format_title(playlist_title),
				"thumbnail_url": playlist_thumbnail_url
			})

		return playlists

	