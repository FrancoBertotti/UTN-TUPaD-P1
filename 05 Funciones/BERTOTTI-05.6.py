#funciones
def tabla_multiplicar(num):
    for i in range (1,11):
        print(f"{i}x{num}={i*num}") #el calculo en la misma linea sin declarar nuevas variables

#código
num=int(input("Ingresa un número: "))
tabla_multiplicar(num)