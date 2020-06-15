from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm
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

def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'templates/club/newmeeting.html', {'form': form})

def newResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'templates/club/newresource.html', {'form': form})