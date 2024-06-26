from django.conf import settings
import requests
import json
import os

import googleapiclient.discovery
import googleapiclient.errors

def format_title(title):
	if len(title)>30:
		return f'{title[0:26]}...'
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

	def get_data(self):


		#get playlists for channelId
		playlist_request = self.youtube.playlists().list(
			part="snippet,contentDetails",
			)
		
		playlist_response = playlist_request.execute()

		#list of playlists
		playlists = [p["id"] for p in playlist_response["items"]]

		nextPageToken = None

		videos = []
		data = []
		
		while True:
			
			#make another request for playlist data (max results for page 1 is 50) 
			for pl in playlists:
				playlist_items_request = self.youtube.playlistItems().list(
					part="contentDetails",
					playlistId=pl,
					maxResults=50,
					pageToken=nextPageToken
					)
				playlist_items_response = playlist_items_request.execute()

				#append video ID to list
				for item in playlist_items_response["items"]:
					videos.append(item["contentDetails"]["videoId"])
			
			#make another request to get video specific infomation
			video_request = self.youtube.videos().list(
				part="contentDetails,snippet,player",
				id=",".join(videos)
				)
			video_response = video_request.execute()

			for item in video_response["items"]:

				#create dict for each video and append to data list
				vid_data = {
					"id": item["id"],
					"title":item["snippet"]["title"],
					"title_formatted":title_formatting(item["snippet"]["title"]),
					"description":item["snippet"]["description"],
					"thumbnail":item["snippet"]["thumbnails"]["medium"]["url"],
					"iframe":item["player"]["embedHtml"],
				}

				data.append(vid_data)

			
			#get next page token from request - break while loop if there aren't anymore pages
			nextPageToken = playlist_response.get("nextPageToken")
			if not nextPageToken:
				break

		return data

	def get_playlist(self):


		#retrieve data for 1 x video. This is similar to the get_data method	
		video_request = youtube.search().list(
			part="snippet",
			q="python tutorial",
			type="playlist",
			maxResults=max_results
			).execute()

		playlist[]
		for item in search_response["items"]:
    		playlist_id = item["id"]["playlistId"]
    		playlist_details = youtube.playlists().list(
        	part="snippet",
        	id=playlist_id
    		).execute()
    		playlist_title = playlist_details["items"][0]["snippet"]["title"]
    		playlist_thumbnail_url = playlist_details["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
    		playlists.append({
      		"id": playlist_id,
      		"title": playlist_title,
      		"thumbnail_url": playlist_thumbnail_url
    		})

		return playlists

	