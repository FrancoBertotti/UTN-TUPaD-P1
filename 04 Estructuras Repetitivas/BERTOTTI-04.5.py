import random
inten=1
num=random.randint(0,9)
#print(num)
numus=int(input("Ingrese un numero para adivinar del 0 al 9: "))
while numus != num:
    numus=int(input("Ingrese otro numero: "))
    inten = inten+1
print(f"Intentó {inten} veces")