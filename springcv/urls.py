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
    url(r'^resumen', empleados_views.profile, name = 'resumen'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(extra_patterns1)),
    url(r'^', include(extra_patterns2)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
