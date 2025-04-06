nombre=input("Escribe tu nombre:")
opcion=input("Ingrese:\n1 para su nombre en MAYUSCULAS\n2 para su numbre en minusculas\n3 para la primer letra en mayusculas ejemplo Franco:\n")
if opcion=="1":
    nombre=nombre.upper()
    print(nombre)
elif opcion=="2":
    nombre=nombre.lower()
    print(nombre)
elif opcion=="3":
    nombre=nombre.title()
    print(nombre)