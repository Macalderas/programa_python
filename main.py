import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from programas.suma import sumar2
from programas.resta import restar2
from vistas.menu import menu2
from vistas.lieas import lineas2


from datetime import datetime
import os

programa = True

while programa:
    os.system("clear")  # usa "cls" si estás en Windows
    print("Hora:", datetime.now().strftime("%H:%M:%S"))
    print("+-------------------------+")
    lineas2(25)
    menu2()

    res = int(input("|[?] "))

    if res == 1:
        print("Sumar dos números")
        sumar2()

    elif res == 2:
        print("Restar dos números")
        restar2()

    elif res == 0:
        print("Salir del programa")
        programa = False
