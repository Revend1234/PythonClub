from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your views here.
def index (request):
    return render(request, 'templates/club/index.html')

def getresources(request):
    resources_list=Resource.objects.all()
    return render(request,'templates/club/resources.html',{'resources_list' : resources_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'templates/club/meetings.html', {'meetings_list': meetings_list})

 def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render(request, 'templates/club/meetdetails.html', context=context)