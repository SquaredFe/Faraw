# Bienvenido a Faraw, este concepto de sistema operativo textual desarrollado en el lenguaje python, este archivo
# es el main, aca es donde la estructura principal de Faraw se desarrolla.
#
# Si necesitas aplicaciones como calculadora, ve a el directorio /appsx/releases/.
# este es uno de los archivos que mas se actualize cada vez que se agregue una nueva app.

import time
import urllib.request
import urllib.error
import os
import sys
import zipfile

if len(sys.argv) > 1:
    orden = sys.argv[1]
    # Si la orden es "skip" el sistema saltara automaticamente la descarga.
    if orden == "skip":
        os.system("python3 ./dev.py")
    elif orden == "abort":
        os.abort
else:
    time.sleep(1)
# Calculate
url_a_descargar = "https://github.com/fefedevv/FarawCalculate/releases/download/v.1.0.0rev.1/FarawCalculate.zip"
nombre = "calculate.zip"
destination_dir = "./appsx/releases/calculate"
dexs = "./appsx"
urllib.request.urlretrieve(url=url_a_descargar, filename=nombre)
with zipfile.ZipFile(nombre, 'r') as zip_ref:
    os.chmod(dexs, 0o777)
    try: 
        os.makedirs(destination_dir)
    except FileExistsError or urllib.error.URLError as e:
        print("La aplicacion Calculadora de Faraw ya existe o ya se instalo, saltando...")
        print("Es posible que debas de conectarte a internet, tal vez el error se deba a que no se puede conectar a los servidores de GitHub...")
    zip_ref.extractall(destination_dir)
    

    
if os.path.exists(destination_dir):
    print("La aplicacion Calculadora de Faraw ya existe o ya se instalo, saltando...")
os.system("python3 ./main/mainb.py normal")
print("Transladado a main nuevamente, saliendo...")