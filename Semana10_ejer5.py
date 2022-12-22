#Entrada
print("Multiplicación generada a partir de los valores brindados")
num=int(input("Cuántos números va a ingresar:"))
#Proceso:
if num <=0:
    print("Imposible")
else:
    prod=1
    for i in range(1, num+1 ):
        a=float(input(f"Escriba el número {i} : "))
        prod=prod*a
    print("La multiplicación de los números escritos es:",prod)