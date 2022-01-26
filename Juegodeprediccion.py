#Juego de predicción

import random as ran


def adivina_el_numero(x):

    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("Bienvenidos al Juego de Adivinación!!!!")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("Su objetivo es adivinar el numero aleatorio")
    

    numero_aleatorio = ran.randint(1, x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("intenta otra vez. Este numeo es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez. Este numero es muy grande.")

    print(f"!Felicitaciones! Adviniaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)

#agregar el while de menu, y los demás juegos