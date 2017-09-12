# Configuracion para sensor DHTxx
#
# Estas variables se sobre escriben en el archivo config_local.py
# que debe contener estas mismas variables exceptuando las 5 
# ultimas lineas

# Configuracion del puerto GPIO al cual esta conectado (GPIO 23)
pin = 23

# Configuracion de la carpeta para la creacion de los archivos log
log_path = "/var/log/iot/"

# Configuracion credenciales MySQL
MYSQL_SERVIDOR = "localhost"
MYSQL_BD = "raspberrypi"
MYSQL_USUARIO = "raspberrypi"
MYSQL_CONTRASENA = "contrasena_super_secreta"

# Carga la configuracion local desde el archivo config_local.py
try:
	from config_local import *
except Exception, e:
	print "ERROR: " + str(e)