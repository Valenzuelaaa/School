# Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
# Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año
#  se aplica la tasa de interés introducida. del x por cien durante n años se convierte en C * (1 + x/100)
#  elevado a n (años). Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual 
#  se convierte en 24117.14 dolares al cabo de 20 años.



def casioFinal():
    print("Ingrese la cantidad de dolares")
    dolares = int(input())
    print("Ingrese la cantidad de interes")
    interes = float(input())
    print("Ingrese el plazo")
    tiempo = int(input())
    print("")
    
    final = casiofx(dolares, interes, tiempo)
    print("La conversion final es de: ",final)

def casiofx(dolares,interes,tiempo):
    calculo = dolares * ((1 + interes/100)) ** tiempo
    
    return calculo

casioFinal()

