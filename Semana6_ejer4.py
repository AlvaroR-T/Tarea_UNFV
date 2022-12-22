#Entrada,dec.
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese un número: "))
num3=int(input("Ingrese un número: "))
#Proceso:
if num1>=num2 and num1>=num3:
    mayor=num1
elif num2>=num1 and num2>=num3:
    mayor=num2
else:
    mayor=num3

if num1<=num2 and num1<=num3:
    menor=num1
elif num2<=num1 and num2<=num3:
    menor=num2
else:
    menor=num3
#salida
print("El número mayor es: ",mayor)
print("El número menor es: ",menor)