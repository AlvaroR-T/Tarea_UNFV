#Entras y declaración de las variables
b=float(input("Lado b: "))
c=float(input("Lado c: "))
print("Ingrese el ángulo en grados sexagesimales: ")
alfa=float(input())
import math
#Constante:
Pi=3.1416
#Proceso,fórmula de la ley de cosenos:
a=(b**2+c**2-2*b*c*math.cos(alfa*Pi/180))**0.5
#SALIDA:
print("El lado a es: ",a)