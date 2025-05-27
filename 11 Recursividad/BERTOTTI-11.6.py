# funcion

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n//10) + n%10

# codigo 

num=int(input("Ingrese un numero para la suma de sus digitos: "))
print(suma_digitos(num))