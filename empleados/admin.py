from django.contrib import admin
from .models import *

admin.site.register(Empleado)
admin.site.register(Country)
admin.site.register(TipoDocumentoIdentidad)
admin.site.register(visas)