#Entrada,dec
nombre=input("Ingrese el Nombre del trabajador: ")
print("Mucho gusto,",nombre)
horas=int(input("Cuántas horas a la semana trabajas: "))
Precio=float(input("Cuánto le pagan por hora: "))
#Proceso
if horas<=60:
    pago1=horas*Precio
    print("El sueldo Final de ",nombre,"es S/",pago1)
else:
    H_extras=horas-60
    pago2=60*Precio
    PagoFinal=pago2 + (H_extras*Precio*3)
    print("El sueldo Final de ",nombre,"es S/",PagoFinal)