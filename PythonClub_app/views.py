from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getresource(request):
    resource_list=ProductType.objects.all()
    return render(request,'pythonclub_app/resource_list',{'resource_list' : resource_list})
