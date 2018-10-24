"""springcv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dashboard import views as dashboard_views
from empleados import views as empleados_views
from django.conf.urls.static import static
from django.conf import settings

# urls de app dashboard
extra_patterns1 = [
    url(r'^login', dashboard_views.login_view, name = 'login'),
    url(r'^logout/$', dashboard_views.login_out, name = 'logout'),
    url(r'^home/$', dashboard_views.home, name = 'home'),
    url(r'^register/$', dashboard_views.register, name = 'register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls de app empleados
extra_patterns2 = [
    url(r'^perfil', empleados_views.perfil, name = 'perfil'),
    url(r'^confirma1', empleados_views.confirma_etapa_1, name = 'confirma1'),
    url(r'^rechaza1', empleados_views.rechaza_etapa_1, name = 'rechaza1'),
    # ETAPA 2
    url(r'^etapa-2', empleados_views.etapa_2, name = 'etapa-2'),
    url(r'^rechaza2', empleados_views.rechaza_etapa_2, name = 'rechaza2'),
    url(r'^confirma2', empleados_views.confirma_etapa_2, name = 'confirma2'),
    # ETAPA 3
    url(r'^etapa-3', empleados_views.etapa_3, name = 'etapa-3'),
    url(r'^rechaza3', empleados_views.rechaza_etapa_3, name = 'rechaza3'),
    url(r'^confirma3', empleados_views.confirma_etapa_3, name = 'confirma3'),
    # ETAPA 4
    url(r'^etapa-4', empleados_views.etapa_4, name = 'etapa-4'),
    url(r'^rechaza4', empleados_views.rechaza_etapa_4, name = 'rechaza4'),
    url(r'^confirma4', empleados_views.confirma_etapa_4, name = 'confirma4'),
    # ETAPA 4
    url(r'^etapa-5', empleados_views.etapa_5, name = 'etapa-5'),
    url(r'^rechaza5_9', empleados_views.rechaza_etapa_5_status_9, name = 'rechaza-status-9'),
    url(r'^confirma5_9', empleados_views.confirma_etapa_5_status_9, name = 'confirma-status-9'),
    url(r'^borrar-curso/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.borrar_curso, name = 'borrar-curso'),
    url(r'^borrar-idioma/(?P<id>[-A-Za-z0-9_]+)$', empleados_views.borrar_idioma, name = 'borrar-idioma'),
    url(r'^confirma5_10', empleados_views.confirma_etapa_5_status_10, name = 'confirma-status-10'),
    url(r'^confirma5_11', empleados_views.confirma_etapa_5_status_11, name = 'confirma-status-11'),
    url(r'^confirma5', empleados_views.confirma_etapa_5, name = 'confirma5'),
    url(r'^rechaza5', empleados_views.rechaza_etapa_5, name = 'rechaza5'),
    # ETAPA 6
    url(r'^etapa-6', empleados_views.etapa_6, name = 'etapa-6'),
    url(r'^rechaza6', empleados_views.rechaza_etapa_6, name = 'rechaza6'),
    url(r'^confirma6', empleados_views.confirma_etapa_6, name = 'confirma6'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(extra_patterns1)),
    url(r'^', include(extra_patterns2)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
