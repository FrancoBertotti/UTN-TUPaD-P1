clasif=int(input("Por favor ingrese la magnitud del terremoto en escala de Richter: "))
if clasif<3 :
    print("Muy leve")
elif clasif>=3 and clasif<4:
    print("Leve")
elif clasif>=4 and clasif<5:
    print("Moderado")
elif clasif>=5 and clasif<6:
    print("Fuerte")
elif clasif>=6 and clasif<7:
    print("Muy fuerte")
elif clasif>=7:
    print("Extremo")