frase=input("Ingresa una frase: ")
separada=frase.split()
print(separada)
mset=set(separada)
print(mset)
dicc={}
cant=1
for palabra in (separada):
    cant=0
    if palabra in separada:
        cant += 1
    else:
        cant = 1
    dicc[palabra]=cant
print(dicc)