#!/usr/bin/python3

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11 y registra los valores
#				 en una base de datos MySQL
# Lenguaje     : Python version 3
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria Circuit Python de Adafruit https://github.com/adafruit/Adafruit_CircuitPython_DHT
# Web          : https://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/

# Importa las librerias necesarias
import time
import datetime
import adafruit_dht
import MySQLdb

# Importa la configuracion
from config import *

# Configuracion del puerto GPIO al cual esta conectado (GPIO 23)
pin = 23

# Crea el objeto para acceder al sensor
# se debe descomentar la linea dependiendo del tipo de sensor (DHT11 o DHT22)
#sensor = adafruit_dht.DHT11(pin)
sensor = adafruit_dht.DHT22(pin)

# Inserta in registro en la base de datos MySQL
def write_mysql(temperatura, humedad):
	db = MySQLdb.connect(host=MYSQL_SERVIDOR,
							user=MYSQL_USUARIO,
							passwd=MYSQL_CONTRASENA,
							db=MYSQL_BD)

	# Crea un cursor usando la conexion
	cursor = db.cursor()

	# Genera la consulta SQL para  insertar el registro
	sql = "INSERT INTO datos (fecha, temperatura, humedad) values (now(),'" + str(temperatura) + "','" + str(humedad) + "');"

	try:
		# Ejecuta el sql
		cursor.execute(sql)
		db.commit()
	except:
		conn.rollback()

	# Cierra cursor y conexion a base de datos
	cursor.close
	db.close

# Escribe un archivo log en log_path con el nombre en el formato yyyy-mm-dd_dht.log
def write_log(text):
	log = open(log_path + datetime.datetime.now().strftime("%Y-%m-%d") + "_dht.log","a")
	line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + text + "\n"
	log.write(line)
	log.close()

# Funcion principal
def main():
	# Ciclo principal infinito
	while True:

		# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
		try:
			# Obtiene la humedad y la temperatura desde el sensor
			humedad = sensor.humidity
			temperatura = sensor.temperature

			# Si obtiene una lectura del sensor la registra en el archivo log
			if humedad is not None and temperatura is not None:
				write_log("DHT Sensor - Temperatura: %s" % str(temperatura))
				write_log("DHT Sensor - Humedad:  %s" % str(humedad))
				write_mysql(temperatura,humedad)
			else:
				write_log('Error al obtener la lectura del sensor')

		# Se ejecuta en caso de que falle alguna instruccion dentro del try
		except RuntimeError as error:
			# Imprime en pantalla el error
			print(error.args[0])

		# Duerme 10 segundos
		time.sleep(10)

# Llama a la funcion principal
if __name__ == "__main__":
    main()
