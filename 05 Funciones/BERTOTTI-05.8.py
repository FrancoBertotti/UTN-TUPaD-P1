#funciones
def calcular_imc(peso,altura):
    print(f"El IMC es de: {round((peso/(altura**2)),2)}")

#código
num=float(input("Ingresa el peso (kg): "))
num2=float(input("Ingresa la altura (m): "))
calcular_imc(num,num2)