num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
acu=0
if num1 < num2:
    menor=num1+1
    mayor=num2
elif num1 > num2:
    menor=num2+1
    mayor=num1
else:
    print("los numeros no pueden ser el mismo")
#print(menor,mayor) de pueba 
while menor<mayor:
    acu=acu+menor
    menor=menor+1
if acu != 0:
    print(f"la suma de los numeros dentro del rango es de {acu}")