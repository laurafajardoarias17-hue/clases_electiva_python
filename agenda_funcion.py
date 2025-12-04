def pedir_nombre():
    return input("Ingresa el nombre del estudiante: ")

def pedir_telefono():
    return input("Ingresa el teléfono: ")

def pedir_direccion():
    return input("Ingresa la dirección: ")

def guardar_y_mostrar_estudiantes(archivo, cantidad):
    with open("agenda_laura2.txt", "w") as ejemplo:
        for _ in range(cantidad):
            nombre = pedir_nombre()
            telefono = pedir_telefono()
            direccion = pedir_direccion()
            
            ejemplo.write(nombre + ", " + telefono + ", " + direccion + "\n")

def agenda_laura()
with open("agenda_laura2.txt","r") as ejemplo:
    print(f"\n agenda laura\n")
    print(ejemplo.read())