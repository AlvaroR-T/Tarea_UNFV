#Entrada
print("Usted ha sido recompensado por su arduo trabajo en la Empresa")
po=2500
horas=int(input("Introduce el número de horas adicionales trabajadas: "))
#Proceso:
for i in range(horas):
    po=po*1.25+48
    print("Luego de ",i+1,"horas trabajadas,usted recibirá ", "S/",po)
print("Siga esforzándose en el trabajo,muchas gracias")