# Bienvenido al centro de actualizaciones de Faraw, desde la version 2, Faraw podra actualzarse automaticamente al iniciarlo
# Si estas buscando el archivo principal donde Faraw Ejecuta ordenes, puedes ir a /main/mainb.py.
# Si necesitas que Faraw saltee las actualizaciones, ejecuta main.py de esta manera:
# 'python3 ./main.py skip'

# Revision 2 0523
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
data = response.json()
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
api_url = "https://api.github.com/repos/fefedevv/FarawCalculate/releases"
response = urllib.request.urlopen(api_url)
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
print("Transladado a main nuevamente, saliendo...")

api_url = "https://api.github.com/repos/fefedevv/FarawNeofetch/releases"
response2 = urllib.request.urlopen(api_url)
data2 = json.load(response2)
latest_release2 = data2[0]["tag_name"]
url_a_descargar2 = data2[0]["assets"][0]["browser_download_url"]
nombre2 = "neofetch.zip"
destination_dir2 = "./appsx/releases/neofetch"
dexs2 = "./appsx"

urllib.request.urlretrieve(url=url_a_descargar2, filename=nombre2)

with zipfile.ZipFile(nombre2, 'r') as zip_ref:
    os.chmod(dexs2, 0o777)
    try: 
        os.makedirs(destination_dir2)
    except FileExistsError or urllib.error.URLError as e:
        print("La aplicacion Neofetch ya existe o ya se instalo, saltando...")
        print("Es posible que debas de conectarte a internet, tal vez el error se deba a que no se puede conectar a los servidores de GitHub...")
    zip_ref.extractall(destination_dir2)

if os.path.exists(destination_dir2):
    print("La aplicacion Neofetch ya existe o ya se instalo, saltando...")

# Faraw Calendar
api_url = "https://api.github.com/repos/fefedevv/FarawCalendar/releases"
response2 = urllib.request.urlopen(api_url)
data2 = json.load(response2)
latest_release2 = data2[0]["tag_name"]
url_a_descargar2 = data2[0]["assets"][0]["browser_download_url"]
nombre2 = "calendar.zip"
destination_dir2 = "./appsx/releases/FarawCalendar"
dexs2 = "./appsx"

urllib.request.urlretrieve(url=url_a_descargar2, filename=nombre2)

with zipfile.ZipFile(nombre2, 'r') as zip_ref:
    os.chmod(dexs2, 0o777)
    try: 
        os.makedirs(destination_dir2)
    except FileExistsError or urllib.error.URLError as e:
        print("La aplicacion Calendar ya existe o ya se instalo, saltando...")
        print("Es posible que debas de conectarte a internet, tal vez el error se deba a que no se puede conectar a los servidores de GitHub...")
    zip_ref.extractall(destination_dir2)

if os.path.exists(destination_dir2):
    print("La aplicacion Calendar ya existe o ya se instalo, saltando...")
os.system("python3 ./main/mainb.py normal")
print("Transladado a main nuevamente, saliendo...")
