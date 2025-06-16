contactos = {}
for i in range(5):
    contactos[input("Ingresa el nombre de contacto: ")] = int(input("Ingresa el numero del contacto: "))
print(contactos)
print(contactos[input("Ingresa el nombre de contacto para ver el numero: ")])