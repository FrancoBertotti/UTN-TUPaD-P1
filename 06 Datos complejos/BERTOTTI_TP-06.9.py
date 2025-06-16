dia=int(input("ingresa el dia: "))
hora=str(input("ingresa la hora: "))
mitupla=(dia,hora)
evento=input("ingresa el evento: ")
dicci={}
dicci[mitupla]=evento
print(f"Agenda: {dicci}")