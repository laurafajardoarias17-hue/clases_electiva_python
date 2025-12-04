# import funciones

# print("calculadora basica")
# print("1.suma")
# print("2.resta")
# print("3.multiplicacion")
# print("4.division")
    
# opcion=input("escriba una de la opcioes anteriores(1-4):")
    
# a=float(input("ingrese el primer numero:"))
# b=float(input("ingrese el segundo numero:"))
    
# if opcion =="1":
#     print("resultado:",funciones.suma(a,b))
# elif opcion== "2":
#     print("resultado:",funciones.resta(a,b))
# elif opcion=="3":
#     print("resultado:", funciones.multiplicacion(a,b))
# elif opcion =="4":
#     print("resultado:",funciones.division(a,b))
# else:
#     print("opcion no valida")
from funciones import suma, resta
print(suma(2,3),resta(5,3))