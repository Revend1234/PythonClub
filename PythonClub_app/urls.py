from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('PythonClub_app/', include('PythonClub.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('getresource/', views.getresources, name='resources'),
    path('getmeeting/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]