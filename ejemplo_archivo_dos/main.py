import funciones

archivo = "archivo_ejemplo_laura.csv"

while True:
    print("menú")
    print("1.ver estudiantes")
    print("2. agregar estudiante")
    print("3.salir")
    
    opcion = input("seleccione una opcion:")
    
    if opcion == "1":
        ests=funciones.leer_estudiantes(archivo)
        for e in ests:
            print(f"{e[´bre´]}-{e[´edad´]}años-{e[´direccion]})
    elif opcion=="2":
    nombre=input("nombre:")
    edad=input("edad:")
    direccion=input("direccion:")
    
    if not funciones.validar_nombre(nombre)
    print("nombre invalido")
    continue
    
    if not funciones.validar_edad(edad):
    print("edad invalida")
    continue
    
    if not funciones.validar_direccion(direccion):
    print("direccion invalido")
    
    funciones.agregar_estudiante(archivo,nombre,edad