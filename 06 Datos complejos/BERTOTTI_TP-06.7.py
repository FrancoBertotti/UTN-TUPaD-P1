#alumnos como numeros de matricula 

set1 = {101, 105, 110, 115, 120, 125}
set2 = {105, 115, 120, 130, 135, 140}
ambos_parciales = set1.intersection(set2)
print(f"Los alumnos que aprobaron ambos parciales son: {ambos_parciales}")
un_parcial = set1.symmetric_difference(set2)
print(f"Los alumnos que aprobaron un solo parcial son: {un_parcial}")
sin_repet = set1.union(set2)
print(f"Los alumnos que aprobaron al menos un parcial son: {sin_repet}")