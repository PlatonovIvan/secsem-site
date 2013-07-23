# Create your views here.
from django.utils.translation import ugettext as _
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from mainpart.models import *

def persons(request, person_id):

	persons = Person.objects.all()
	director = Director.objects.all()
	workers = Worker.objects.all()
	res_ass = Research_associate.objects.all()
	postgrs = Postgraduate.objects.all()
	masters = Master.objects.all()
	specs = Specialist.objects.all()
	bachs = Bachelor.objects.all()
	total_len = len(director) + len(workers) + len(res_ass) + len(postgrs) + \
				 len(masters) + len(specs) + len(bachs) 
	if total_len == 0:
		title = "Mans"
		tt = loader.get_template('mainpart/blank_person.html')
		cc = RequestContext(request, {
			'title': title
		})
		return HttpResponse(tt.render(cc))
	try:
		cur = []
		person_id = str(person_id)
		if (person_id.isdigit()):
			person_id = int(person_id)
			p = persons.get(id = person_id)
			if (director.get(id = person_id)):
				cur = director.get(id = person_id)
				person_type = "director"
			elif (workers.get(id = person_id)):
				cur = workers.get(id = person_id)
				person_type = "worker"
			elif (res_ass.get(id = person_id)):
				cur = res_ass.get(id = person_id)
				person_type = "res_ass"
			elif (postgrs.get(id = person_id)):
				cur = postgrs.get(id = person_id)
				person_type = "postgr"
			elif (masters.get(id = person_id)):
				cur = masters.get(id = person_id)
				person_type = "master"
			elif (specs.get(id = person_id)):
				cur = specs.get(id = person_id)
				person_type = "spec"
			elif (bachs.get(id = person_id)):
				cur = bachs.get(id = person_id)
				person_type = "bach"
			else:
				raise Http404()
		else:
			cur={}
			person_id_old = person_id
			if ((person_id == "director") or (person_id == "all")) and (len(director)!=0):
				cur['director']=director
				person_type = "director"
			if ((person_id == "researcher") or (person_id == "all")) and (len(res_ass)!=0):
				cur['res_ass']=res_ass
				person_type = "res_ass"
			if ((person_id == "workers") or (person_id == "all")) and (len(workers)!=0):
				cur['workers'] = workers
				person_type = "worker"
			if (person_id == "postgraduate") or (person_id == "all"):
				if (len(postgrs)!=0):
					cur['postgrs'] = postgrs
					person_type = "postgr"
				if (len(masters)!=0):
					cur['masters'] = masters
					person_type = "master"
			if (person_id == "student") or (person_id == "all"):
				if (len(specs)!=0):
					cur['specs'] = specs
					person_type = "spec"
				if (len(bachs)!=0):
					cur['bachs'] = bachs
					person_type = "bach"

			if (person_id_old == "all"):
				person_type = "all"

			if ( len(cur)==0):
				raise Http404()
		
  		t = loader.get_template('mainpart/person.html')
  		c = RequestContext(request, {
			'cur': cur,
			'person_id':person_id,
			'person_type': person_type
  		})
  		return HttpResponse(t.render(c))
	except ValueError:
		title = "Mans"
		tt = loader.get_template('mainpart/blank_person.html')
		cc = RequestContext(request, {
			'title': title
		})
		return HttpResponse(tt.render(cc))
		#raise Http404()



def main(request):
	directors = Director.objects.all()
	res_ass = Research_associate.objects.all()
	workers = Worker.objects.all()
	publications = Publication.objects.all()
  	"""
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
  	"""
  	news = NewsPost.objects.all().order_by('-id')[:2]  
  	
  	#sliders = Slide.objects.all()

  	t = loader.get_template('mainpart/main.html')
  	c = RequestContext(request, {
      		'directors': directors,
			'res_ass': res_ass,
			'workers': workers,
	 		# 'sliders': sliders,
	  		'newsposts': news,
	 		# 'videocourse': video,
	 		# 'courses': coursess,
	 		# 'videotype': videotype,
  	})
	
  	return HttpResponse(t.render(c))    	

def publications(request, pub_year):
	pubs = Publication.objects.all()
	years = sorted(pubs.values_list('year', flat = True), reverse = True)
	if len(pubs) == 0:
		title = "Studyings"
		tt = loader.get_template('mainpart/blank_publications.html')
		cc = RequestContext(request, {
		'title': title
		})
		return HttpResponse(tt.render(cc))
	
	try:
		pub_year = int(pub_year)
	except ValueError:
		raise Http404()
	
	contain = False
	if pub_year == 0:
		contain=True
		ordered_pubs = pubs.order_by('year').reverse()
	
	else:
		ordered_pubs = pubs.filter(year__exact = pub_year)
		print ordered_pubs
		if (ordered_pubs):
			contain = True
		
	if contain == False:
		raise Http404()
	
	t = loader.get_template('mainpart/publications.html')
	c = RequestContext(request, {
     	'publications': ordered_pubs,
     	'years': years,
		'pub_year': pub_year
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
		project_id = str(project_id)
		project_type = ""
		if (project_id.isdigit()):
			project_id = int(project_id)
			cur = projects.get(id = project_id)
			project_type = "Special"
			if (not cur):
				raise Http404()
		else:
			cur = projects
			project_type = "All"
		t = loader.get_template('mainpart/project.html')
		c = RequestContext(request, {
			'projects': projects,
			'cur': cur,
			'project_type': project_type
		})
		return HttpResponse(t.render(c))  
	except ValueError:
		raise Http404()

def courses(request, course_type, course_id):
  	
	try:	
		lections = Lecture.objects.all()
		workshops = Workshop.objects.all()
		courses = Course.objects.all()
		total_len = len(lections) + len(workshops)+ len(courses)
		if (total_len == 0):
			title = "Courses"
			tt = loader.get_template('mainpart/blank_courses.html')
			cc = RequestContext(request, {
				'title': title
			})
		course_id = int(course_id)
		if (course_type == "lection"):
			cur = lections
			if (cur):
				raise Http404()
		elif (course_type == "workshop"):
			cur = workshops
			if (cur):
				raise Http404()
		elif (course_type == "course"):
			cur = courses
			if (cur):
				raise Http404()
		elif (course_type == "all"):
			cur = []
		else:	
			raise Http404()

		t = loader.get_template('mainpart/courses.html')
		c = RequestContext(request, {
     		'cur': cur,
			'course_type': course_type
  		})
		return HttpResponse(t.render(c))  
	except ValueError:
		raise Http404()

def studying(request, studying_id):
	try:
		studying_id = int (studying_id)
		if (studying_id < 0) or (studying_id > 4):
			raise Http404()
		t = loader.get_template('mainpart/studying.html')
		c = RequestContext(request, {
			'studying_id':studying_id
		})
		return HttpResponse(t.render(c))
	except ValueError:
		raise Http404()  
	
def news(request, new_id):
	news = NewsPost.objects.all()
	news = news.order_by('time')
  	if len(news) == 0:
   		title = "Studyings"
   		tt = loader.get_template('mainpart/blank_news.html')
   		cc = RequestContext(request, {
			'title': title
   		})
   		return HttpResponse(tt.render(cc))
  	contain = False
  	
	try:
   		new_id = str(new_id)
		news_type = ""
		if (new_id.isdigit()):
			cur = news.get(id = new_id)
			news_type = "Special"
			if (not cur):
				raise Http404()
			else:
				contain = True
		else:
			cur = news
			news_type = "All"
  		t = loader.get_template('mainpart/news.html')
 		c = RequestContext(request, {
     		'news': news, 
     		'cur': cur,
			'news_type': news_type
  		})
  		return HttpResponse(t.render(c)) 	
	except ValueError:
   		raise Http404()

def about(request, about_type):
  	t = loader.get_template('mainpart/about.html')
  	c = RequestContext(request, {
     	'about_type': about_type
  	})
  	return HttpResponse(t.render(c))

def tags(request, req_tag):
	publications = Publication.objects.filter(tags__name = req_tag)	
	workshops = Workshop.objects.filter(tags__name = req_tag)
	lectures = Lecture.objects.filter(tags__name = req_tag)
	news = NewsPost.objects.filter(tags__name = req_tag)
	courses = Course.objects.filter(tags__name = req_tag)
	projects = Project.objects.filter(tags__name = req_tag)
	total_len = len(publications)+len(workshops)+len(lectures)+\
				len(news)+len(courses)+len(projects)
	if (total_len == 0):
		title = "Search Results"
   		tt = loader.get_template('mainpart/blank_tags.html')
   		cc = RequestContext(request, {
			'title': title
   		})
   		return HttpResponse(tt.render(cc))

	t = loader.get_template('mainpart/tags.html')
  	c = RequestContext(request, {
     	'publications': publications,
		'workshops': workshops,
		'lectures': lectures,
		'news': news,
		'courses': courses,
		'projects': projects,
  	})
  	return HttpResponse(t.render(c))

