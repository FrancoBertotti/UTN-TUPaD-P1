#funciones

def serie_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return serie_fib(num-1) + serie_fib(num-2)
    
#codigo
num1=int(input("Ingrese un numero: "))
print(f"La serie Fibonacci hasta la posision {num1} es: {serie_fib(num1)}")
