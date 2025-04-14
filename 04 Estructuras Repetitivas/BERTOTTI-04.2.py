import math
num=int(input("ingrese un numero: "))
cont=0
while num > 0:
    num=num/10
    num=math.trunc(num)
    cont=cont+1
print(f"el numero tiene {cont} digitos")