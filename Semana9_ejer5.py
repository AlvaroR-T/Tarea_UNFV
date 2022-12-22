#Declaración de var.
a=int(input("Ingrese un número: "))
b=int(input("Ingrese un número: "))
#Proceso
for i in range(a,b+1):
    x=i**3
    print("El cubo de", i, "es",x)
