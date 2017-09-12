# RaspberryPi-DHT11
Programas ejemplo de como conectar el sensor de temperatura y humedad DHT11 a una Raspberry Pi.

## Software Necesario
- Librerias de desarrollo Python y cliente MySQL

  sudo apt-get install python-pip python-dev libmysqlclient-dev

- Libreria Python MySQLdb

  sudo pip install MySQL-python

- Libreria de Adafruit Python DHT, disponible en https://github.com/adafruit/Adafruit_Python_DHT

## Diagrama de conexión
![](http://www.internetdelascosas.cl/wp-content/uploads/2017/05/Raspberry-Pi-DHT11_bb-768x374.png)


## Tutorial e Instalación
Pueden leer el tutorial completo para realizar este proyecto en

http://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/

## Base de datos
El programa dht_mysql.py escribe los registros en una base de datos MySQL, para crear la tabla datos se debe usar el script SQL ubicado en la carpeta sql

## Consultas y sugerencias
Escribir a contacto@iot.cl
