#Ejercicios 1, 2 y 3

#1)
print("Ejercicio 1:\n")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas)
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(f"Con añadidos: \n{precios_frutas}")
print("\n")

#2)

print("Ejercicio 2:\n")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(f"Con cambios de precios: \n{precios_frutas}")
print("\n")

#3)

print("Ejercicio 3:\n")
lista=precios_frutas.keys()
print(f"Ahora solo las frutas: \n{lista}")