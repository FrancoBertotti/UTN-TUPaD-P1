#funciones
def operaciones_basicas(a,b):
    print(f"{a}+{b}={a+b}\n{a}-{b}={a-b}\n{a}x{b}={a*b}\n{a}/{b}={a/b}\n") #saltos de linea para que se aprecie mejor el resultado

#código
num=int(input("Ingresa un número: "))
num2=int(input("Ingresa otro número: "))
operaciones_basicas(num,num2)