import math
#funciones

def calcular_area_circ(rad):
    print(f"El area del circulo es: {math.pi*(rad**2)}") #calcula en la misma linea el area
def calcular_perimetro_circ(rad):
    print(f"El perimietro del circulo es: {2*rad*math.pi}")

#código
radio=int(input("Ingresa el radio del circulo: "))

calcular_area_circ(radio)
calcular_perimetro_circ(radio)