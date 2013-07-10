from django.db import models
from django.contrib import admin
# Create your models here.


class Identity(models.Model):
	name = models.CharField(max_length=20,blank=True)
	surname = models.CharField(max_length=20,blank=True)
	patronymic = models.CharField(max_length=20,blank=True)
	nickname = models.CharField(max_length=30)
	def __unicode__(self):
		return (self.surname + " " + self.name + " " + self.patronymic)
		
class ContactInformation(models.Model):
	email = models.EmailField(max_length=30,blank=True)
	phone_number = models.DecimalField(max_digits=19,decimal_places=4,null=True,blank=True)
	social_network1 = models.URLField(null=True, blank=True)
	social_network2 = models.URLField(null=True,blank=True)
	social_network3 = models.URLField(null=True,blank=True)
	def __unicode__(self):
		return self.email
		
class PersonalInformation(models.Model):
    biography = models.TextField(blank=True)
    publications = models.ManyToManyField('Publication')
    photo = models.CharField(max_length=20)
    def __unicode__(self):
		return self.photo

	
# Family of Persons	
class Person(models.Model):
	person_id = models.OneToOneField("Identity")
	contacts = models.OneToOneField("ContactInformation",null=True, blank=True)
	personal = models.OneToOneField("PersonalInformation",null=True, blank=True)
	def __unicode__(self):
	    return self.person_id.nickname
		
#
# Family of Person.Students

class Student(Person):
	year_of_entrance = models.IntegerField(null=True,blank=True)
	year_of_graduation = models.IntegerField(null=True,blank=True)
	def __unicode__(self):
	    return self.person_id.nickname
		
class Bachelor(Student):
	def __unicode__(self):
	    return self.person_id.nickname
		
class Specialist(Student):
	def __unicode__(self):
	    return self.person_id.nickname
		
class Master(Student):
	def __unicode__(self):
	    return self.person_id.nickname
		
class Postgraduate(Student):
	def __unicode__(self):
	    return self.person_id.nickname
		
#
# Family of Person.Employee

class Employee(Person):
	post = models.CharField(max_length=50)
	date_of_entrance = models.DateField()
	
class Research_associate(Employee):
	students = models.ManyToManyField(Student)
	scientific = models.CharField(max_length=150)
	
class Worker(Employee):
	pass
	
class Director(Research_associate):
	pass	
		


# Family of Scientific_works
"""
class Scientific_work(models.Model):
	topic = models.CharField(max_length=150)
	year = models.IntegerField()
	university = models.CharField(max_length=100)
	supervisors = models.ManyToManyField(Supervisor)
	
class Course_work(Scientific_work):
	number_of_course = models.IntegerField()
	author = models.ForeignKey(Student)
	
class Thesis_project(Scientific_work):
	thesis_project = models.OneToOneField('Bachelor',null=True,blank=True)
class Thesis(Scientific_work):
	thesis = models.OneToOneField('Specialist',null=True,blank=True)

class Masters_dissertation(Scientific_work):
	masters_dissertation = models.OneToOneField('Master',null=True,blank=True)

class Candidate_dissertation(Scientific_work):
	candidate_dissertation = models.OneToOneField('Postgraduate',null=True,blank=True)

"""

class Publication(models.Model):
	topic = models.CharField(max_length=150,blank=True)
	year = models.IntegerField(blank=True)
	doi = models.CharField(max_length=30,blank=True)
	journal = models.CharField(max_length=150,blank=True)
	place = models.CharField(max_length=150,blank=True)
	conference = models.CharField(max_length=150,blank=True)
	def __unicode__(self):
	    return self.topic

VIDEO_TYPE = (
    ('server', 'Server'),
    ('emded', 'Embed'),
)	

class Content(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	bookmark = models.CharField(max_length=100, blank=True)
	#type = models.CharField(max_length=6, choices=VIDEO_TYPE) #not sure to do this
	def __unicode__(self):
	    return self.name	
	
class Event(models.Model):
	time = models.DateTimeField(null=True,blank=True)
	place = models.CharField(max_length=100,blank=True)
	contents = models.OneToOneField('Content')
	participants = models.ManyToManyField('Person',null=True,blank=True)
	def __unicode__(self):
	    return self.place
		
class Workshop(Event):
	seminarian = models.ManyToManyField('Person',null=True,blank=True)
	task = models.TextField(blank=True)
	materials = models.TextField(blank=True)
	def __unicode__(self):
	    return self.contents.name
		
class Lecture(Event):
	lecturer = models.ManyToManyField('Person',null=True,blank=True)
	task = models.TextField(blank=True)
	materials = models.TextField(blank=True)
	def __unicode__(self):
	    return self.contents.name	
	
class NewsPost(models.Model):
	contents = models.OneToOneField('Content')
	author = models.ManyToManyField('Person',related_name='newspost_author_set',null=True,blank=True)
	time = models.DateTimeField(null=True,blank=True)
	list_events = models.ManyToManyField('Event',null=True,blank=True)
	list_long_term = models.ManyToManyField('LongTermActivity',null=True,blank=True)
	people = models.ManyToManyField('Person',related_name='newspost_people_set',null=True,blank=True)
	def __unicode__(self):
	    return self.contents.name
	
class LongTermActivity(models.Model):
	contents = models.OneToOneField('Content')
	goal = models.TextField(blank=True)
	starts = models.DateTimeField(null=True,blank=True)
	ends = models.DateTimeField(null=True,blank=True)
	events = models.ManyToManyField('Event',null=True,blank=True)
	def __unicode__(self):
	    return self.contents.name

class Course(LongTermActivity):
	instructor = models.ManyToManyField('Person',null=True,blank=True)
	time = models.TimeField(null=True,blank=True)
	prerequisites = models.ForeignKey('self',null=True,blank=True)
	def __unicode__(self):
	    return self.contents.name
		
class Project(LongTermActivity):
	participants = models.ManyToManyField('Person', blank=True)
	repository = models.URLField(blank=True)
	publications = models.ManyToManyField('Publication',null=True,blank=True)
	def __unicode__(self):
	    return self.contents.name


