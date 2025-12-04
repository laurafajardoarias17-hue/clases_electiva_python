with open("agenda_laura.txt","w") as ejemplo:
     for i in range(6):
         nombre=input("ingresa el nombre del estudiante:")
         telefono=input("ingrese el telefono:")
         direccion=input("ingresa la direccion:")
         ejemplo.write(nombre + ", "+ telefono+", "+ direccion +"\n")
         
with open ("agenda_laura.txt","r") as ejemplo:
    print("\n lista de estudiantes guardados:" )
    print(ejemplo.read())