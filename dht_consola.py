#!/usr/bin/python3

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11
# Lenguaje     : Python version 3
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria Circuit Python de Adafruit https://github.com/adafruit/Adafruit_CircuitPython_DHT
# Web          : https://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/

# Importa las librerias necesarias
import sys
import time
import adafruit_dht

# Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 23

# Crea el objeto para acceder al sensor
# se debe descomentar la linea dependiendo del tipo de sensor (DHT11 o DHT22)
#sensor = adafruit_dht.DHT11(pin)
sensor = adafruit_dht.DHT22(pin)

# Funcion principal
def main():
    # Ciclo principal infinito
    while True:

        # Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
        try:
    		# Obtiene la humedad y la temperatura desde el sensor
            humedad = sensor.humidity
            temperatura = sensor.temperature

    		# Imprime en la consola las variables temperatura y humedad con un decimal
            print('Temperatura={0:0.1f} C  Humedad={1:0.1f}%'.format(temperatura, humedad))

        # Se ejecuta en caso de que falle alguna instruccion dentro del try
        except RuntimeError as error:
            # Imprime en pantalla el error
            print(error.args[0])

        # Duerme 10 segundos
        time.sleep(10)

# Llama a la funcion principal
if __name__ == "__main__":
    main()
