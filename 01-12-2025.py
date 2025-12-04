# FUNCIONES
def saludar(nombre):
    return f"¡hola,{nombre}! bienvenidos a clase numero 8."
mensaje=saludar("laura")
print(mensaje)
def suma (a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division (a,b):
    if b!=0:
         return a/b
    else:
         return"¡¡¡error!!!- no se puede dividir entre cero"
def calculadora():
    print("calculadora basica")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    
    opcion=input("escriba una de la opcioes anteriores(1-4):")
    
    primernumero=float(input("ingrese el primer numero:"))
    segundonumero=float(input("ingrese el segundo numero:"))
    
    if opcion =="1":
        print("resultado:",suma(primernumero, segundonumero))
    elif opcion== "2":
        print("resultado:",resta(primernumero, segundonumero))
    elif opcion=="3":
        print("resultado:", multiplicacion(primernumero, segundonumero))
    elif opcion =="4":
        print("resultado:",division(primernumero,segundonumero))
    else:
        print("opcion no valida")
calculadora()        
    