from django.conf.urls.defaults import *
from sss.mainpart.views import a_all

urlpatterns = patterns('',
	url(r'^$', a_all),
)