#funcion

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
# codigo

cadena=input("Ingrese una palabra para ver si es palindromo: ")
print(es_palindromo(cadena))