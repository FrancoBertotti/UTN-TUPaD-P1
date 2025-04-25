#ejercico 1
lista=list(range(4,101,4))
print(lista)
#ejercicio 2
lista2=["avion","auto","moto","barco","bicicleta"]
print(lista2[-2])
#ejercicio 3
listaVacia=[]
listaVacia.append("perro")
listaVacia.append("gato")
listaVacia.append(16)
print(listaVacia)
#ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[3]="oso"
print(animales)
#ejercicio 5
#si comenzamos desde el .remove, eso va a eliminar un elemento de la
#lista, lo que quiere eliminar es el numero mayor de los int que
#contiene la lista, con la funcion "max"
#numeros=[8,15,3,22,7]
#numeros.remove(max(numeros))
#print(numeros)
#ejercicio 6
lista6=list(range(10,31,5))
print(lista6[0:2])
#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1]="vento"
autos[2]="corolla"
print(autos)
#ejercicio 8
dobles=[]
for i in range (5,20,5):
    acu=i*2
    dobles.append(acu)
print(dobles)
#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras [1].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(compras)
#ejercicio 10
lista_anidada=[15,True,[25.5,57.9,30.6],False]
print(lista_anidada)