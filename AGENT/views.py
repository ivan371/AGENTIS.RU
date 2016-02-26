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
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import User_AGENTIS
from .models import orders_data
from .models import message
from .models import order

def index(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/index.html',{'p': p}, RequestContext(request))
	
def enter(request):
	return render(request, 'AGENTIS/enter.html')

def orders(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/orders.html',{'p': p}, RequestContext(request))

def messagers(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	m = message.objects.filter(mess_from = p)
	m1 = message.objects.filter(mess_to = p)
	print(p.login)
	return render_to_response('AGENTIS/messager.html',{'p': p, 'm': m, 'm1': m}, RequestContext(request))

def exit(request):
	auth.logout(request)
	return render(request, 'AGENTIS/index.html')
	
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
		offs = orders_data.objects.filter(user_m = p)
		return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs}, RequestContext(request))
	
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
		return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs}, RequestContext(request))

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
		return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs}, RequestContext(request))

def ch_email(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		if POST.get('email') and '@' not in POST['email']:
			errors.append('Ваш новый e-mail не корректен.')
			return render_to_response('AGENTIS/self_room.html', {'errors': errors[0], 'p': p}, RequestContext(request))
		p.email	= POST['email']
		p.save()
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def ch_number(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		if POST.get('email') and not request.POST['number'].isdigit():
			errors.append('Ваш новый номер не корректен.')
			return render_to_response('AGENTIS/self_room.html',{'errors': errors[0], 'p': p}, RequestContext(request))
		p.number = POST['number']
		p.save()
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def ch_prof(request):
	c = {}
	c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		p.who	= POST['who']
		p.save()
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

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
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def self_room(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def registration(request):
	return render(request, 'AGENTIS/registration.html')

def list_rieltors(request):
	offers_list = {'name_mess', 'sum_mess'}
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	offs = orders_data.objects.filter(user_m = p)
	return render_to_response('AGENTIS/list_rieltors.html',{'offs': offs}, RequestContext(request))
	
def list_rieltors_order(request):
	offs = orders_data.objects.all()
	return render_to_response('AGENTIS/list_rieltors_order.html',{'offs': offs}, RequestContext(request))

def mess_success(request):
	return render_to_response('AGENTIS/mess_success.html', RequestContext(request))

def make_offer(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		p = User_AGENTIS.objects.get(login = request.session['member_id'])
		return render_to_response('AGENTIS/make_offer.html', {'p': p, 'name': POST['name']},  RequestContext(request))

def send_mess(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		print(POST['name'])
		print(request.session['member_id'])
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
					message = POST['message']
					) 
		m.save()
		return render(request, 'AGENTIS/mess_success.html')

def about(request):
	return render(request, 'AGENTIS/about.html')
	
def connection(request):
	return render(request, 'AGENTIS/connection.html')
	
def how_work(request):
	return render(request, 'AGENTIS/how_work.html')	

def how_rieltors(request):
	return render(request, 'AGENTIS/how_work.html')	
	
def how_insurance(request):
	return render(request, 'AGENTIS/how_work.html')	
	
	
def registration_complete(request):
	return render(request, 'AGENTIS/registration_complete.html')	
	
def enter_success(request):
	return render(request, 'AGENTIS/enter_success.html')		

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
		if not errors:
			p = User_AGENTIS(who = int(request.POST['who']),
				login = request.POST['login'],
				surname = request.POST['surname'],
				forename = request.POST['forename'],
				partronyname = request.POST['patronyname'],
				region = int(request.POST['region']),
				email = request.POST['email'],
				number = int(request.POST['number']),
				message = request.POST['message'])
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
			p = orders_data(user_m = u,
				name_mess = request.POST['name'],
				sum_mess = request.POST['sum'],
				message = request.POST['description'])
			p.save()
		#	user = User.objects.create_user(username=request.POST['login'], email=request.POST['email'], password=request.POST['password'])
		#	user.save()
			return HttpResponseRedirect('/list_rieltors/')
	return render_to_response('AGENTIS/list_again.html',{'errors': errors[0]}, RequestContext(request))
