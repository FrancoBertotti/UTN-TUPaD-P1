#funciones

def a_binario (num):
    if num == 0:
        return ''
    else:
        return a_binario(num // 2) + str(num % 2)
    
#codigo

num=int(input("Ingrese un numero: "))
print(f"El numero en binario es de: {a_binario(num)}")