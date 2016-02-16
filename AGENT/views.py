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

def index(request):
	return render(request, 'AGENTIS/index.html')
	
def enter(request):
	return render(request, 'AGENTIS/enter.html')

def orders(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/orders.html',{'p': p}, RequestContext(request))

def messagers(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/messager.html',{'p': p}, RequestContext(request))

def exit(request):
	auth.logout(request)
	return render(request, 'AGENTIS/index.html')
	
	
def ch_email(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def ch_number(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def ch_prof(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def ch_initial(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def self_room(request):
	p = User_AGENTIS.objects.get(login = request.session['member_id'])
	return render_to_response('AGENTIS/self_room.html',{'p': p}, RequestContext(request))

def registration(request):
	return render(request, 'AGENTIS/registration.html')

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

