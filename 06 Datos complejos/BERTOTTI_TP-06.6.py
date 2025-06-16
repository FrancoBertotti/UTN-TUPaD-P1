alumnos = {}
for i in range(3):
    nombre=input("Ingresa el nombre del alumno: ")
    notas=[]
    for i in range (3):
        numero=int(input("Ingresa una nota: "))
        notas.append(numero)
    tupla=tuple(notas)
    alumnos[nombre] = tupla
print(alumnos)
