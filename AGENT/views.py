#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.template import *
from django import template
from django.template.loader import get_template
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.forms import forms
from django.template import RequestContext
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import modelform_factory
from django.core.files import File

from .models import User_AGENTIS
from .models import orders_data
from .models import message
from .models import order
from .models import image
from .forms import MediaModel
from .display_mess import display_mess

def index(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/index.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/index.html', RequestContext(request))	

def for_rieltors(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/for_rieltors.html',{'p': p, 'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/for_rieltors.html', RequestContext(request))
	
def enter(request):
	return render(request, 'AGENTIS/enter.html')

def orders(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	if p.who == 2:
		o = order.objects.filter(order_to = p)
	else:
		o = order.objects.filter(order_from = p)
	mess = display_mess(p)
	is_mess = mess.is_mes()
	return render_to_response('AGENTIS/orders.html',{'p': p, 'o': o, 'is_mess': is_mess}, RequestContext(request))

def chat(request):
	c = {}
	c.update(csrf(request))
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	mess = display_mess(p)
	is_mess = mess.is_mes()
	errors = []
	if request.method == 'POST':
		POST = request.POST
		if p.who == 2:
			ms = message(mess_to = User_AGENTIS.objects.get(login = request.session['member_id']),
					mess_from = User_AGENTIS.objects.get(login = POST['name']),
					status = 0,
					message = POST['message'],
					author = 1,
					) 
			ms.save()
		else:
			ms = message(mess_from = User_AGENTIS.objects.get(login = request.session['member_id']),
					mess_to = User_AGENTIS.objects.get(login = POST['name']),
					status = 0,
					message = POST['message'],
					author = 0,
					) 
			ms.save()
		return redirect('messagers/')

def messagers(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	mess = display_mess(p)
	is_mess = mess.is_mes()
	ps = mess.nm
	for pss in ps:
		print(pss)
		
	return render_to_response('AGENTIS/messager.html',{'p': p, 'm': mess.nm, 'who': p.who, 'is_mess': is_mess}, RequestContext(request))


@csrf_exempt
def change_status(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		print(POST['name'])
		p = User_AGENTIS.objects.get(login = POST['name'])
		if(p.who == 1):
			m = message.objects.filter(mess_from = p)
		else:
			m = message.objects.filter(mess_to = p)
		for mess in m:
			mess.status = 1
			mess.save()
		#mess = display_mess(p)
		#is_mess = mess.is_mes()
		#mess.clear_status(POST['name'])
	return HttpResponse (content_type="application/json")

def exit(request):
	auth.logout(request)
	return render(request, 'AGENTIS/index.html')

def filter_region(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		print(POST['region'])
		if POST['region'] == '1':
			errors.append('Выберите регион')
			offs = orders_data.objects.all()
			return render_to_response('AGENTIS/list_rieltors_order.html',{'errors': errors[0], 'offs': offs}, RequestContext(request))
		p = User_AGENTIS.objects.filter(region = POST['region'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		offs = orders_data.objects.filter(user_m = p)
		return render_to_response('AGENTIS/list_rieltors_order.html',{'offs': offs, 'is_mess': is_mess}, RequestContext(request))

def filter_profil(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		print(POST['region'])
		if POST['region'] == '1':
			errors.append('Выберите регион')
			p = User_AGENTIS.objects.filter(who = 1)
			mess = display_mess(p)
			is_mess = mess.is_mes()
			return render_to_response('AGENTIS/profile.html',{'errors': errors[0], 'ps': p, 'is_mess': is_mess}, RequestContext(request))
		p = User_AGENTIS.objects.filter(region = POST['region'], who = 1)
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/profile.html',{'ps': p, 'is_mess': is_mess}, RequestContext(request))
	
def ch_off_name(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		offs = orders_data.objects.filter(user_m = p, name_mess = POST['off_name_old'])
		for offers in offs:
			offers.name_mess = POST['off_name']
			offers.save()
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		offs = orders_data.objects.filter(user_m = p)
		return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs, 'is_mess': is_mess}, RequestContext(request))
	
def ch_off_sum(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		offs = orders_data.objects.filter(user_m = p, sum_mess = POST['off_sum_old'])
		for offers in offs:
			offers.sum_mess = POST['off_sum']
			print('off_sum')
			offers.save()
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		offs = orders_data.objects.filter(user_m = p)
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs, 'is_mess': is_mess}, RequestContext(request))

def ch_off_mess(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		offs = orders_data.objects.filter(user_m = p, message = POST['off_mess_old'])
		for offers in offs:
			offers.message = POST['off_mess']
			offers.save()
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		offs = orders_data.objects.filter(user_m = p)
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs, 'is_mess': is_mess}, RequestContext(request))

def ch_email(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		if POST.get('email') and '@' not in POST['email']:
			errors.append('Ваш новый e-mail не корректен.')
			return render_to_response('AGENTIS/self_room.html', {'errors': errors[0], 'p': p,'is_mess': is_mess}, RequestContext(request))
		p.email	= POST['email']
		p.save()
	return render_to_response('AGENTIS/self_room.html',{'p': p ,'is_mess': is_mess}, RequestContext(request))

def ch_number(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		if POST.get('email') and not request.POST['number'].isdigit():
			errors.append('Ваш новый номер не корректен.')
			return render_to_response('AGENTIS/self_room.html',{'errors': errors[0], 'p': p,'is_mess': is_mess}, RequestContext(request))
		p.number = POST['number']
		p.save()
	return render_to_response('AGENTIS/self_room.html',{'p': p,'is_mess': is_mess}, RequestContext(request))

def ch_prof(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		p.who	= POST['who']
		p.save()
		mess = display_mess(p)
		is_mess = mess.is_mes()
	return render_to_response('AGENTIS/self_room.html',{'p': p,'is_mess': is_mess}, RequestContext(request))

def ch_initial(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		#if POST.get('surname') and POST.get('forename') and POST.get('partronyname'):
		#	errors.append('Ваши новые инициалы не корректны')
		#	return render_to_response('AGENTIS/self_room.html',{'errors': errors[0], 'p': p}, RequestContext(request))
		p.surname = POST['surname']
		p.forename = POST['forename']
		p.partronyname = POST['partronyname']
		p.save()
		mess = display_mess(p)
		is_mess = mess.is_mes()
	return render_to_response('AGENTIS/self_room.html',{'p': p,'is_mess': is_mess}, RequestContext(request))

def self_room(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	offs = orders_data.objects.filter(user_m = p)
	mess = display_mess(p)
	is_mess = mess.is_mes()
	count = mess.count_mess(p.who)
	return render_to_response('AGENTIS/self_room.html',{'p': p, 'offs': offs,'is_mess': is_mess, 'count': count}, RequestContext(request))
	
def change_self(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	mess = display_mess(p)
	is_mess = mess.is_mes()
	return render_to_response('AGENTIS/change_self.html',{'p': p,'is_mess': is_mess}, RequestContext(request))

def registration(request):
	return render(request, 'AGENTIS/registration.html')

def list_rieltors(request):
	offers_list = {'name_mess', 'sum_mess'}
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	mess = display_mess(p)
	is_mess = mess.is_mes()
	offs = orders_data.objects.filter(user_m = p)
	for offers in offs:
		offers.img.img = offers.img.goodname()
	return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs,'is_mess': is_mess}, RequestContext(request))
	
def list_rieltors_order(request):
	offs = orders_data.objects.all()
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/list_rieltors_order.html',{'offs': offs,'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/list_rieltors_order.html',{'offs': offs}, RequestContext(request))

def lists(request):
	offs = orders_data.objects.all()
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/list.html',{'offs': offs, 'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/list.html',{'offs': offs}, RequestContext(request))

def profile(request):
	ps = User_AGENTIS.objects.filter(who = 1)
	for pss in ps:
		pss.img.img = pss.img.goodname()
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/profile.html',{'ps': ps, 'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/profile.html',{'ps': ps}, RequestContext(request))


def mess_success(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/mess_success.html',{'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/mess_success.html', RequestContext(request))

def make_offer(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		o = order(order_from = User_AGENTIS.objects.get(login = request.session['member_id']),
					order_to = User_AGENTIS.objects.get(login = POST['name']),
					status = 0,
					href_order = POST['name_mess']
				)
		o.save()
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/make_offer.html', {'p': p, 'name': POST['name'], 'is_mess': is_mess},  RequestContext(request))

def send_mess(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		print(POST['name'])
		print(request.session['member_id'])
		try:
			p = User_AGENTIS.objects.get(login = request.session['member_id'])
			mess = display_mess(p)
			is_mess = mess.is_mes()
			return render_to_response('AGENTIS/send_mess.html', {'name': POST['name'], 'is_mess': is_mess},  RequestContext(request))
		except:
			return render_to_response('AGENTIS/send_mess.html', {'name': POST['name']},  RequestContext(request))

def save_mess(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		print(POST['name'])
		print(request.session['member_id'])
		m = message(mess_from = User_AGENTIS.objects.get(login = request.session['member_id']),
					mess_to = User_AGENTIS.objects.get(login = POST['name']),
					status = 0,
					message = POST['message'],
					author = 0,
					) 
		m.save()
		try:
			p = User_AGENTIS.objects.get(login = request.session['member_id'])
			mess = display_mess(p)
			is_mess = mess.is_mes()
			return render_to_response('AGENTIS/mess_success.html', {'is_mess': is_mess}, RequestContext(request))
		except:
			return render_to_response('AGENTIS/mess_success.html',  RequestContext(request))

def about(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/about.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/about.html',  RequestContext(request))

def connection(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/connection.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/connection.html',  RequestContext(request))
	
def how_work(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/how_work.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/how_work.html',  RequestContext(request))

def how_rieltors(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/how_work.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/how_work.html',  RequestContext(request))
	
def how_insurance(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/how_work.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/how_work.html',  RequestContext(request))
	
def registration_complete(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/registration_complete.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/registration_complete.html',  RequestContext(request))

def enter_success(request):
	try:
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		mess = display_mess(p)
		is_mess = mess.is_mes()
		return render_to_response('AGENTIS/enter_success.html', {'is_mess': is_mess}, RequestContext(request))
	except:
		return render_to_response('AGENTIS/enter_success.html',  RequestContext(request))

def enter_result(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		if not POST.get('login', ''):
			errors.append('Вы не ввели логин!')  
		if not POST.get('password', ''):
			errors.append('Вы не ввели пароль!')
		if not errors:
			if(User.objects.filter(username=POST['login']).exists()):
				user = auth.authenticate(username=POST['login'], password=POST['password'])
				if user is not None and user.is_active:	
					auth.login(request, user)
					request.session['member_id'] = User.objects.get(username=POST['login']).username
					return HttpResponseRedirect('/enter_success/')			
				else:
					errors.append('Логин и пароль не совпадают')				
			else:
				errors.append('Введеный вами логин не существует')		
		return render_to_response('AGENTIS/enter.html',{'errors': errors[0]}, RequestContext(request))	
	
def registration_result(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		if not request.POST.get('login', ''):
			errors.append('Введите ваш логин')
		if not request.POST.get('surname', ''):
			errors.append('Введите вашу фамилию')
		if not request.POST.get('forename', ''):
			errors.append('Введите ваше имя')
		if not request.POST.get('patronyname', ''):
			errors.append('Введите ваше отчество')
		if not request.POST.get('email', ''):
			errors.append('Введите ваше e-mail')
		if request.POST['region'] == 's1':
			errors.append('Введите ваш регион')
		if not request.POST.get('number', ''):
			errors.append('Введите ваш телефон')
		if not request.POST.get('password', ''):
			errors.append('Введите ваш пароль')
		if not request.POST.get('password_repiate', ''):
			errors.append('Повторно введите пароль')
		if request.POST.get('password_repiate') and request.POST.get('password') and request.POST.get('password') != request.POST.get('password_repiate'):
			errors.append('Пароли не совпадают')
		if request.POST.get('number') and not request.POST['number'].isdigit():
			errors.append('Некорректно введен телефонный номер')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Ваш e-mail не корректен.')
		tmp_str ="tmp/"+ str(request.FILES['img'])
		print(tmp_str)
		with open(tmp_str, 'wb+') as f:
			for chunk in request.FILES['img'].chunks():
				f.write(chunk)
    		#f.write(request.FILES['img'].read())
		reopen = open(tmp_str, "rb")
		django_file = File(reopen)
		newim = image()
		newim.name_mess = str(request.FILES['img'])
		newim.img.save(str(request.FILES['img']), django_file, save=True)	
		if not errors:
			p = User_AGENTIS(who = int(request.POST['who']),
				login = request.POST['login'],
				surname = request.POST['surname'],
				forename = request.POST['forename'],
				partronyname = request.POST['patronyname'],
				region = int(request.POST['region']),
				email = request.POST['email'],
				number = int(request.POST['number']),
				message = request.POST['message'],
				img = newim
				)
			#p.img.save(str(request.FILES['img']), django_file, save=True)
			p.save()
			user = User.objects.create_user(username=request.POST['login'], email=request.POST['email'], password=request.POST['password'])
			user.save()
			return HttpResponseRedirect('/registration_complete/')
	return render_to_response('AGENTIS/registration.html',{'errors': errors[0]}, RequestContext(request))

def order_result(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		if not request.POST.get('name', ''):
			errors.append('Введите название вашего предложения')
			print('name')
		if not request.POST.get('sum', ''):
			errors.append('Введите сумму вашего предложения')
			print('sum')
		if not errors:
			u = User_AGENTIS.objects.get(login = request.session['member_id'])
			tmp_str ="tmp/"+ str(request.FILES['img'])
			print(tmp_str)
			with open(tmp_str, 'wb+') as f:
				for chunk in request.FILES['img'].chunks():
					f.write(chunk)
			reopen = open(tmp_str, "rb")
			django_file = File(reopen)
			newim = image()
			newim.name_mess = str(request.FILES['img'])
			newim.img.save(str(request.FILES['img']), django_file, save=True)
			p = orders_data(user_m = u,
				name_mess = request.POST['name'],
				sum_mess = request.POST['sum'],
				message = request.POST['description'],
				img = newim
			)
			p.save()
		#	user = User.objects.create_user(username=request.POST['login'], email=request.POST['email'], password=request.POST['password'])
		#	user.save()
			return HttpResponseRedirect('/list_rieltors/')
	return render_to_response('AGENTIS/list_again.html',{'errors': errors[0]}, RequestContext(request))
