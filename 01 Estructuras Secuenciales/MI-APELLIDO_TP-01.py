#Franco Bertotti - Ejercicio 1
print("Hola Mundo!")
# Franco Bertotti - Ejercicio 2
nombre= input("Ingresa tu nombre: ")
print("Hola " + nombre + "!")
#Franco Bertotti - Ejercicio 3
nombre=input("Como es tu nombre: ")
apellido=input("Como es tu apellido: " )
edad=input("Cual es tu edad: ")
residencia=input("Donde vives: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#Franco Bertotti - Ejercicio 4
radio=float(input("Ingresa el radio: "))
area=3.14159*radio**2
perimetro=2*3.14159*radio
print(f"el area del circulo es {area} y el perimetro es {perimetro}")
#Franco Bertotti - Ejercicio 5
seg=int(input("Ingresa la cantidad de segundos para saber el equivalente en horas: "))
hora=(seg/60)/60
print(f"Equivale a {hora} horas")
#Franco Bertotti - ejercicio 6
num=int(input("Escribe un numero: "))
print(f"tabla de multiplicación: 1x{num}={num*1} 2x{num}={num*2} 3x{num}={num*3} 4x{num}={num*4} 5x{num}={num*5} 6x{num}={num*6} 7x{num}={num*7} 8x{num}={num*8} 9x{num}={num*9} 10x{num}={num*10}")
#Franco Bertotti - Ejercicio 7
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
print(f"{num1}+{num2}={num1+num2}, {num1}/{num2}={num1/num2}, {num1}x{num2}={num1*num2}, {num1}-{num2}={num1-num2}")
#Franco Bertotti - ejercicio 8
altura=float(input("ingrese su altura: "))
peso=float(input("ingrese su peso: "))
imc=peso/(altura**2)
print(f"El IMC es {imc}")
#Franco Bertotti - Ejercicio 9
tempc=int(input("ingrese la temperatura en celsius: "))
tempf=((tempc*(9/5))+32)
print(f"la temperatura en fahrenheit es de: {tempf}")
#Franco Bertotti - Ejercicio 10
num1=float(input("ingrese un numero: "))
num2=float(input("ingrese otro numero: "))
num3=float(input("ingrese otro numero: "))
prom=(num1+num2+num3)/3
print(f"el promedio es: {prom}")