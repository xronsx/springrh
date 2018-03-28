#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import *
from django.conf import settings
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.core.files import File
from django.utils.safestring import mark_safe

class Formulario1(forms.Form):
	apellido_paterno = forms.CharField(label = "apellido_paterno", required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	apellido_materno = forms.CharField(label = "apellido_materno", required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	fecha_nacimiento = forms.DateField(label = "fecha_nacimiento", input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	pais_nacimiento = forms.ModelChoiceField(label = "pais_nacimiento", required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
	nacionalidad = forms.ModelMultipleChoiceField(label = "nacionalidad", required = True, queryset=Country.objects.all().order_by('pais'), widget = forms.SelectMultiple(attrs={'class': 'chosen-select', 'data-placeholder':'Seleccione los paises de los cuales posee nacionalidad', 'multiple style':'width:350px'}))
	edad = forms.IntegerField(label = "edad", required = True, widget = forms.TextInput(attrs={'class': 'touchspin1', 'name':'demo1'}))
	foto = forms.FileField(label='foto', required = True)
	acta_nacimiento = forms.FileField(label='acta_nacimiento', required = True)
	direccion = forms.CharField(label = "dirección", widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
	tlf = forms.CharField(label = "tlf", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'data-mask': '(99) 9999-9999)'}))
	tipo_documento_identidad = forms.ModelChoiceField(label = "tipo_documento_identidad", queryset=TipoDocumentoIdentidad.objects.all(), required=True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
	docu_ident_front = forms.FileField(label='documento_identidad_front', required = True)
	docu_ident_back = forms.FileField(label='documento_identidad_back', required = False)
	pasaporte = forms.IntegerField(label = "pasaporte", required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	fecha_vencimiento_pasaporte = forms.DateField(label = "fecha_vencimiento_pasaporte", input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	imagen_pasaporte = forms.FileField(label='imagen_pasaporte', required = True)

	def __init__(self, *args, **kwargs):
		super(Formulario1, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}