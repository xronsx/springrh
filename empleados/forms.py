#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
from empleados.opciones import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import *
from django.conf import settings
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.core.files import File
from django.utils.safestring import mark_safe
from django.forms import extras
from django.contrib.admin import widgets
from django.forms import formset_factory
import datetime
from .opciones import *

years_to_display = range(datetime.datetime.now().year - 100, datetime.datetime.now().year + 1)

class Formulario1(forms.Form):
	apellido_paterno = forms.CharField(label = 'apellido_paterno', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	apellido_materno = forms.CharField(label = 'apellido_materno', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	fecha_nacimiento = forms.DateField(label = 'fecha_nacimiento', input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	pais_nacimiento = forms.ModelChoiceField(label = 'pais_nacimiento', required = True, queryset=Country.objects.all().order_by('pais'), initial=1,  widget = forms.Select(attrs={'class': 'form-control'}))
	nacionalidad = forms.ModelMultipleChoiceField(label = 'nacionalidad', required = True, queryset=Country.objects.all().order_by('pais'), widget = forms.SelectMultiple(attrs={'class': 'chosen-select', 'data-placeholder':'Seleccione los paises de los cuales posee nacionalidad', 'multiple style':'width:350px'}))
	edad = forms.IntegerField(label = 'edad', required = True, widget = forms.TextInput(attrs={'class': 'touchspin1', 'name':'demo1'}))
	foto = forms.FileField(label='foto', required = True)
	acta_nacimiento = forms.FileField(label='acta_nacimiento', required = True)
	direccion = forms.CharField(label = 'dirección', widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
	tlf = forms.CharField(label = 'tlf', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'data-mask': '(99) 9999-9999)'}))
	tipo_documento_identidad = forms.ModelChoiceField(label = 'tipo_documento_identidad', queryset=TipoDocumentoIdentidad.objects.all(), required=True, initial=1, widget = forms.Select(attrs={'class': 'form-control'}))
	docu_ident_front = forms.FileField(label='documento_identidad_front', required = True)
	docu_ident_back = forms.FileField(label='documento_identidad_back', required = True)
	pasaporte = forms.IntegerField(label = 'pasaporte', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	fecha_vencimiento_pasaporte = forms.DateField(label = 'fecha_vencimiento_pasaporte', input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
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

class Formulario_etapa_2(forms.Form):
	visa_1 = forms.ModelChoiceField(label = 'visa_1', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
	visa_2 = forms.ModelChoiceField(label = 'visa_2', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
	visa_3 = forms.ModelChoiceField(label = 'visa_3', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
	visa_4 = forms.ModelChoiceField(label = 'visa_4', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
	visa_5 = forms.ModelChoiceField(label = 'visa_5', required = False, queryset=Country.objects.all().order_by('pais'),  widget = forms.Select(attrs={'class': 'form-control'}))
	vigencia_visa_1 = forms.DateField(label = 'vigencia_visa_1', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	vigencia_visa_2 = forms.DateField(label = 'vigencia_visa_2', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	vigencia_visa_3 = forms.DateField(label = 'vigencia_visa_3', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	vigencia_visa_4 = forms.DateField(label = 'vigencia_visa_4', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	vigencia_visa_5 = forms.DateField(label = 'vigencia_visa_5', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	img_visa_1 = forms.FileField(label='img_visa_1', required = False)
	img_visa_2 = forms.FileField(label='img_visa_2', required = False)
	img_visa_3 = forms.FileField(label='img_visa_3', required = False)
	img_visa_4 = forms.FileField(label='img_visa_4', required = False)
	img_visa_5 = forms.FileField(label='img_visa_5', required = False)
	curp = forms.CharField(label = 'curp', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	imagen_curp = forms.FileField(label='imagen_curp', required = True)
	rfc = forms.CharField(label = 'rfc', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	imagen_rfc = forms.FileField(label='imagen_rfc', required = True)
	sat = forms.CharField(label = 'sat', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	imagen_sat = forms.FileField(label='imagen_sat', required = True)
	infonavit = forms.CharField(label = 'infonavit', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	imagen_infonavit = forms.FileField(label='imagen_infonavit', required = True)
	imss = forms.IntegerField(label = 'imss', required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))
	imagen_imss = forms.FileField(label='imagen_imss', required = True)
	licencia_conducir = forms.CharField(label = 'licencia_conducir', required = False, widget = forms.TextInput(attrs={'class': 'form-control'}))
	vigencia_licencia_conducir = forms.DateField(label = 'vigencia_licencia_conducir', required = False, input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}))
	estado_emision_licencia = forms.ChoiceField(label = 'estado_emision_licencia', required = False, initial=1, choices = STATUS_CHOICES,  widget = forms.Select(attrs={'class': 'form-control'}))
	permanente = forms.BooleanField(label = 'permanente',required=False, initial = False, widget = forms.RadioSelect(choices=[(True, 'Si'),(False, 'No')],attrs={'class': 'radio-info'}))
	img_licencia = forms.FileField(label='img_licencia', required = False)
	def __init__(self, *args, **kwargs):
		super(Formulario_etapa_2, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}

class FormConyugue(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormConyugue, self).__init__(*args, **kwargs)
		# change a widget attribute:
		self.fields['acta'].widget.attrs["class"] = 'form-control'
		self.fields['nombre'].widget.attrs["class"] = 'form-control'
		self.fields['apellido_paterno'].widget.attrs["class"] = 'form-control'
		self.fields['apellido_materno'].widget.attrs["class"] = 'form-control'
		self.fields['fecha_nacimiento'].widget.attrs["class"] = 'form-control'
		self.fields['fecha_nacimiento'].widget.initial = timezone.now()
		self.fields['profesion'].widget.attrs["class"] = 'form-control'
		self.fields['tlf'].widget.attrs["class"] = 'form-control'
		self.fields['tlf'].widget.attrs["data-mask"] = '(99) 9999-9999)'
		self.fields['email'].widget.attrs["class"] = 'form-control'
		self.fields['lugar_de_trabajo'].widget.attrs["class"] = 'form-control'
		self.fields['email_trabajo'].widget.attrs["class"] = 'form-control'
		# REQUIRED
		self.fields['acta'].required = False
		self.fields['nombre'].required = False
		self.fields['apellido_paterno'].required = False
		self.fields['apellido_materno'].required = False
		self.fields['fecha_nacimiento'].required = False
		self.fields['profesion'].required = False
		self.fields['tlf'].required = False
		self.fields['email'].required = False
	class Meta:
		model = Conyugue
		fields = ('acta', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'profesion', 'lugar_de_trabajo', 'tlf', 'email', 'email_trabajo',)
		widgets = {
            'lugar_de_trabajo': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'fecha_nacimiento': forms.SelectDateWidget(years=years_to_display),
        }

class EstadoCivil(forms.Form):
	estado_civil = forms.ChoiceField(label = 'estado_civil', required = True, choices=ESTADO_CIVIL, initial=Soltero, widget = forms.RadioSelect(attrs={'onclick':'javascript:yesnoCheck();'}))

	def __init__(self, *args, **kwargs):
		super(EstadoCivil, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}

class PreguntasEtapa3(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PreguntasEtapa3, self).__init__(*args, **kwargs)

		self.fields['fecha_llegada'].widget.attrs["class"] = 'form-control'

	class Meta:
		model = Preguntas
		fields = ('fecha_llegada', 'permiso_trabajo', 'solicitud_permiso_trabajo',)
		widgets = {
			'fecha_llegada' : forms.SelectDateWidget(years=years_to_display),
			'permiso_trabajo' : forms.CheckboxInput(attrs={'onclick':'javascript:yesnoCheck();'}),
			'solicitud_permiso_trabajo' : forms.CheckboxInput(attrs={'style':'display:none;'}),
		}

class ExtranjeroSiNo(forms.Form):
	SiNo = forms.ChoiceField(label = 'SiNo', required = True, choices=EXTRANJERO, initial=No, widget = forms.RadioSelect(attrs={'onclick':'javascript:yesnoCheck();'}))
	def __init__(self, *args, **kwargs):
		super(ExtranjeroSiNo, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}

class numero_hijos(forms.Form):
	cantidad = forms.IntegerField(label = 'Cantidad de hijos', initial=0, required = True, widget = forms.TextInput(attrs={'class': 'touchspin1', 'name':'demo1'}))
	def __init__(self, *args, **kwargs):
		super(numero_hijos, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}

class FormHijos(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormHijos, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs["class"] = 'form-control'
		self.fields['apellido_paterno'].widget.attrs["class"] = 'form-control'
		self.fields['apellido_materno'].widget.attrs["class"] = 'form-control'
		self.fields['fecha_nacimiento'].widget.attrs["class"] = 'form-control'
		# REQUIRED
		self.fields['nombre'].widget.attrs["required"] = 'true'
		self.fields['apellido_paterno'].widget.attrs["required"] = 'true'
		self.fields['apellido_materno'].widget.attrs["required"] = 'true'
		self.fields['fecha_nacimiento'].widget.attrs["required"] = 'true'
		self.fields['edad'].widget.attrs["required"] = 'true'

	class Meta:
		model = Hijo
		fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'edad',)
		widgets = {
			'fecha_nacimiento' : forms.SelectDateWidget(years=years_to_display),
			'edad' : forms.TextInput(attrs={'class': 'touchspin1', 'name':'demo1'}),
		}

class EstudiosForm(forms.ModelForm):
    class Meta:
        model = Estudio
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(EstudiosForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(CapacitacionForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})

class IdiomasForm(forms.ModelForm):
    class Meta:
        model = Idioma
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(IdiomasForm, self).__init__(*args, **kwargs)
        for campos in self.fields:
            self.fields[campos].widget.attrs.update({'class': 'form-control'})