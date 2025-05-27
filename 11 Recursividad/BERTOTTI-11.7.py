#funcion
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n-1) + n 


#codigo
num=int(input("Ingrese un numero para iniciar la base de la piramide: "))
print(suma_digitos(num))