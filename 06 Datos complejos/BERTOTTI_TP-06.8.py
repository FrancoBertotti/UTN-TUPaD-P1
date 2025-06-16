prod = {}
r=True
while r == True:
    prod[input("Ingresa el nombre del producto: ")] = int(input("cantidad de stock: "))
    e=input("Desea seguir agregando productos? 'S' o 'N': ")
    if e == "N":
        r=False
    elif e == "n":
        r=False
    else:
        r=True
print(prod)
print("Ingresa 1 para consultar stock, 2 para modificar stock o 3 para agregar nuevo prodcuto")
opcion=int(input("Opcion: "))
if opcion == 1:
    cons=input("ingresa el nombre a consultar stock: ")
    stock=prod[cons]
    print(f"para el producto {cons} el stock es de: {stock}")
elif opcion == 2:
    cons=input("ingresa el nombre del producto a cambiar stock: ")
    prod[cons]=int(input("ingrese nuevo stock: "))
    stock=prod[cons]
    print(f"para el producto {cons} el stock es de: {stock}")
elif opcion == 3:
    r=True
    while r == True:
        prod[input("Ingresa el nombre del producto: ")] = int(input("cantidad de stock: "))
        e=input("Desea seguir agregando productos? 'S' o 'N': ")
        if e == "N":
            r=False
        elif e == "n":
            r=False
        else:
            r=True
print(prod)