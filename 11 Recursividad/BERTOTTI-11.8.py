#funcion

def contar_digito(num,dig):
    if num == 0 or dig > 9 or dig <0 :
        return 0
    else:
        if dig == (num%10):
            return contar_digito((num//10),dig) + 1
        else:
            return contar_digito((num//10),dig)

#codigo

numero=int(input("Ingrese un numero: "))
digito=int(input("Ingrese un digito para ver cuantas está en el numero: "))

print(contar_digito(numero,digito))