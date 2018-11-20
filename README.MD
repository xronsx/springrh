SPRINGRRHH - CONTROL DE DOCUMENTACIÓN DE PERSONAL 
=================================================

Python 3+

Desarrollado en Ubuntu linux 16.04 LTS (Testeado en Debian y CentOs)

Instrucciones
-------------
+ Compilar OpenAlrp en el entorno siguiendo los pasos que se describen en https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux)
	- 1. $ sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
	- 2. Testear la librería:
		- 2.1. wget http://plates.openalpr.com/ea7the.jpg
		- 2.2. alpr -c us ea7the.jpg
		- 2.3. wget http://plates.openalpr.com/h786poj.jpg
		- 2.4. alpr -c eu h786poj.jpg
+ Instalar Binding para Python
	- 1. Descarga o clonar el repositorio https://github.com/openalpr/openalpr
	- 2. Dirigirse a /openalpr/src/bindings/python/
	- 3. Instalar Binding con python setup.py install
+ pip install -r requirements.txt
+ python manage.py migrate
+ python manage.py makemigrations inicio
+ python manage.py migrate
+ python manage.py createsuperuser
+ python manage.py runserver
+ En el navegador (ruta / ip)/login

NOTAS
-----

1.- En el el settings.py modificar las lineas 135 y 136 según las rutas absolutas del equipo o servidor donde se esté ejecutando la aplicación.

2.- La aplicación usa por defecto el motor de base de datos que trae integrado Django (sqlite). Se recomienda hacer el deployment final usando un gestor de base de datos más robusto. En el settings.py se incluyeron las lineas necesarias para implementar con postgresql.