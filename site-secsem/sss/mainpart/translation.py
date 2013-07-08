from modeltranslation.translator import translator, TranslationOptions
from mainpart.models import Identity, PersonalInformation, Employee, Research_associate, Publication, Content, Event, Workshop, Lecture, LongTermActivity

class IdentityTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', "patronymic",)

class PersonalInformationTranslationOptions(TranslationOptions):
	fields = ('biography',)

class EmployeeTranslationOptions(TranslationOptions):
	fields = ('post', )

class Research_associateTranslationOptions(TranslationOptions):
	fields = ('scientific', )

class PublicationTranslationOptions(TranslationOptions):
	fields = ('topic', 'doi', 'journal', 'place', 'conference', )

class ContentTranslationOptions(TranslationOptions):
	fields = ('name', 'description', 'bookmark', )

class EventTranslationOptions(TranslationOptions):
	fields = ('place', )

class WorkshopTranslationOptions(TranslationOptions):
	fields = ('task', 'materials', )

class LectureTranslationOptions(TranslationOptions):
	fields = ('task', 'materials' )

class LongTermActivityTranslationOptions(TranslationOptions):
	fields = ('goal', )

translator.register(Identity, IdentityTranslationOptions)
translator.register(PersonalInformation, PersonalInformationTranslationOptions)
translator.register(Employee, EmployeeTranslationOptions)
translator.register(Research_associate, Research_associateTranslationOptions)
translator.register(Publication, PublicationTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Workshop, WorkshopTranslationOptions)
translator.register(Lecture, LectureTranslationOptions)
translator.register(LongTermActivity, LongTermActivityTranslationOptions)
