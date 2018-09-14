#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
	pais = models.CharField(max_length=600, unique=True)

	def __str__(self):
		return str(self.pais)

class TipoDocumentoIdentidad(models.Model):
	tipo_documento = models.CharField(max_length=600, unique=True)

	def __str__(self):
		return str(self.tipo_documento)

class Empleado(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	apellido_paterno = models.CharField(max_length=600)
	apellido_materno = models.CharField(max_length=600)
	pais_nacimiento = models.ForeignKey(Country, related_name="pais_nacimiento_de")
	fecha_nacimiento = models.DateTimeField('fecha de nacimiento', auto_now_add = False)
	direccion = models.CharField(max_length=600)
	tlf = models.CharField(max_length=255)
	edad = models.IntegerField(blank = False)
	foto = models.ImageField(upload_to = 'profiles/')
	acta_nacimiento = models.ImageField(upload_to = 'actas_nacimiento/')
	tipo_documento_identidad = models.ForeignKey(TipoDocumentoIdentidad, related_name="pais_nacimiento_de")
	docu_ident_front = models.ImageField(upload_to = 'documentos_identidad/')
	docu_ident_back = models.ImageField(upload_to = 'documentos_identidad/', blank = True)
	pasaporte = models.IntegerField(blank = False)
	pasaporte_valido = models.DateTimeField('fecha de vencimiento', auto_now_add = False)
	imagen_pasaporte = models.ImageField(upload_to = 'pasaportes/')
	status = models.IntegerField(blank = False, default=1)
	# ETAPA 2
	curp = models.CharField(max_length=600, blank = True, null = True)
	imagen_curp = models.ImageField(upload_to = 'curps/', blank = True, null = True)
	rfc = models.CharField(max_length=600, blank = True, null = True)
	imagen_rfc = models.ImageField(upload_to = 'rfcs/', blank = True, null = True)
	sat = models.CharField(max_length=600, blank = True, null = True)
	imagen_sat = models.ImageField(upload_to = 'sats/', blank = True)
	infonavit = models.CharField(max_length=600, blank = True, null = True)
	imagen_infonavit = models.ImageField(upload_to = 'infonavits/', blank = True, null = True)
	imss = models.IntegerField(blank = True, null = True)
	imagen_imss = models.ImageField(upload_to = 'imss/', blank = True, null = True)
	# ETAPA 3
	estado_civil = models.CharField(max_length=600, blank = True, null = True)

	def __str__(self):
		return str ((self.user.first_name)+" "+(self.user.last_name))

class Nacionalidad(models.Model):
	user = models.ForeignKey(Empleado, related_name="user_de")
	pais = models.ForeignKey(Country, related_name="nacionalidad_de")

	def __str__(self):
		return str ((self.user.user.first_name)+" "+(self.user.user.last_name)+" "+(self.pais.pais))

class visas(models.Model):
	user = models.ForeignKey(Empleado, related_name="user_de_visas")
	pais = models.ForeignKey(Country, related_name="nacionalidad_de_visas")
	fecha_vigencia = models.DateTimeField('fecha de termino de vigencia', auto_now_add = False)
	imagen_visa = models.ImageField(upload_to = 'visas/')

	def __str__(self):
		return str ((self.user.user.first_name)+" "+(self.user.user.last_name)+" "+(self.pais.pais))

class LicenciasConducir(models.Model):
	user = models.ForeignKey(Empleado, related_name="user_de_licencia")
	fecha_vigencia = models.DateTimeField('fecha de termino de vigencia', auto_now_add = False)
	imagen_licencia = models.ImageField(upload_to = 'licencias_conducir/')
	permanente = models.BooleanField(default=False)
	estado_emision = models.CharField(max_length=600)
	licencia = models.CharField(max_length=600, unique=True)

	def __str__(self):
		return str ((self.user.user.first_name)+" "+(self.user.user.last_name))

class Conyugue(models.Model):
	user = models.ForeignKey(Empleado, related_name="user_de_conyugue")
	acta = models.ImageField('Acta de Matrimonio / Unión Libre',upload_to = 'acta_matrimonio/')
	nombre = models.CharField('Nombre del conyugue', max_length=600)
	apellido_paterno = models.CharField('Apellido paterno del conyugue', max_length=600)
	apellido_materno = models.CharField('Apellido materno del conyugue', max_length=600)
	fecha_nacimiento = models.DateTimeField('Fecha de nacimiento del conyugue', auto_now_add = False)
	profesion = models.CharField(max_length=600)
	tlf = models.CharField(max_length=255)
	email = models.CharField(max_length=600)
	email_trabajo = models.CharField(max_length=600, blank = True, null = True)
	lugar_de_trabajo = models.CharField(max_length=600, blank = True, null = True)

	def __str__(self):
		return str ((self.nombre)+" "+(self.apellido_paterno)+" "+(self.apellido_materno))
