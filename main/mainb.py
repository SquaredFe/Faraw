# Este codigo es el principio estructural de Faraw, aqui es donde puede abrir sus apps de Faraw como
# Faraw Calculate o Faraw Games
# Estructura del programa // import
faraw_ver = "1.0.0"
faraw_rev = "2"
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')
print("¡Te damos la bienvenida a Faraw!")
directorio = os.getcwd()
appsx = ["Salir"]
print(directorio)
subdirectory = directorio.replace("/main", "/")
if os.path.exists(subdirectory + "/appsx/releases/calculate"):
    print("Calculadora de Faraw detectada!")
    appsx + ["Calculadora"]
else:
    print("Calculadora de Faraw no se ha detectado.")
    print("Si has iniciado Faraw sin los parametros 'skip' puede ser que \nFaraw no pueda detectar aplicaciones.")

if os.path.exists(subdirectory + "/appsx/releases/FarawCalendar"):
    print("Calendario de Faraw detectado!")
    appsx + ["Calendario"]
else:
    print("Calculadora de Faraw no se ha detectado.")
    print("Si has iniciado Faraw sin los parametros 'skip' puede ser que \nFaraw no pueda detectar aplicaciones.")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Faraw version " + faraw_ver + ", Revision " + faraw_rev)
print("Bienvenido/a a Faraw, si necesitas ayuda, escribe 'help'. ¡Gracias por utilizar Faraw!")

def dec(cln):
    if cln == "true":
        os.system('cls' if os.name == 'nt' else 'clear')
    usrinp = input("user@faraw $ ")
    if usrinp == "apps -ls":
        print("Tienes las siguientes apps instaladas:")
        if os.path.exists(subdirectory + "/appsx/releases/calculate"):
            print("  Calculadora de Faraw (abrir con 'apps calculadora')")
            
        if os.path.exists(subdirectory + "/appsx/releases/neofetch/Faraw-Neofetch/"):
            print("  Faraw Neofetch (abrir con 'apps neofetch')")
        
        if os.path.exists(subdirectory + "/appsx/releases/FarawCalendar/FarawCalendar"):
            print("  Faraw Calendar (abrir con 'apps calendar')")
        dec("")
    elif usrinp == "help":
        print("¡Bienvenido/a a Faraw, un concepto de sistema operativo textual, aqui te ofrecemos los distintos comandos posibles:")
        print("print [input]           Descripcion: Hace que se escriba un mensaje en la terminal")
        print("apps  [-ls] [nombre de app]  Descripcion: Ejecuta una aplicacion, el argumento 'ls' muestra la lista de apps") 
        print("                             ejemplo: apps calculadora: Abre la calculadora.")
        # print("config                       Descripcion: Abre la configuracion (si esta disponible en /appsx)")
        input("Enter para cerrar...")
        dec(cln="true")
    
    elif usrinp.__contains__("apps") == True:
        if usrinp.__contains__("calculadora") == True:
         os.system("python3 " + subdirectory + "/appsx/releases/calculate/main/main.py")
         print("Volviendo a Faraw...")
         time.sleep(2)
         dec("true")
        elif usrinp.__contains__("neofetch") == True:
            os.system("python3 " + subdirectory + "/appsx/releases/neofetch/Faraw-Neofetch/main/main.py")
            print("Volviendo a Faraw...")
            time.sleep(2)
            dec("true")
        elif usrinp.__contains__("calendar") == True:
            os.system("python3 " + subdirectory + "/appsx/releases/FarawCalendar/FarawCalendar/main/main.py")
            print("Volviendo a Faraw...")
            time.sleep(2)
            dec("true")
        else:
            print("Verifica el comando e intentalo nuevamente")
            dec("")
    elif usrinp == "exit":
        print("Saliendo de Faraw...")
        time.sleep(2)
    elif usrinp.__contains__("print") == True:
        print(usrinp.replace("print ", ""))
        dec("")
    else:
        print(usrinp + ": Orden o funcion no encontrada (¿Perdido? Utiliza la funcion integrada help\n para ver todas las funciones y programas disponibles.)")
        dec(cln="")
dec(cln="")