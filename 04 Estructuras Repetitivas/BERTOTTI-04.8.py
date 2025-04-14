pares=0
impares=0
pos=0
neg=0
#si o si inicilizar variables antes del bucle en este caso
for i in range (100):
    num=int(input("Por favor ingrese un numero: "))
    if num % 2 == 0:
        pares=pares+1
        if num > 0:
            pos=pos+1
        elif num < 0:
            neg=neg+1
    elif num % 2 !=0:
        impares=impares+1
        if num > 0:
            pos=pos+1
        elif num < 0:
            neg=neg+1
print(f"ha ingresado {pares} numeros pares, {impares} impares, {pos} positivos y {neg} negativos")