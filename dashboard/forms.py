#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import *
from django.conf import settings
from django.forms import ModelChoiceField
from django.core.files import File

Colector = "Colector"
Administrador = "Administrador"
GRUPO = (
        (Colector, 'Colector'),
        (Administrador, 'Administrador'),
    )

class ActivaEmpleado(forms.Form):
	username = forms.CharField(label = "user", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User'}))
	email = forms.EmailField(label = "email", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(label = "password", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

	def __init__(self, *args, **kwargs):
		super(ActivaEmpleado, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}