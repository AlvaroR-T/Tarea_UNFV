#Entrada
edad=int(input("¿Qué edad tienes? "))
#Proceso
if edad>0 and edad<18:
    print("Eres un menor de edad")
elif edad>=18 and edad<60:
    print("Eres un adulto")
elif edad>=60 and edad<100:
    print("Eres un adulto mayor")
else:
    print("Eres una Persona longeva")