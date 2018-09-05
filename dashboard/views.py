# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from empleados.models import Empleado
from .models import *
from .forms import *
from datetime import datetime, timedelta
from django.db import IntegrityError

# Create your views here.

def login_view(request):
	state = ""
	username = ""
	password = ""
	next = ""

	if request.GET:
	    next = request.GET['next']

	if request.POST:
	    username = request.POST['username']
	    password = request.POST['password']

	    if '@' in username:
	        try:
	            check = User.objects.get(email=username)
	            username = check.username
	        except:
	            pass

	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            if next == "":
	                return HttpResponseRedirect('/home/')
	            else:
	                return HttpResponseRedirect(next)
	        else:
	            state = 0
	    else:
	        state = 0
	return render(request, 'dashboard/login.html', {'state':state, 'username': username, 'next': next,},)

@login_required(login_url = '/login/')
def login_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url = '/login/')
def home(request, template_name = "dashboard/dashboard.html"):
	# Verificamos si el usuario tiene foto, Si existe algún registro en
	# Tabla Empleados que referencie al usuario en turno y si este posee
	# foto cargada al sistema
	usuario = request.user
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		foto = 1
		etapa = empleado.status
	except:
		foto = 0
		etapa = 1
		pass
	return render(request, template_name, locals(),)

def register(request, template_name = "dashboard/register.html"):
	if request.method == 'POST':
		form = ActivaEmpleado(request.POST)
		if form.is_valid():
			correo = request.POST['email']
			usuario = request.POST['username']
			contrasena = form.cleaned_data['password']
			# Consultar si existe correo
			usuario_inactivo = User.objects.get(email = correo)
			if usuario_inactivo:
				# Verificar su status (ACTIVADO O NO ACTIVADO)
				if usuario_inactivo.is_active:
					mensaje = 0
				else:
					# Actualizar USERNAME
					usuario_inactivo.username = usuario
					usuario_inactivo.save()
					# Actualizar PASSWORD
					usuario_inactivo.set_password(contrasena)
					usuario_inactivo.save()
					# Cambiar status
					usuario_inactivo.is_active = True
					usuario_inactivo.save()
					mensaje = 1
		else:
			print(form.errors)
	else:
		form = ActivaEmpleado()
	return render(request, template_name, locals(),)