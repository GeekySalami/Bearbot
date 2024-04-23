from django.shortcuts import render
from . import mixins
from . import gem
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def learn(request):
	yt = mixins.Youtube()
	vids = yt.get_video(query = "python3")
	return render(request,'learn/learningmodule.html',{'vids':vids})

@csrf_exempt  
def sugg(request):
    print(request.POST)
    if request.method == 'POST':
        data = json.loads(request.body)
        cde = data.get('cde', '')
        cde = str(cde)
        sum = gem.Summarizer()
        cdesummary = sum.resp(cde)
        ytv = mixins.Youtube()
        ytvid = ytv.get_video(query=cdesummary)
        print("if entered")
    else:
        cdesummary = "This is the sumarry"
        ytv = mixins.Youtube()
        ytvid = ytv.get_video(query=cdesummary)
        print("if not entered")
    
    print("summarry:"+cdesummary)
    return JsonResponse({"vids":ytvid})