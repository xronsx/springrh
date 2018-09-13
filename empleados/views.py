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
from dashboard.views import *
from .metodos import *
# Create your views here.

# ========= INICIO ETAPA 1 ==========
@login_required(login_url = '/login/')
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
			fecha_nacimiento = datetime.strptime(request.POST['fecha_nacimiento'], '%d/%m/%Y').strftime('%Y-%m-%d')
			fecha_vencimiento_pasaporte = datetime.strptime(request.POST['fecha_vencimiento_pasaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')
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
			form = set_values(usuario)
			nacionalidades = Nacionalidad.objects.filter(user=empleado)
			#return HttpResponseRedirect('/resumen/%s' % usuario.pk) #EJEMPLO PARA REDIRECT A PÁGINA CON DATOS
			#return HttpResponseRedirect('/perfil/')
		else:
			print (form.errors)
			form.errors
			try:
				empleado = Empleado.objects.get(user = usuario.pk)
				if empleado:
					form = set_values(usuario)
					nacionalidades = Nacionalidad.objects.filter(user=empleado)
			except:
				form = Formulario1()
	else:
		try:
			empleado = Empleado.objects.get(user = usuario.pk)
			if empleado:
				form = set_values(usuario)
				nacionalidades = Nacionalidad.objects.filter(user=empleado)
		except:
			form = Formulario1()
		#form.fields['tipo_documento_identidad'].initial = datetime.now().strftime("%m-%d-%y")
	return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def confirma_etapa_1(request, template_name = "dashboard/dashboard.html"):
	usuario = request.user
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		empleado.status = 2
		empleado.save()
	except:
		pass
	return home(request)

@login_required(login_url = '/login/')
def rechaza_etapa_1(request, template_name = "empleados/perfil.html"):
	usuario = request.user
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		empleado.status = 1
		empleado.delete()
	except:
		pass
	return perfil(request)
# ========= FIN ETAPA 1 ==========


# ========= INICIO ETAPA 2 ==========
@login_required(login_url = '/login/')
def etapa_2(request, template_name = "empleados/etapa_2.html"):
	usuario = request.user
	empleado = Empleado.objects.get(user = usuario.pk)
	if request.method == 'POST':
		form = Formulario_etapa_2(request.POST, request.FILES)
		if form.is_valid():
			try:
				# VISA 1
				pais_visa_1 = request.POST['visa_1']
				if pais_visa_1:
					pais_visa_1 = Country.objects.get(pk=pais_visa_1)
					fecha_vigencia_visa_1 = datetime.strptime(request.POST['vigencia_visa_1'], '%d/%m/%Y').strftime('%Y-%m-%d')
					img_visa_1 = request.FILES['img_visa_1']
				# VISA 2
				pais_visa_2 = request.POST['visa_2']
				if pais_visa_2:
					pais_visa_2 = Country.objects.get(pk=pais_visa_2)
					fecha_vigencia_visa_2 = datetime.strptime(request.POST['vigencia_visa_2'], '%d/%m/%Y').strftime('%Y-%m-%d')
					img_visa_2 = request.FILES['img_visa_2']
				# VISA 3
				pais_visa_3 = request.POST['visa_3']
				if pais_visa_3:
					pais_visa_3 = Country.objects.get(pk=pais_visa_3)
					fecha_vigencia_visa_3 = datetime.strptime(request.POST['vigencia_visa_3'], '%d/%m/%Y').strftime('%Y-%m-%d')
					img_visa_3 = request.FILES['img_visa_3']
				# VISA 4
				pais_visa_4 = request.POST['visa_4']
				if pais_visa_4:
					pais_visa_4 = Country.objects.get(pk=pais_visa_4)
					fecha_vigencia_visa_4 = datetime.strptime(request.POST['vigencia_visa_4'], '%d/%m/%Y').strftime('%Y-%m-%d')
					img_visa_4 = request.FILES['img_visa_4']
				# VISA 5
				pais_visa_5 = request.POST['visa_5']
				if pais_visa_5:
					pais_visa_5 = Country.objects.get(pk=pais_visa_5)
					fecha_vigencia_visa_5 = datetime.strptime(request.POST['vigencia_visa_5'], '%d/%m/%Y').strftime('%Y-%m-%d')
					img_visa_5 = request.FILES['img_visa_5']
				# LICENCIA
				licencia = request.POST['licencia_conducir']
				if licencia:
					estado_emision = form.cleaned_data['estado_emision_licencia']
					fecha_vigencia_licencia = datetime.strptime(request.POST['vigencia_licencia_conducir'], '%d/%m/%Y').strftime('%Y-%m-%d')
					img_licencia = request.FILES['img_licencia']

				curp = form.cleaned_data['curp']
				imagen_curp = request.FILES['imagen_curp']
				rfc = form.cleaned_data['rfc']
				imagen_rfc = request.FILES['imagen_rfc']
				sat = form.cleaned_data['sat']
				imagen_sat = request.FILES['imagen_sat']
				infonavit = form.cleaned_data['infonavit']
				imagen_infonavit = request.FILES['imagen_infonavit']
				imss = form.cleaned_data['imss']
				imagen_imss = request.FILES['imagen_imss']

			except:
				mensaje_error = "Faltan Datos"
				print(mensaje_error)
				form.errors

			# GUARDADO DE DATOS
			try:
				if pais_visa_1:
					nueva_visa = visas(user=empleado, pais=pais_visa_1, fecha_vigencia=fecha_vigencia_visa_1, imagen_visa=img_visa_1)
					previo = visas.objects.filter(user=empleado,pais=pais_visa_1,fecha_vigencia=fecha_vigencia_visa_1)
					if not previo.exists():
						nueva_visa.save()
				if pais_visa_2:
					nueva_visa = visas(user=empleado, pais=pais_visa_2, fecha_vigencia=fecha_vigencia_visa_2, imagen_visa=img_visa_2)
					previo = visas.objects.filter(user=empleado,pais=pais_visa_2,fecha_vigencia=fecha_vigencia_visa_2)
					if not previo.exists():
						nueva_visa.save()
				if pais_visa_3:
					nueva_visa = visas(user=empleado, pais=pais_visa_3, fecha_vigencia=fecha_vigencia_visa_3, imagen_visa=img_visa_3)
					previo = visas.objects.filter(user=empleado,pais=pais_visa_3,fecha_vigencia=fecha_vigencia_visa_3)
					if not previo.exists():
						nueva_visa.save()
				if pais_visa_4:
					nueva_visa = visas(user=empleado, pais=pais_visa_4, fecha_vigencia=fecha_vigencia_visa_4, imagen_visa=img_visa_4)
					previo = visas.objects.filter(user=empleado,pais=pais_visa_4,fecha_vigencia=fecha_vigencia_visa_4)
					if not previo.exists():
						nueva_visa.save()
				if pais_visa_5:
					nueva_visa = visas(user=empleado, pais=pais_visa_5, fecha_vigencia=fecha_vigencia_visa_5, imagen_visa=img_visa_5)
					previo = visas.objects.filter(user=empleado,pais=pais_visa_5,fecha_vigencia=fecha_vigencia_visa_5)
					if not previo.exists():
						nueva_visa.save()
				if licencia:
					nueva_licencia = LicenciasConducir(user=empleado,
						permanente=request.POST['permanente'], 
						fecha_vigencia=fecha_vigencia_licencia, 
						estado_emision=estado_emision, 
						imagen_licencia=img_licencia, 
						licencia=licencia)
					nueva_licencia.save()
				empleado = Empleado.objects.get(user = usuario.pk)
				empleado.curp = curp
				empleado.imagen_curp = imagen_curp
				empleado.rfc = rfc
				empleado.imagen_rfc = imagen_rfc
				empleado.sat = sat
				empleado.imagen_sat = imagen_sat
				empleado.infonavit = infonavit
				empleado.imagen_infonavit = imagen_infonavit
				empleado.imss = imss
				empleado.imagen_imss = imagen_imss
				empleado.status = 3
				empleado.save()
				if visas.objects.filter(user=empleado).exists():
					todas_visas = visas.objects.filter(user=empleado)
				if LicenciasConducir.objects.filter(user=empleado).exists():
					licencia_data = LicenciasConducir.objects.filter(user=empleado)
				form = set_values_2(usuario)
			except:
				mensaje_error = "Error al guardar datos"
				print (mensaje_error)
				form.errors

		else:
			form.errors
			try:
				empleado = Empleado.objects.get(user = usuario.pk)
				if empleado.status == 3:
					if visas.objects.filter(user=empleado).exists():
						todas_visas = visas.objects.filter(user=empleado)
					if LicenciasConducir.objects.filter(user=empleado).exists():
						licencia_data = LicenciasConducir.objects.filter(user=empleado)
					form = set_values_2(usuario)
			except:
				form = Formulario_etapa_2()
	else:
		try:
			empleado = Empleado.objects.get(user = usuario.pk)
			if empleado.status == 3:
				if visas.objects.filter(user=empleado).exists():
					todas_visas = visas.objects.filter(user=empleado)
				if LicenciasConducir.objects.filter(user=empleado).exists():
					licencia_data = LicenciasConducir.objects.filter(user=empleado)
				form = set_values_2(usuario)
			else:
				form = Formulario_etapa_2()
		except:
			pass
	return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def rechaza_etapa_2(request, template_name = "empleados/etapa_2.html"):
	usuario = request.user
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		empleado.status = 2
		empleado.imagen_curp.delete(save=True)
		empleado.imagen_rfc.delete(save=True)
		empleado.imagen_sat.delete(save=True)
		empleado.imagen_infonavit.delete(save=True)
		empleado.imagen_imss.delete(save=True)
		if visas.objects.filter(user=empleado).exists():
			todas_visas = visas.objects.filter(user=empleado)
			todas_visas.delete()
		if LicenciasConducir.objects.filter(user=empleado).exists():
			licencia_data = LicenciasConducir.objects.filter(user=empleado)
			licencia_data.delete()
	except:
		pass
	return etapa_2(request)

@login_required(login_url = '/login/')
def confirma_etapa_2(request, template_name = "dashboard/dashboard.html"):
	usuario = request.user
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		empleado.status = 4
		empleado.save()
	except:
		pass
	return home(request)
# ========= FIN ETAPA 2 ==========

# ========= INICIO ETAPA 3 ==========
@login_required(login_url = '/login/')
def etapa_3(request, template_name = "empleados/etapa_3.html"):
	return render(request, template_name, locals(),)