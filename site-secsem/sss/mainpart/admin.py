from django.contrib import admin
from mainpart.models import Identity, PersonalInformation, Employee, Research_associate, Publication, Content, Event, Workshop, Lecture, LongTermActivity
from modeltranslation.admin import TranslationAdmin

class IdentityAdmin(TranslationAdmin):
	list_display = ('surname', 'name', 'patronymic')
	fieldsets = [
		(u'Identity', {
			'fields': [
				'name',
				'surname',
				'patronymic',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class PersonalInformationAdmin(TranslationAdmin):
    
	fieldsets = [
		(u'PersonalInformation', {
			'fields': [
				'biography',
			]
		}),
	]
	group_fieldsets = True
	
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
	
class EmployeeAdmin(TranslationAdmin):
    
	fieldsets = [
		(u'Emplyee', {
			'fields': [
				'post',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class Research_associateAdmin(TranslationAdmin):
    
	fieldsets = [
		(u'Research Associate', {
			'fields': [
				'scientific',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class PublicationAdmin(TranslationAdmin):
    
	list_display = ('topic',)
	fieldsets = [
		(u'Publication', {
			'fields': [
				'topic',
				'doi',
				'journal',
				'place',
				'conference',
			]
		}),
	]
	group_fieldsets = True
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
    
	list_display = ('name', )
	fieldsets = [
		(u'Content', {
			'fields': [
				'name',
				'description',
				'bookmark',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class EventAdmin(TranslationAdmin):
    
	display_list = ('place', )
	fieldsets = [
		(u'Event', {
			'fields': [
				'place',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

	
class WorkshopAdmin(TranslationAdmin):
    
	fieldsets = [
		(u'WorkShop', {
			'fields': [
				'task',
				'materials',
			]
		}),
	]
	group_fieldsets = True
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
    
	fieldsets = [
		(u'Lecture', {
			'fields': [
				'task',
				'materials',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

class LongTermActivityAdmin(TranslationAdmin):
    
	fieldsets = [
		(u'Identity', {
			'fields': [
				'goal',
			]
		}),
	]
	group_fieldsets = True
	class Media:

		js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
		css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Identity, IdentityAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Research_associate, Research_associateAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(LongTermActivity, LongTermActivityAdmin)

