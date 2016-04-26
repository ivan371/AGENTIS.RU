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
	url(r'list_rieltors_order/$', list_rieltors_order),
	url(r'order_result/$', order_result),
	url(r'ch_off_name/$', ch_off_name),
	url(r'ch_off_sum/$', ch_off_sum),
	url(r'ch_off_mess/$', ch_off_mess),
	url(r'send_mess/$', send_mess),
	url(r'save_mess/$', save_mess),
	url(r'make_offer/$', make_offer),	
	url(r'mess_success/$', mess_success),	
	url(r'chat/$', chat),	
	url(r'filter/$', filter_region),
	url(r'for_rieltors/$', for_rieltors),
	url(r'list/$', lists),
	url(r'profile/$', profile),
	url(r'filter_profil/$', filter_profil),
	url(r'change_self/$', change_self),
	url(r'change_status/$', change_status),
	]
	
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
