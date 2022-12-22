#Declaración de variables:
print("Ingrese el número que guste:")
print("1:Hallar la suma de ángulos internos de un polígono regular:")
print("2:Área del triángulo equilátero:")

Opc=int(input("Opc: "))

#Proceso:
if Opc==1 :
    print("Eligió la Suma de ángulos internos de un polígono regular")
    print("Ingrese el número de lados de dicho polígono:")
    n=int(input("n: "))
    Suma=(180*(n-2))
    print("La suma de ángulos internos del polígono regular es:", Suma)

elif Opc==2 :
    print("Eligió el Área del triángulo equilátero:")
    print("Ingrese el lado del triángulo:")
    X=float(input("X:"))
    Área=X**2*((3**0.5)/4)
    print("El Área del triángulo es:",Área) 
else: Opc>=3
print("Operación no válida")
    

