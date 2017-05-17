#!/usr/bin/python

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11 
# Lenguaje     : Python
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria de Adafruit https://github.com/adafruit/Adafruit_Python_DHT
# Web          : http://internetdelascosas.cl/
 
# Importa las librerias necesarias 
import sys
import time
import Adafruit_DHT

# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.DHT11

# Configuracion del puerto GPIO al cual esta conectado
pin = 23

try:	
	# Ciclo principal
	while True:
		
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

		print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))

		time.sleep(10)

except Exception,e:
	print str(e)
