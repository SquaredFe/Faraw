# Bienvenido a Faraw, este concepto de sistema operativo textual desarrollado en el lenguaje python, este archivo
# es el main, aca es donde la estructura principal de Faraw se desarrolla.
#
# Si necesitas aplicaciones como calculadora, ve a el directorio /appsx/releases/.
# este es uno de los archivos que mas se actualize cada vez que se agregue una nueva app.

import time
import urllib.request
import os
import sys
if len(sys.argv) > 1:
    orden = sys.argv[1]
    # Si la orden es "skip" el sistema saltara automaticamente la descarga.
    if orden == "skip":
        os.system("python3 ./startup.py")
    elif orden == "abort":
        os.abort
else:
    time.sleep(1)
# url_a_descargar = 
# nombre = 
# urllib.request.urlretrieve(url=url_a_descargar, filename=nombre)
    os.system("python3 ./startup.py normal")