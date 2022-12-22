#Entrada
print("Suma generada a partir de los valores brindados")
num=int(input("Cuántos números va a ingresar:"))
#Proceso:
if num <=0:
    print("Imposible")
else:
    sum=0
    for i in range(1, num+1 ):
        a=float(input(f"Escriba el número {i} : "))
        sum=sum+a
    print("La suma de los números escritos es:",sum)