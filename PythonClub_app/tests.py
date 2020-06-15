from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your tests here.

class MeetingTest(TestCase):
   #set up one time sample data
   def setup(self):
       title = MeetingTitle(titlename='Information')
       meeting=Meeting(meetinglocation='Computer Room', meetingtitle=title, meetingtime='12:30')
       return meeting

   def test_string(self):
       meet = self.setup()
       self.assertEqual(str(meet), meet.titlename)
  
   def test_time(self):
       meet=self.setup()
       self.assertEqual(meet.meetingtime(), 12:30)

   def test_title(self):
       meet=self.setup()
       self.assertEqual(str(meet.titlename), 'Information')

   def test_table(self):
       self.assertEqual(str(meeting._meta.db_table), 'Meetings')

class MinutesTest(TestCase):
   def test_string(self):
       minute=Minute(minutestext="Agenda Items")
       self.assertEqual(str(minute), minute.minutestext)

   def test_table(self):
       self.assertEqual(str(minutes._meta.db_table), 'minute')

class ResourceTest(TestCase):
   #set up one time sample data
   def setup(self):
       name = ResourceName(resourcename='Code Academy')
       resource=Resource(resourceurl='https://www.codecademy.com/learn/learn-python', resourcetype=name, resourcedate='4/3/2020')
       return resource

   def test_string(self):
       reso = self.setup()
       self.assertEqual(str(reso), reso.resourcename)
  
   def test_url(self):
       reso=self.setup()
       self.assertEqual(reso.resourceurl(), https://www.codecademy.com/learn/learn-python)

   def test_type(self):
       reso=self.setup()
       self.assertEqual(str(reso.resourcetype), 'Learn Python')

   def test_table(self):
       self.assertEqual(str(resource._meta.db_table), 'Resources')

class EventTest(TestCase):
   #set up one time sample data
   def setup(self):
       title = EventTitle(EventTitle='Learning Basic')
       event=Event(eventlocation='room3210', eventtitle=name, eventdate='6/13/2020')
       return event

   def test_string(self):
       even = self.setup()
       self.assertEqual(str(even), even.eventlocation)
  
   def test_date(self):
       even=self.setup()
       self.assertEqual(even.eventdate(), '6/13/2020')

   def test_description(self):
       even=self.setup()
       self.assertEqual(str(eve.description), 'Basic Course')

   def test_table(self):
       self.assertEqual(str(event._meta.db_table), 'Events')

class MeetingFormTest(TestCase):
    def setup(self):
       title = MeetingFormTest(titlename='Schedule')
       meeting=Meeting(meetinglocation='room 3201', meetingtitle=title, meetingtime='1:30')
       return meeting

   def test_table(self):
       self.assertEqual(str(meeting._meta.db_table), 'Meetings')