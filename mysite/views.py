from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("hello world")

def current_time(request):
    now = datetime.datetime.now()
    html = "<h1>Now is %s</h1>" % now
    return HttpResponse(html)

