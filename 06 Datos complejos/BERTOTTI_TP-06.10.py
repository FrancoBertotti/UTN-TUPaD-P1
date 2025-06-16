dicc1={"Argentina":"Buenos Aires","Chile":"Santiago"}
print(f"diccionario original: {dicc1}")
l1=list(dicc1.values())
l2=list(dicc1.keys())
dicc2=dict(zip(l1,l2))
print(f"diccionario invertido: {dicc2}")