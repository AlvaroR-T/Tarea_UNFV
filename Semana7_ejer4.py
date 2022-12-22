#Entrada-Declaración
print("Bienvenido a nuestra tienda,estimado cliente")
Nom_Prod=input("Ingrese el nombre del producto: ")
Precio_Prod=int(input("Ingrese el precio del producto: "))
Cant_Prod=int(input("Ingrese la cantidad de productos: "))
#Proceso
importe=Precio_Prod*Cant_Prod
descuento=importe*0.22
Total_a_pagar=importe-descuento
#Salida
print("El importe es: ",importe)
print("El descuento es: ",descuento)
print("El Monto total a pagar es: ",Total_a_pagar)