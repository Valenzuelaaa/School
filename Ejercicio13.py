# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
# las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
# últimas tiene que decir que riman un poco y si no, que no riman.

print("Ingresa la primera palabra")
word1 = input()
print("Ingresa la segunda palabra")
word2= input()


def gallos(word1,word2):

    if word1[-1]==word2[-1] and word1[-2]==word2[-2] and word1[-3]==word2[-3]:
        print("Riman")

    elif word1[-1]==word2[-1] and word1[-2]==word2[-2]:
        print("Les falta para rimar")
        
    else: 
        print("Las palabras no riman")


gallos(word1,word2)