#Decl.
c=0
n=int(input("Ingrese la cantidad de números: "))
#Proceso:
for n in range(1,n+1):
    num =int(input("Ingrese número: "))
    if num%2==0:
     c=c+1

print("Hay", c,"número pares")