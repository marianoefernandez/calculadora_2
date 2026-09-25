import time
import platform
import subprocess
from funciones import *
from salidas import *
from entradas import *

def limpiar_consola() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls",shell=True)#WINDOWS
    else:
        subprocess.run("clear",shell=True)#OTROS SO (MAC y LINUX)
    print("\n\n")

def refrescar_menu(tiempo_menu:int = 0,mensaje_menu:str = "Toque enter para continuar...", ) -> None:
    time.sleep(tiempo_menu)
    if tiempo_menu == 0:
        input(mensaje_menu)
    limpiar_consola()

def mostrar_menu_calculadora() -> None:
    print("1. Ingresar el primer numero")
    print("2. Ingresar el segundo numero")
    print("3. Calcular la suma")
    print("4. Calcular la resta")
    print("5. Calcular la division")
    print("6. Calcular la multiplicacion")
    print("7. Calcular potencia")
    print("8. Calcular el factorial")
    print("9. Calcular todos los resultados")
    print("10. Salir")

def ejecutar_menu_calculadora() -> None:
    bandera_primer_numero = False
    bandera_segundo_numero = False

    while True:
        #Primer Paso --> Mostrar el menu
        mostrar_menu_calculadora()
        #Para interactuar con el menu yo voy a utilizar un if-elif o un match
        #Segundo Paso --> Elegir que opcion del menu quiero

        opcion = pedir_entero_rango(1,10,"Ingrese una opcion en el menu: ","ERROR, la opcion tiene que estar entre (1 y 10)")
        limpiar_consola()

        #if-elif-else
        if opcion == 1:
            numero_uno = int(input("Ingrese el primer numero: "))
            bandera_primer_numero = True
        elif opcion == 2:
            numero_dos = int(input("Ingrese el segundo numero: "))
            bandera_segundo_numero = True
        elif opcion == 10:
            print("SALIENDO DEL PROGRAMA")
            break
        elif bandera_primer_numero == False or bandera_segundo_numero == False:
            print("DEBE INGRESAR LOS NUMEROS PARA PODER CONTINUAR...")
        elif opcion == 3:
            resultado_suma = calcular_suma(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_suma,"+")
        elif opcion == 4:
            resultado_resta = calcular_resta(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_resta,"-")
        elif opcion == 5:
            resultado_division = calcular_division(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_division,"/")
        elif opcion == 6:
            resultado_multiplicacion = calcular_multiplicacion(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_multiplicacion,"*")
        elif opcion == 7:
            resultado_potencia = calcular_potencia(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_potencia,"elevado a")
        elif opcion == 8:
            factorial_uno = calcular_factorial(numero_uno)
            factorial_dos = calcular_factorial(numero_dos)
            informar_factorial(numero_uno,numero_dos,factorial_uno,factorial_dos)
        elif opcion == 9:
            informar_resultados(numero_uno,numero_dos)

        refrescar_menu()#Va a ponerme el mensaje Toque enter para continuar...
        # refrescar_menu(3)#Va a permitirme esperar 3 segundos sin mostrarme ningun mensaje que diga "Toque enter para continuar..."
        # refrescar_menu(mensaje_menu="Hola Mundo")#Cambia el mensaje por defecto

def interactuar_menu(lista_datos:list) -> bool:
    print("EN DESARROLLO CUANDO VEAMOS LISTAS")