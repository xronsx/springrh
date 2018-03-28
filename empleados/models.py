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

	def __str__(self):
		return str ((self.user.first_name)+" "+(self.user.last_name))

class Nacionalidad(models.Model):
	user = models.ForeignKey(Empleado, related_name="user_de")
	pais = models.ForeignKey(Country, related_name="nacionalidad_de")

	def __str__(self):
		return str ((self.user.user.first_name)+" "+(self.user.user.last_name)+" "+(self.pais.pais))

# class visas(models.Model):
# 	user = models.ForeignKey(Empleado, related_name="user_de")
# 	pais = models.ForeignKey(Country, related_name="nacionalidad_de")
# 	imagen_visa = models.ImageField(upload_to = 'visas/')

# 	def __str__(self):
# 		return str ((self.user.user.first_name)+" "+(self.user.user.last_name)+" "+(self.pais.pais))