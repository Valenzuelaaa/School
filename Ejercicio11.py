# Diseñar un sistema de puntos para el juego El reino del dragón:
# La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
# Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, entra en
# la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde, saldrá en pantalla el 
# total de los puntos que realizo y la opción de empezar de nuevo.
import time
import random

def intro():
    print ("Bienvenido al juego, el reino del dragon!")
    print ("Prueba tu suerte el dia de hoy!")
    print ("Elige un cueva y dependiendo el humor del dragon guardian se te concederan monedas o seras comido por el guardian")
    print ("Intenta conseguir el mayor numero de monedas en equipo, Buena suerte!.")
    print ("")

def CuevaActual():
    intro()
    cueva = ""
    while cueva == "":
        print("Adentrandote en la cueva del señor dragon, ves dos caminos, por cual decides entrar? cueva 1 o 2?")
        break
    cueva = input()
    return cueva

inicio = "Si"
Coins = 0

while inicio == "Si":
    Decision = CuevaActual()
    caidaMortal = random.randint (1, 20)
    print ("Comienzas tu caminata hacia cueva #",Decision)
    time.sleep(3)
    print ("Al seguir caminando ves una luz a unos metros de donde te encuentras")
    time.sleep(2)
    if caidaMortal > 15:
        print("Antes de llegar a la guarida del dragon, se abre un hoyo en el suelo y caes a tu muerte, Fin del juego")
    else:
        print ("Subes la mirada y un dragon se encuentra custodiando un tesoro, te dice: Estoy pensando en un numero maldito del 1 al 10, si adivinas el numero maldito, he de terminar tu vida humano, de conseguir un numero sin maldicion, compartire una parte de mi tesoro contigo")
        print ("Elige un numero del 1 al 10:")
        respuesta = input()
        time.sleep(2)
        numeroMaldito = random.randint(1,10)
        print("El numero maldito es", numeroMaldito)


 
    if respuesta != (numeroMaldito):
        print ("Bien hecho humano, toma cualquier pedazo de equipo y te dire su valor ")
        equipo = random.randint(50, 200)
        print("Eliges un equipo al azar, el equipo tiene un valor de: ",equipo) 
        Coins += equipo
    else:
        print ("Mala suerte humano, lo hare rapido para que no sufras")
        print ("El dragon crea una bola de fuego y te pulveriza")
        print("Valor conseguido en equipo: ",Coins)
        inicio = input("Deseas intentarlo de nuevo?: Si o No" )
        Coins = 0
        