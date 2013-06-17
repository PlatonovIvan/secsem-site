from django.db import models
from django.contrib import admin
# Create your models here.
class Person(models.Model):
	surname = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	nickname = models.CharField(max_length=30)
	patronymic = models.CharField(max_length=20, blank=True)
	information = models.TextField()
	email = models.EmailField()
	photo = models.CharField(max_length=50)
	def __unicode__(self):
	    return self.surname

class NewsPost(models.Model):
    title = models.CharField(max_length=150)
    preview = models.CharField(max_length=400)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    picture = models.CharField(max_length=50)
    def __unicode__(self):
       return self.title

class Slide(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    picture = models.CharField(max_length=150)
    def __unicode__(self):
       return self.title
	
class Course(models.Model):
    name = models.CharField(max_length=150)
    lector = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    time = models.TimeField()
    annotation = models.CharField(max_length=400)
    def __unicode__(self):
       return self.name

class FAQ(models.Model):
 question = models.TextField()
 answer = models.TextField()
 def __unicode__(self):
    return self.question
	
class Publication(models.Model):
 name = models.CharField(max_length=150)
 all_info = models.TextField()
 picture = models.CharField(max_length=50)
 def __unicode__(self):
   return self.name
	
VIDEO_TYPE = (
    ('server', 'Server'),
    ('emded', 'Embed'),
)	
class VideoCourse(models.Model):
 name = models.CharField(max_length=150)
 annotation = models.CharField(max_length=400)    
 path = models.CharField(max_length=70)
 type = models.CharField(max_length=6, choices=VIDEO_TYPE)
 def __unicode__(self):
    return self.name

class Project(models.Model):
 name = models.CharField(max_length=150)
 all_info = models.TextField()
 link = models.URLField()
 def __unicode__(self):
   return self.name 

class Studying(models.Model):
 title = models.CharField(max_length=150)
 all_info = models.TextField()
 timestamp = models.DateTimeField(blank=True)
 author = models.CharField(max_length=50, blank=True)
 def __unicode__(self):
   return self.title

	
admin.site.register(Person)
admin.site.register(Slide)
admin.site.register(VideoCourse)
admin.site.register(Course)
admin.site.register(NewsPost)
admin.site.register(FAQ)
admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(Studying)