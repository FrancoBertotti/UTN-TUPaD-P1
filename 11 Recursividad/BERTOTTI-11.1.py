#Funcion

def factorial(num):
    if num == 1:
        return 1
    elif num <= 0:
        return "Error, el numero no puede ser 0 o menor."
    else:
        return num * (factorial(num-1))

#codigo

num1=int(input("Ingrese un numero: "))
print(f"El factorial de {num1} es: {factorial(num1)}")