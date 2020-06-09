from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresource/', views.getresource, name='resources'),
    path('getmeeting/', views.getmeeting, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails')
]