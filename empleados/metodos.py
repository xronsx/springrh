# -*- coding: utf-8 -*-
from empleados.views import *
from empleados.models import *
from empleados.forms import *
from django.contrib.auth.models import User

def set_values (usuario):
	form = Formulario1()
	try:
		empleado = Empleado.objects.get(user = usuario.pk)
		form.fields['apellido_paterno'].initial = empleado.apellido_paterno
		form.fields['apellido_materno'].initial = empleado.apellido_materno
		form.fields['fecha_nacimiento'].initial = empleado.fecha_nacimiento
		form.fields['pais_nacimiento'].initial = empleado.pais_nacimiento
		form.fields['edad'].initial = empleado.edad
		form.fields['tipo_documento_identidad'].initial = empleado.tipo_documento_identidad
		form.fields['fecha_vencimiento_pasaporte'].initial = empleado.pasaporte_valido
		form.fields['pasaporte'].initial = empleado.pasaporte
		form.fields['tlf'].initial = empleado.tlf
		form.fields['direccion'].initial = empleado.direccion
		form.fields['foto'].initial = empleado.foto
		form.fields['docu_ident_front'].initial = empleado.docu_ident_front
		form.fields['docu_ident_back'].initial = empleado.docu_ident_back
		form.fields['imagen_pasaporte'].initial = empleado.imagen_pasaporte
		form.fields['acta_nacimiento'].initial = empleado.acta_nacimiento
		nacionalidades = Nacionalidad.objects.filter(user=empleado)
		form.fields['nacionalidad'].initial = nacionalidades
	except:
		pass
	return form