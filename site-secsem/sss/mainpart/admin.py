from django.contrib import admin
from mainpart.models import *
from modeltranslation.admin import TranslationAdmin


class IdentityAdmin(TranslationAdmin):

	list_display = ('surname', 'name', 'patronymic',)
	fieldsets = [
		(u'Identity', {
			'fields': [
				'surname',
				'name',
				'patronymic',
				'nickname',
			]
		}),
	]

	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
	
	def get_model_perms(self, request):
		return {}


class ContactInformationAdmin(admin.ModelAdmin):
	list_display = ('email', 'phone_number', 'social_network1', 'social_network3', 'social_network3')
	fieldsets = [
		(u'Contact Information', {
			'fields': [
				'email',
				'phone_number',
				'social_network1',
				'social_network2',
				'social_network3',
			]
		}),
	]
	def get_model_perms(self, request):
		return {}


class PersonalInformationAdmin(TranslationAdmin):

	list_display = ('photo', 'biography',)
	fieldsets = [
		(u'Additional PersonalInformation', {
			'fields': [
				'photo',
				'biography',
				'publications',
			]
		}),
	]
	filter_vertical = ('publications', )		
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
	
	def get_model_perms(self, request):
		return {}

class PersonAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'contacts', 'personal')
	def get_model_perms(self, request):
		return {}


	

class StudentAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'contacts', 'year_of_entrance', 'year_of_graduation')
	def get_model_perms(self, request):
		return {}



class BachelorAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'contacts', 'year_of_entrance', 'year_of_graduation')
	list_filter = ['year_of_graduation']
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Years of Studying', {
			'fields': [
				'year_of_entrance',
				'year_of_graduation',
			]
		}),	
	]

class SpecialistAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'contacts', 'year_of_entrance', 'year_of_graduation')	
	list_filter = ['year_of_graduation']
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Years of Studying', {
			'fields': [
				'year_of_entrance',
				'year_of_graduation',
			]
		}),

	]

class MasterAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'contacts', 'year_of_entrance', 'year_of_graduation')
	list_filter = ['year_of_graduation']
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Years of Studying', {
			'fields': [
				'year_of_entrance',
				'year_of_graduation',
			]
		}),
	]

class PostgraduateAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'contacts', 'year_of_entrance', 'year_of_graduation')
	list_filter = ['year_of_graduation']
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Years of Studying', {
			'fields': [
				'year_of_entrance',
				'year_of_graduation',
			]
		}),

	]

class EmployeeAdmin(TranslationAdmin):
    
	list_display = ('person_id', 'post', 'date_of_entrance')
	list_filter = ['date_of_entrance']
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
	
	def get_model_perms(self, request):
		return {}



class Research_associateAdmin(TranslationAdmin):
    
	list_display = ('person_id', 'post', 'scientific')
	list_filter = ['date_of_entrance']
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Employee Information', {
			'fields': [
				'post',
				'date_of_entrance',
				'students',
				'scientific',
			]
		}),
	]
	
	filter_vertical = ('students', )	


	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class WorkerAdmin(admin.ModelAdmin):
	list_display = ('person_id', 'post', 'date_of_entrance')
	list_filter = ['date_of_entrance']
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Employee Information', {
			'fields': [
				'post',
				'date_of_entrance',
			]
		}),

	]

class DirectorAdmin(admin.ModelAdmin):
	
	list_display = ('person_id', 'post', 'scientific')
	fieldsets = [
		(u'General Personal Information', {
			'fields': [
				'person_id',
			]
		}),
		(u'Conatact Information', {
			'fields': [	
				'contacts',
			]
		}),
		(u'Additional Personal Information', {
			'fields': [
				'personal',
			]
		}),
		(u'Employee Information', {
			'fields': [
				'post',
				'date_of_entrance',
				'students',
				'scientific',
			]
		}),
	]
	filter_vertical = ('students', )	
 	

class PublicationAdmin(TranslationAdmin):
    
	list_display = ('topic', 'doi', 'journal', 'place', 'conference',)
	list_filter = ['year', 'place']
	fieldsets = [
		(u'Publication', {
			'fields': [
				'topic',
				'doi',
				'journal',
				'place',
				'conference',
				'year',
				'tags',
			]
		}),
	]
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class ContentAdmin(TranslationAdmin):
    
	list_display = ('name', 'description', 'bookmark')
	fieldsets = [
		(u'Content', {
			'fields': [
				'name',
				'description',
				'bookmark',
			]
		}),
	]
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
	def get_model_perms(self, request):
		return {}


class EventAdmin(TranslationAdmin):
    
	display_list = ('place', 'time', 'contents', 'participants')
	list_filter = ['place', 'time']
	fieldsets = [
		(u'Event', {
			'fields': [
				'place',
				'time',
				'contents',
				'participants',
			]
		}),
	]
	filter_vertical = ('participants', )	
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
	def get_model_perms(self, request):
		return {}

	
class WorkshopAdmin(TranslationAdmin):  
	display_list = ('place', 'time', 'seminarian', 'task')
	list_filter = ['place', 'time']
	fieldsets = [
		(u'WorkShop', {
			'fields': [
				'time',
				'place',
				'contents',
				'participants',
				'seminarian',
				'task',
				'materials',
			]
		}),
	]
	filter_vertical = ('participants', )	
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class LectureAdmin(TranslationAdmin):
    
	display_list = ('place', 'time', 'lecturer', 'task')
	list_filter = ['place', 'time']
	fieldsets = [
		(u'Lecture', {
			'fields': [
				'time',
				'place',
				'contents',
				'participants',
				'lecturer',
				'task',
				'materials',
			]
		}),
	]
	filter_vertical = ('participants', )	
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class NewsPostAdmin(admin.ModelAdmin):
	display_list = ('contents', 'author', 'time', 'list_events')
	list_filter = ['author', 'time']
	#date_hierarhy = 'time'
	fieldsets = [
		(u'News Post', {
			'fields': [
				'contents',
				'author',
				'time',
				'list_events',
				'list_long_term',
				'people',
			]
		}),
	]
	filter_vertical = ('author', )	



class LongTermActivityAdmin(TranslationAdmin):
    
	display_list = ('contents', 'goal', 'starts', 'ends', 'events')
	fieldsets = [
		(u'Long Term Activity', {
			'fields': [
				'contents',
				'goal',
				'starts',
				'ends',
				'events',
			]
		}),
	]
	filter_vertical = ('events', )	
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

	def get_model_perms(self, request):
		return {}


class CourseAdmin(admin.ModelAdmin):
	display_list = ('contents', 'goal', 'starts', 'ends', 'instructor')
	list_filter = ['starts', 'ends']
	fieldsets = [
		(u'Course', {
			'fields': [
				'instructor',
				'time',
				'prerequisites',
			]
		}),
	]
	filter_vertical = ('instructor',)	

class ProjectAdmin(admin.ModelAdmin):
	display_list = ('contents', 'goal', 'starts', 'ends', 'participants', 'repository')
	list_filter = ['starts', 'ends']
	fieldsets = [
		(u'Project', {
			'fields': [
				'participants',
				'repository',
				'publications',
			]
		}),
	]
	filter_vertical = ('participants', 'publications')	


admin.site.register(Identity, IdentityAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Bachelor, BachelorAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Postgraduate, PostgraduateAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Research_associate, Research_associateAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(LongTermActivity, LongTermActivityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Project, ProjectAdmin)
