#Entrada
cantidad=0
x=1
n=int(input("Cuantas piezas cargara:"))
#Proceso:
while x<=n:
    largo=float(input("Ingrese la medida de la pieza:"))
    if largo>=0.3 and largo<=0.4:
        cantidad=cantidad+1
    x=x+1
print("La cantidad de piezas aptas son:")
print(cantidad)