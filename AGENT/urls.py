from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from AGENT.views import *

urlpatterns = [
	url(r'^$', index),
	url(r'index', index),
	url(r'enter/$', enter),
	url(r'registration/$', registration),
	url(r'about/$', about),
	url(r'how_work/$', how_work),
	url(r'connection/$', connection),
	url(r'how_rieltors/$', how_rieltors),
	url(r'how_insurance/$', how_insurance),
	url(r'registration_result/$', registration_result),
	url(r'registration_complete/$', registration_complete),
	url(r'enter_result/$', enter_result),
	url(r'enter_success/$', enter_success),
	url(r'exit/$', exit),
	url(r'self_room/$', self_room),
	url(r'orders/$', orders),
	url(r'messagers/$', messagers),
	url(r'ch_email/$', ch_email),
	url(r'ch_number/$', ch_number),
	url(r'ch_prof/$', ch_prof),
	url(r'ch_initial/$', ch_initial),
	url(r'list_rieltors/$', list_rieltors),
	url(r'order_result/$', order_result),
	]
