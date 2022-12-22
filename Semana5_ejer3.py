#Entrada,dec.
vo=int(input("Ingrese la velocidad inicial(m/s): "))
Time=int(input("Ingrese el tiempo(seg): "))
dist=int(input("Ingrese la distancia: "))
#Constante
g=9.8

#Proceso
vf=(vo**2+2*g*dist)**0.5

#Salida:
print("La velocidad final es: ", vf)