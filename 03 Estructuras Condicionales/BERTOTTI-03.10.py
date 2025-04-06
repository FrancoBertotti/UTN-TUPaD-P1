hemis=input("Ingrese N si vive en el hemisferio norte o S si vive en el sur: ")
mes=input("Ingrese, en minusculas, el mes del año en el que se encuentra: ")
dia=int(input("Ingrese el numero del día: "))
#hacer anidación
if hemis=="N" or hemis=="n":
    if mes=="enero" or mes=="febrero" or (mes=="diciembre" and dia>=21) or (mes=="marzo" and dia<=20):
        print("Usted esta en invierno")
    elif mes=="abril" or mes=="mayo" or (mes=="marzo" and dia>=21) or (mes=="junio" and dia<=20):
        print("Usted esta en primavera")
    elif mes=="julio" or mes=="agosto" or (mes=="junio" and dia>=21) or (mes=="septiembre" and dia<=20):
        print("Usted esta en verano")
    elif mes=="octubre" or mes=="noviembre" or (mes=="septiembre" and dia>=21) or (mes=="diciembre" and dia<=20):
        print("Usted esta en otoño")
elif hemis=="S" or hemis=="s":
    if mes=="enero" or mes=="febrero" or (mes=="diciembre" and dia>=21) or (mes=="marzo" and dia<=20):
        print("Usted esta en verano")
    elif mes=="abril" or mes=="mayo" or (mes=="marzo" and dia>=21) or (mes=="junio" and dia<=20):
        print("Usted esta en otoño")
    elif mes=="julio" or mes=="agosto" or (mes=="junio" and dia>=21) or (mes=="septiembre" and dia<=20):
        print("Usted esta en invierno")
    elif mes=="octubre" or mes=="noviembre" or (mes=="septiembre" and dia>=21) or (mes=="diciembre" and dia<=20):
        print("Usted esta en primavera")
