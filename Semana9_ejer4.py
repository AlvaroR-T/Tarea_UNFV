#Decl.
b=0
n=int(input("Ingrese la cantidad de números: "))
#Proceso:
for n in range(1,n+1):
    num =int(input("Ingrese número: "))
    if num%2==0:
     b=b+1
    else:
      x=n-b  

print("Hay", b,"números pares", "y", x,"números impares")