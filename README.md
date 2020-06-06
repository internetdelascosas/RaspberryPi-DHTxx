# RaspberryPi-DHT11
Programas ejemplo de como conectar el sensor de temperatura y humedad DHTxx a una Raspberry Pi.

## Software Necesario
- Librerias de desarrollo Python y cliente MySQL

  sudo apt-get install python3-dev **default-libmysqlclient-dev**

- Libreria Python MySQLdb

  sudo pip3 install mysqlclient

- Libreria Circuit Python de Adafruit, disponible en https://github.com/adafruit/Adafruit_CircuitPython_DHT

  pip3 install adafruit-circuitpython-dht

## Diagrama de conexión
![](http://www.internetdelascosas.cl/wp-content/uploads/2017/05/Raspberry-Pi-DHT11_bb-768x374.png)


## Tutorial e Instalación
Pueden leer el tutorial completo para realizar este proyecto en

https://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/

## Base de datos
El programa dht_mysql.py escribe los registros en una base de datos MySQL, para crear la tabla datos se debe usar el script SQL ubicado en la carpeta sql

  cat ./sql/create_data.sql | mysql -u [usuario] -p [base_de_datos]

## Consultas y sugerencias
Escribir a contacto@iot.cl
