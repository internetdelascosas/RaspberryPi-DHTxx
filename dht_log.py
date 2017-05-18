#!/usr/bin/python

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11 
# Lenguaje     : Python
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria de Adafruit https://github.com/adafruit/Adafruit_Python_DHT
# Web          : http://internetdelascosas.cl/

# Importa las librerias necesarias 
import time
import datetime
import Adafruit_DHT

# Log file
log_path = "/var/log/iot/"

# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.DHT11

# Configuracion del puerto GPIO al cual esta conectado (GPIO 23)
pin = 23

# Escribe un archivo log en log_path con el nombre en el formato yyyy-mm-dd_dht.log
def write_log(text):
	log = open(log_path + datetime.datetime.now().strftime("%Y-%m-%d") + "_dht.log","a")
	line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + text + "\n"
	log.write(line)
	log.close()

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:
	# Ciclo principal infinito
	while True:
		# Obtiene la humedad y la temperatura desde el sensor 
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

		# Si obtiene una lectura del sensor la registra en el archivo log
		if humedad is not None and temperatura is not None:
			write_log("DHT Sensor - Temperatura: %s" % str(temperatura))
			write_log("DHT Sensor - Humedad:  %s" % str(humedad))
		else:
			write_log('Error al obtener la lectura del sensor')

		# Duerme 10 segundos
		time.sleep(10)

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
	# Registra el error en el archivo log y termina la ejecucion
	write_log(str(e))
