#-*- coding: utf-8 -*-
#Estados
Aguascalientes='Aguascalientes'
BajaCalifornia='Baja California'
BajaCaliforniaSur='Baja California Sur'
Campeche='Campeche'
Chiapas='Chiapas'
Chihuahua='Chihuahua'
Coahuila='Coahuila'
Colima='Colima'
CiudaddeMéxico = 'Ciudad de México'
DistritoFederal='Distrito Federal'
Durango='Durango'
EstadodeMéxico='Estado de México'
Guanajuato='Guanajuato'
Guerrero='Guerrero'
Hidalgo='Hidalgo'
Jalisco='Jalisco'
Michoacán='Michoacán'
Morelos='Morelos'
Nayarit='Nayarit'
NuevoLeón='Nuevo León'
Oaxaca='Oaxaca'
Puebla='Puebla'
Querétaro='Querétaro'
QuintanaRoo='Quintana Roo'
SanLuisPotosí='San Luis Potosí'
Sinaloa='Sinaloa'
Sonora='Sonora'
Tabasco='Tabasco'
Tamaulipas='Tamaulipas'
Tlaxcala='Tlaxcala'
Veracruz='Veracruz'
Yucatán='Yucatán'
Zacatecas='Zacatecas'

#Estado Civil
Casado='Casado(a)'
Soltero='Soltero(a)'
UnionLibre='Unión Libre'
Viudo='Viudo(a)'

Si = 'Si'
No = 'No'

STATUS_CHOICES = (
	(Aguascalientes,'Aguascalientes'),
	(BajaCalifornia,'Baja California'),
	(BajaCaliforniaSur,'Baja California Sur'),
	(CiudaddeMéxico, 'Ciudad de México'),
	(Campeche,'Campeche'),
	(Chiapas,'Chiapas'),
	(Chihuahua,'Chihuahua'),
	(Coahuila,'Coahuila'),
	(Colima,'Colima'),
	(DistritoFederal,'Distrito Federal'),
	(Durango,'Durango'),
	(EstadodeMéxico,'Estado de México'),
	(Guanajuato,'Guanajuato'),
	(Guerrero,'Guerrero'),
	(Hidalgo,'Hidalgo'),
	(Jalisco,'Jalisco'),
	(Michoacán,'Michoacán'),
	(Morelos,'Morelos'),
	(Nayarit,'Nayarit'),
	(NuevoLeón,'Nuevo León'),
	(Oaxaca,'Oaxaca'),
	(Puebla,'Puebla'),
	(Querétaro,'Querétaro'),
	(QuintanaRoo,'Quintana Roo'),
	(SanLuisPotosí,'San Luis Potosí'),
	(Sinaloa,'Sinaloa'),
	(Sonora,'Sonora'),
	(Tabasco,'Tabasco'),
	(Tamaulipas,'Tamaulipas'),
	(Tlaxcala,'Tlaxcala'),
	(Veracruz,'Veracruz'),
	(Yucatán,'Yucatán'),
	(Zacatecas,'Zacatecas'),
)

ESTADO_CIVIL = (
	(Soltero,'Soltero(a)'),
	(Casado,'Casado(a)'),
	(UnionLibre,'Unión Libre'),
	(Viudo, 'Viudo(a)'),
)

years = (
		'1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
		'1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
		'1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
		'1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
		'2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
		'2012', '2013', '2014', '2015', '2016', '2017', '2018')

EXTRANJERO = (
	(No,'No'),
	(Si,'Si'),
)