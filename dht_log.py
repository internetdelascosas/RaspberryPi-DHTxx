#!/usr/bin/python3

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHTxx y escribe los datos en un archivo log
# Lenguaje     : Python version 3
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria Circuit Python de Adafruit https://github.com/adafruit/Adafruit_CircuitPython_DHT
# Web          : https://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/

# Importa las librerias necesarias
import time
import datetime
import adafruit_dht

# Log file
log_path = "/var/log/iot/"

# Configuracion del puerto GPIO al cual esta conectado (GPIO 23)
pin = 23

# Crea el objeto para acceder al sensor
# se debe descomentar la linea dependiendo del tipo de sensor (DHT11 o DHT22)
#sensor = adafruit_dht.DHT11(pin)
sensor = adafruit_dht.DHT22(pin)

# Funcion: Escribe un archivo log en log_path con el nombre en el formato yyyy-mm-dd_dht.log
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
				write_log("DHT Sensor - Humedad: %s" % str(humedad))
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
