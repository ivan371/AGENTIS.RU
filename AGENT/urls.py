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
	url(r'index', views.index, name='index'),
	url(r'enter/$', views.enter, name='enter'),
	url(r'registration/$', views.registration, name='registration'),
	url(r'about/$', views.about, name='about'),
	url(r'how_work/$', views.how_work, name='how_work'),
	url(r'connection/$', views.connection, name='connection'),
	url(r'how_rieltors/$', views.how_rieltors, name='how_rieltors'),
	url(r'how_insurance/$', views.how_insurance, name='how_insurance'),
	url(r'registration_result/$', views.registration_result, name='registration_result'),
	url(r'registration_complete/$', views.registration_complete, name='registration_complete'),
	url(r'enter_result/$', views.enter_result, name='enter_result'),
	url(r'enter_success/$', views.enter_success, name='enter_success'),
	url(r'exit/$', views.exit, name='exit'),
	url(r'self_room/$', views.self_room, name='selt_room'),
	url(r'orders/$', views.orders, name='orders'),
	url(r'messagers/$', views.messagers, name='messagers'),
	url(r'ch_email/$', views.ch_email, name='ch_email'),
	url(r'ch_number/$', views.ch_number, name='ch_number'),
	url(r'ch_prof/$', views.ch_prof, name='ch_prof'),
	url(r'ch_initial/$', views.ch_initial, name='ch_initital'),
	url(r'list_rieltors/$', views.list_rieltors, name='list_rieltors'),
	url(r'list_rieltors_order/$', views.list_rieltors_order, name='list_rieltors_order'),
	url(r'order_result/$', views.order_result, name='order_result'),
	url(r'ch_off_name/$', views.ch_off_name, name='ch_off_name'),
	url(r'ch_off_sum/$', views.ch_off_sum, name='ch_off_sum'),
	url(r'ch_off_mess/$', views.ch_off_mess, name='ch_off_mess'),
	url(r'send_mess/$', views.send_mess, name='send_mess'),
	url(r'save_mess/$', views.save_mess, name='save_mess'),
	url(r'make_offer/$', views.make_offer, name='make_offer'),	
	url(r'mess_success/$', views.mess_success, name='mess_success'),	
	url(r'chat/$', views.chat, name='chat'),	
	url(r'filter/$', views.filter_region, name='filter_region'),
	url(r'filter_spec/$', views.filter_spec, name='filter_spec'),
	url(r'for_rieltors/$', views.for_rieltors, name='for_rieltors'),
	url(r'list/$', views.lists, name='lists'),
	url(r'profile/$', views.profile, name='profile'),
	url(r'filter_profil/$', views.filter_profil, name='filter_profil'),
	url(r'change_self/$', views.change_self, name='change_self'),
	url(r'change_status/$', views.change_status, name='change_status'),
	url(r'messagers_all/$', views.messagers_all, name='messagers_all'),
	url(r'more/$', views.more, name='more'),
	]
	
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
