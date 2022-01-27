import random


#Juego de predicción
def adivina_el_numero(x):

    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("Bienvenidos al Juego de Adivinación!!!!")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("Su objetivo es adivinar el numero aleatorio")
    

    numero_aleatorio = random.randint(1, x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("intenta otra vez. Este numeo es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez. Este numero es muy grande.")

    print(f"!Felicitaciones! Adviniaste el numero {numero_aleatorio} correctamente")


#Juego Rock-Paper-Scissor
def jugar():
    print("                                       ")
    print("--------------------------------------")
    print("Bienvenidos a Piedra Papel o Tijeras!!")
    print("--------------------------------------")
    print("                                       ")

    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, o 'ti' para tijeras. \n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    
    if usuario == computadora:
        print("la computadora elijio " + computadora)
        return 'EMPATE!!!'
    else:
        if gano_el_jugador(usuario,computadora):
            print("la computadora elijio " + computadora)
            return 'GANASTE!!!!'
    
        else:
            print("la computadora elijio " + computadora)
            return 'Perdiste :('


def gano_el_jugador(jugador, oponente):
    if ((jugador == 'ti' and oponente =='pa') or 
    (jugador == 'pa' and oponente == 'pi') or
    (jugador == 'pi' and oponente == 'ti')):
        return True
    else:
        return False



def menu():

    x = 0

    while x != 3:

        print("                                       ")
        print(f"-------------------------------------------------------")
        print(f"Bienvenido al sistema de Juegos de Free-Code-Camp!!!!")
        print(f"-------------------------------------------------------")
        print(f"Presione 1 para jugar a Adivinar el Numero!")
        print(f"Presione 2 para jugar a piedras, papel, tijeras!")
        print(f"Presione 3 para salir")
        print("                                       ")
        x = int(input('Ingrese su opcion: '))


        if x == 1:
            n = int(input("dame un numero"))
            adivina_el_numero(n)

        if x == 2:
            jugar()



if __name__ == '__main__':
    menu()