from django.shortcuts import render
from .mixins import Youtube
# Create your views here.

def dash (request):
	yt = Youtube()
	playlist = yt.get_playlist()
	return render(request,'dashboard/dash.html', {'plist':playlist})