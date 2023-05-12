# Este codigo es el principio estructural de Faraw, aqui es donde puede abrir sus apps de Faraw como
# Faraw Calculate o Faraw Games
# Estructura del programa // import
import os
import curses
import time
screen = curses.initscr()
curses.cbreak()
screen.clear()
num = 1
screen.addstr("Bienvenido a Faraw! Faraw esta autodetectando tus apps...")
screen.refresh()
time.sleep(4)

opciones = ["Faraw Calculate", "Faraw Settings", "Faraw ...", "Salir"]
opcion_seleccionada = 0
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Función para imprimir las opciones y la flecha
def imprimir_opciones(stdscr, opcion_seleccionada):
    stdscr.clear()
    
    # Imprimimos las opciones
    for i, opcion in enumerate(opciones):
        if opcion_seleccionada == i:
            # Si es la opción seleccionada, la marcamos con la flecha
            stdscr.addstr(i, 0, "  > " + opcion)
        else:
            stdscr.addstr(i, 0, "    " + opcion)
    stdscr.refresh()

# Imprimimos las opciones y la flecha por primera vez
imprimir_opciones(stdscr, opcion_seleccionada)

# Loop para mover la flecha con las teclas de flecha arriba y abajo
while True:
    tecla = stdscr.getch()
    if tecla == curses.KEY_UP:
        opcion_seleccionada = max(0, opcion_seleccionada - 1)
    elif tecla == curses.KEY_DOWN:
        opcion_seleccionada = min(len(opciones) - 1, opcion_seleccionada + 1)
    elif tecla == ord('\n'):
        # Si se presiona Enter, salimos del loop y mostramos la opción seleccionada
        break
    # Actualizamos la pantalla con las nuevas opciones y flecha
    imprimir_opciones(stdscr, opcion_seleccionada)

# Mostramos la opción seleccionada
stdscr.addstr(len(opciones) + 1, 0, "Seleccionaste la opción: " + opciones[opcion_seleccionada] + ", continuando...")
time.sleep(2)

# Esperamos a que el usuario presione cualquier tecla para salir
stdscr.getch()

# Restauramos la configuración original de la pantalla
curses.echo()
curses.nocbreak()
curses.endwin()
if opcion_seleccionada == 0:
    ruta_actual = os.path.dirname(os.path.abspath(__file__)) # Obtiene la ruta actual del archivo
    ruta_anterior = os.path.abspath(os.path.join(ruta_actual, os.pardir)) # Navega a la carpeta anterior
    ruta_main = os.path.join(ruta_anterior, 'appsx')
    ruta_main2 = os.path.join(ruta_main, 'releases')
    ruta_mainf = ruta_main2 + "/calculate/main/main.py"
    os.system("python3 " + ruta_mainf)
    
    os.system("python3 " + ruta_actual + "/mainb.py")
elif opcion_seleccionada == 3:
    print("¡Adios!")
    curses.echo()
    curses.nocbreak()
    curses.endwin()