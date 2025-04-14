import math
num=int(input("ingrese un numero: "))
num2=0
acu=0
while num > 0:
    num2=num%10
    num=math.trunc(num/10)
    acu=(acu*10)+num2
print(f"El numero invertido es: {acu}")