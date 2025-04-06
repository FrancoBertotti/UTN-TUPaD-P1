from statistics import mode, median, mean
import random
numerosAleatorios= [random.randint(1,100) for i in range (50)]
print(numerosAleatorios)
mediana=median(numerosAleatorios)
media=mean(numerosAleatorios)
moda=mode(numerosAleatorios)
print("mediana:",mediana, "media:",media, "moda:",moda)
if media>mediana and mediana>moda:
    print("Hay sesgo positivo")
elif media<mediana and mediana<moda:
    print("Hay sesgo negativo")
elif media==mediana and mediana==moda:
    print("No hay sesgo")