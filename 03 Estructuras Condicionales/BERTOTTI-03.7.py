#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
frase=input("Escribe una frase o palabra: ")
ultimaL=frase[-1]
#usar[-1] para evaluar desde el final al principio
if ultimaL=="a"or ultimaL=="e" or ultimaL=="i" or ultimaL=="o" or ultimaL=="u":
    print(frase,"!")
else :
    print(frase)
