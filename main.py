# Bienvenido a la parte inicial de Faraw, donde todas las apps se descargan y se integran al sistema.
# Si estas buscando el archivo principal donde Faraw Ejecuta ordenes, puedes ir a /main/mainb.py.
# Si necesitas que Faraw saltee las actualizaciones, ejecuta main.py de esta manera:
# 'python3 ./main.py skip'
import os
import requests
import zipfile

packages_names = ["FarawNeofetch", "FarawCalendar", "FarawCalculate"]
base_url = "https://github.com/SquaredFe/{}/releases/latest/download/{}.far"
output_directory = "./appsx/releases/"

# Crea el directorio de salida si no existe
os.makedirs(output_directory, exist_ok=True)

for package_name in packages_names:
    url = base_url.format(package_name, package_name)
    response = requests.get(url)
    
    if response.status_code == 200:
        # Obtén el nombre del archivo
        filename = os.path.join(output_directory, package_name + ".zip")
        
        # Descarga el archivo .FAR y guárdalo como .zip
        with open(filename, "wb") as file:
            file.write(response.content)
        
        # Extrae el contenido del archivo .zip en un directorio con el mismo nombre
        package_directory = os.path.join(output_directory, package_name)
        os.makedirs(package_directory, exist_ok=True)
        
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(package_directory)
        
        # Borra el archivo .zip
        os.remove(filename)
    
    else:
        print(f"[WARNING] Paquete {package_name} No encontrado, es posible que todavia no se encuentre disponible el paquete .FAR. Continuando con el siguiente.")

print("[INFORMATION] Descarga y extracción completadas.")
os.system("python3 ./main/mainb.py normal")
print("[...]")