# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from .forms import *
# Create your views here.

def perfil(request, template_name = "empleados/perfil.html"):
	usuario = request.user
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		foto = 1
	except:
		foto = 0
	if request.method == 'POST':
		form = Formulario1(request.POST, request.FILES)
		if form.is_valid():
			apellido_paterno = form.cleaned_data['apellido_paterno']
			apellido_materno = form.cleaned_data['apellido_materno']
			fecha_nacimiento = datetime.datetime.strptime(request.POST['fecha_nacimiento'], '%d/%m/%Y').strftime('%Y-%m-%d')
			fecha_vencimiento_pasaporte = datetime.datetime.strptime(request.POST['fecha_vencimiento_pasaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')
			pais_nacimiento = request.POST['pais_nacimiento']
			pais_nacimiento = Country.objects.get(pk=pais_nacimiento)
			edad = form.cleaned_data['edad']
			tlf = form.cleaned_data['tlf']
			direccion = form.cleaned_data['direccion']
			foto = request.FILES['foto']
			acta_nacimiento = request.FILES['acta_nacimiento']
			nacionalidad = form.cleaned_data['nacionalidad']
			tipo_documento_identidad_valor = TipoDocumentoIdentidad.objects.get(pk=request.POST['tipo_documento_identidad'])
			# Grabamos los datos nativos en tabla empleados
			nuevo_empleado = Empleado(user=usuario,
				apellido_paterno=apellido_paterno,
				apellido_materno=apellido_materno,
				fecha_nacimiento=fecha_nacimiento,
				pais_nacimiento=pais_nacimiento,
				edad=edad,
				foto=request.FILES['foto'],
				acta_nacimiento=request.FILES['acta_nacimiento'],
				docu_ident_front=request.FILES['docu_ident_front'], 
				docu_ident_back=request.FILES['docu_ident_back'],
				tipo_documento_identidad=tipo_documento_identidad_valor,
				pasaporte_valido=fecha_vencimiento_pasaporte, 
				pasaporte=request.POST['pasaporte'],
				imagen_pasaporte=request.FILES['imagen_pasaporte'], 
				tlf=tlf, 
				direccion=direccion)
			nuevo_empleado.save()
			# Grabamos las nacionalidades en la tabla nacionalidades referenciando pais y usuario
			for dato in nacionalidad:
				objeto_pais = Country.objects.get(pais=dato)
				if objeto_pais:
					empleado = Empleado.objects.get(user = usuario.pk)
					nacionalidad = Nacionalidad(user=empleado,pais=objeto_pais)
					nacionalidad.save()
			#return HttpResponseRedirect('/detalles/%s' % cic) EJEMPLO PARA REDIRECT A PÁGINA CON DATOS
			return HttpResponseRedirect('/resumen_general/')
		else:
			print (form.errors)
		form = Formulario1()
	else:
		#pass
		form = Formulario1()
		#form.fields['tipo_documento_identidad'].initial = datetime.now().strftime("%m-%d-%y")
	return render(request, template_name, locals(),)

def profile(request, template_name = "empleados/profile.html"):
	return render(request, template_name, locals(),)