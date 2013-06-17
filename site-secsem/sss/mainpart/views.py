# Create your views here.
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from mainpart.models import *

def persons(request, person_id):
  mans = Person.objects.all()
  contain = False
  if len(mans) == 0:
   title = "Mans"
   tt = loader.get_template('mainpart/blank_person.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
#  try:
#   person_id = str(person_id)
#  except ValueError:
#   raise Http404()
  if person_id == 0:
   contain = True
   cur = mans[0]
  else:
   for man in mans:
    if man.nickname == person_id:
     contain = True
     cur = man
     break
  if contain == False:
   raise Http404()
#    if len(mans) < person_id:
#	    person_id = len(mans)
  t = loader.get_template('mainpart/person.html')
  c = RequestContext(request, {
     'mans': mans, 'cur': cur
  })
  return HttpResponse(t.render(c))
	
def main(request):
  mans = Person.objects.all().order_by('-id')[:2]
  coursess = Course.objects.all()
  all_video = VideoCourse.objects.all()
  if len(all_video) == 0:
   video = all_video
   videotype = 2
  else:
   video = all_video[len(all_video)-1]
   if video.type == "server":
    videotype = 1
   else:
    videotype = 0
  news = NewsPost.objects.all().order_by('-id')[:2]  
  sliders = Slide.objects.all()
  t = loader.get_template('mainpart/main.html')
  c = RequestContext(request, {
      'persons': mans,
	  'sliders': sliders,
	  'newsposts': news,
	  'videocourse': video,
	  'courses': coursess,
	  'videotype': videotype
  })
  return HttpResponse(t.render(c))    	
  
def publications(request, pub_id):
  pubs = Publication.objects.all()
  if len(pubs) == 0:
   title = "Studyings"
   tt = loader.get_template('mainpart/blank_publications.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
  contain = False
  try:
   pub_id = int(pub_id)
  except ValueError:
   raise Http404()
  if pub_id == 0:
   contain = True
   cur = pubs[0]
  else:
   for pub in pubs:
    if pub.id == pub_id:
     contain = True
     cur = pub
     break
  if contain == False:
   raise Http404()
  t = loader.get_template('mainpart/publications.html')
  c = RequestContext(request, {
     'publications': pubs, 'cur': cur
  })
  return HttpResponse(t.render(c))

def faq(request, faq_id):
  faqs = FAQ.objects.all()
  if len(faqs) == 0:
   title = "Studyings"
   tt = loader.get_template('mainpart/blank_faq.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
  contain = False
  try:
   faq_id = int(faq_id)
  except ValueError:
   raise Http404()
  if faq_id == 0:
   contain = True
   cur = faqs[0]
  else:
   for faq in faqs:
    if faq.id == faq_id:
     contain = True
     cur = faq
     break
  if contain == False:
   raise Http404()
  t = loader.get_template('mainpart/faq.html')
  c = RequestContext(request, {
     'faqs': faqs, 'cur': cur
  })
  return HttpResponse(t.render(c))

def project(request, project_id):
  projects = Project.objects.all()
  if len(projects) == 0:
   title = "Studyings"
   tt = loader.get_template('mainpart/blank_project.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
  contain = False
  try:
   project_id = int(project_id)
  except ValueError:
   raise Http404()
  if project_id == 0:
   contain = True
   cur = projects[0]
  else:
   for project in projects:
    if project.id == project_id:
     contain = True
     cur = project
     break
  if contain == False:
   raise Http404()
  t = loader.get_template('mainpart/project.html')
  c = RequestContext(request, {
     'projects': projects, 'cur': cur
  })
  return HttpResponse(t.render(c))  

def courses(request, course_type, course_id):
  courses = Course.objects.all()
  videos = VideoCourse.objects.all()
  total_len = len(courses)+len(videos)
  
  if total_len == 0:
   title = "Courses"
   tt = loader.get_template('mainpart/blank_courses.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
   
  if len(courses) == 0:
   course_type = 1
   
  contain = False
  try:
   course_type = int(course_type)
  except ValueError:
   raise Http404()  
  if course_type != 1 and course_type != 0:
   raise Http404()
  if course_type == 0:
   try:
    course_id = int(course_id)
   except ValueError:
    raise Http404()
   if course_id == 0:
    contain = True
    cur = courses[0]
   else:
    for course in courses:
     if course.id == course_id:
      contain = True
      cur = course
      break
   if contain == False:
    raise Http404()
   videotype = 2
	
  if course_type == 1:
   try:
    course_id = int(course_id)
   except ValueError:
    raise Http404()
   if course_id == 0:
    contain = True
    cur = videos[0]
   else:
    for video in videos:
     if video.id == course_id:
      contain = True
      cur = video
      break
   if contain == False:
    raise Http404()  
   if cur.type == "server":
    videotype = 1
   else:
    videotype = 0
  
  t = loader.get_template('mainpart/courses.html')
  c = RequestContext(request, {
     'courses': courses, 'cur': cur,
	 'videotype': videotype, 'ttype': course_type,
	 'videos': videos
  })
  return HttpResponse(t.render(c))  
  
def studying(request, studying_id):
  studyings = Studying.objects.all()
  if len(studyings) == 0:
   title = "Studyings"
   tt = loader.get_template('mainpart/blank_studying.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
  contain = False
  try:
   studying_id = int(studying_id)
  except ValueError:
   raise Http404()
  if studying_id == 0:
   contain = True
   cur = studyings[0]
  else:
   for studying in studyings:
    if studying.id == studying_id:
     contain = True
     cur = studying
     break
  if contain == False:
   raise Http404()
  t = loader.get_template('mainpart/studying.html')
  c = RequestContext(request, {
     'studyings': studyings, 'cur': cur
  })
  return HttpResponse(t.render(c))  
  
def news(request, new_id):
  news = NewsPost.objects.all()
  if len(news) == 0:
   title = "Studyings"
   tt = loader.get_template('mainpart/blank_news.html')
   cc = RequestContext(request, {
	'title': title
   })
   return HttpResponse(tt.render(cc))
  contain = False
  try:
   new_id = int(new_id)
  except ValueError:
   raise Http404()
  if new_id == 0:
   contain = True
   cur = news[0]
  else:
   for new in news:
    if new.id == new_id:
     contain = True
     cur = new
     break
  if contain == False:
   raise Http404()
  t = loader.get_template('mainpart/news.html')
  c = RequestContext(request, {
     'news': news, 'cur': cur
  })
  return HttpResponse(t.render(c))  