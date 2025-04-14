#usar .append para concatenar los ingresos del usuario y colocar lista con los [] para que alamacene varios int
from statistics import median
mediana=0
lista=[]
for i in range (100):
    num=int(input("Ingrese un numero: "))
    lista.append(num)
mediana=median(lista)
#print(lista) de control
print(f"La mediana es {mediana}")