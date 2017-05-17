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

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:	
	# Ciclo principal infinito
	while True:
		# Obtiene la humedad y la temperatura desde el sensor 
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
		
		# Imprime en la consola las variables temperatura y humedad con un decimal
		print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))

		# Duerme 10 segundos
		time.sleep(10)

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
	# Imprime en pantalla el error e
	print str(e)
