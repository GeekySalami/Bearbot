from django.conf import settings
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

	def get_video(self, query):

		video_request = self.youtube.search().list(
			part="snippet",
			q=query,
			type="video",
			maxResults=4,
			).execute()

		videos = []

		for item in video_request["items"]:
			video_id = item["id"]["videoId"]
			video_details = self.youtube.videos().list(
        	part="snippet",
        	id=video_id
    		).execute()
			video_title = video_details["items"][0]["snippet"]["title"]
			video_thumbnail_url = video_details["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
			videos.append({
				"id": video_id,
				"title": format_title(video_title),
				"thumbnail_url": video_thumbnail_url
			})

		return videos