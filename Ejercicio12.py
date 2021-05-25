# Escribe un programa que te permita jugar a una versión simplificada del
# juego Master Mind. El juego consistirá en adivinar una cadena de números
# distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
# a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
# cadena de números. En cada intento, el programa informará de cuántos números
# han sido acertados (el programa considerará que se ha acertado un número si
# coincide el valor y la posición).


import random

def mastermind():
    print("De cuantas cifras sera la cadena?")
    cadena = int(input())
    print("Cual es tu numero elegido?")
    numero = int(input())
    variable = ""
    score = 0
    print(range(cadena))
    for num in range(cadena):
        x = random.randint(0, 9)
        x = str(x)
        variable += x
        print(variable)
        
    for x in cadena:
        cadena = str(cadena)

        if cadena[x] == variable[x]:
            score += 1
        else:
            pass
    print("Has adivinado:", score , "numeros!")

mastermind()