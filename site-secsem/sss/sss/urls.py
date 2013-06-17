from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sss.views.home', name='home'),
    # url(r'^sss/', include('sss.foo.urls')),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
    url(r'^persons/(\w+)/$', 'mainpart.views.persons'),
	url(r'^publications/(\d+)/$', 'mainpart.views.publications'),
	url(r'^faq/(\d+)/$', 'mainpart.views.faq'),
	url(r'^project/(\d+)/$', 'mainpart.views.project'),
	url(r'^studying/(\d+)/$', 'mainpart.views.studying'),
	url(r'^courses/(\d+)/(\d+)/$', 'mainpart.views.courses'),
	url(r'^news/(\d+)/$', 'mainpart.views.news'),
	url(r'^$', 'mainpart.views.main'),
)