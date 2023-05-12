# Bienvenido al centro de actualizaciones de Faraw, desde la version 2, Faraw podra actualzarse automaticamente al iniciarlo
# Si estas buscando el archivo principal donde Faraw Ejecuta ordenes, puedes ir a /main/mainb.py.
# Si necesitas que Faraw saltee las actualizaciones, ejecuta main.py de esta manera:
# 'python3 ./main.py skip'

import time
import urllib.request
import urllib.error
import os
import sys
import zipfile
import requests
import json
# Hacer una solicitud GET a la API de GitHub
response = requests.get("https://api.github.com/repos/fefedevv/FarawCalculate/releases/latest")

# Analizar la respuesta JSON
data = response.json()

# Obtener el nombre del último release
latest_release = data["name"]


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
# URL de la API de GitHub para obtener información de los releases
api_url = "https://api.github.com/repos/fefedevv/FarawCalculate/releases"

# Hacer una solicitud GET a la API de GitHub
response = urllib.request.urlopen(api_url)

# Analizar la respuesta JSON
data = json.load(response)

# Obtener la última versión del release
latest_release = data[0]["tag_name"]
url_a_descargar = data[0]["assets"][0]["browser_download_url"]

# Descargar la última versión
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
