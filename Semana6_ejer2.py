#Entrada
SUELDO=float(input("Ingrese Sueldo: "))

#Proceso
if SUELDO<1500:
    AUM=SUELDO*0.10
    SUELDO_N=SUELDO+AUM
    print("El sueldo es: ",SUELDO_N)
else:
    print("El sueldo es: ",SUELDO)