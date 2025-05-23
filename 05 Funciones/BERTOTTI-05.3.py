#funciones
def imprimir_info(nom,ap,ed,res):
    print(f"Soy {nom} {ap}, tengo {ed} años y vivo en {res}")#la funcion imprime esa frase con esos fundamentos

#código
nombre=input(("Ingresa tu nombre: "))
apel=input(("Ingresa tu apellido: "))
edad=input(("Ingresa tu edad: "))
resid=input(("Ingresa tu residencia: "))

imprimir_info(nombre,apel,edad,resid)