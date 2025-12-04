# # # # # # # # # # # # # # # # # # # # # # # # textoEjemplo='hola buenas noches'
# # # # # # # # # # # # # # # # # # # # # # # # print(textoEjemplo.upper())
# # # # # # # # # # # # # # # # # # # # # # # textoEjemplo='Hola Buenas Noches'
# # # # # # # # # # # # # # # # # # # # # # # print(textoEjemplo.lower())
# # # # # # # # # # # # # # # # # # # # # # textoejemplo="hola buenas noches"
# # # # # # # # # # # # # # # # # # # # # # print(textoejemplo.replace("noches","tardes"))
# # # # # # # # # # # # # # # # # # # # # texto="  hola mundo  "
# # # # # # # # # # # # # # # # # # # # # limpio=texto.strip()
# # # # # # # # # # # # # # # # # # # # # print(limpio)
# # # # # # # # # # # # # # # # # # # # texto=">>>hola<<<"
# # # # # # # # # # # # # # # # # # # # nuevo=texto.strip("><")
# # # # # # # # # # # # # # # # # # # # print(nuevo)
# # # # # # # # # # # # # # # # # # # texto="programar en python es divertido"
# # # # # # # # # # # # # # # # # # # pos= texto.find("casa")
# # # # # # # # # # # # # # # # # # # print(pos)
# # # # # # # # # # # # # # # # # # palabra="python"
# # # # # # # # # # # # # # # # # # print(palabra[0])
# # # # # # # # # # # # # # # # # # print(palabra[0:3])
# # # # # # # # # # # # # # # # # # print(palabra[2:])
# # # # # # # # # # # # # # # # # # print(palabra[-1])
# # # # # # # # # # # # # # # # # palabra="programa en python"
# # # # # # # # # # # # # # # # # print(len(palabra))
# # # # # # # # # # # # # # # # numero=6
# # # # # # # # # # # # # # # # print(f"tabla del {numero}")
# # # # # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # # # # #     print(f"{numero}x{i}={numero*i}")
# # # # # # # # # # # # # # # numero_secreto=6
# # # # # # # # # # # # # # # intento=int(input("adivina el numero del 1 al 10:"))
# # # # # # # # # # # # # # # while intento != numero_secreto:
# # # # # # # # # # # # # # #     print("incorrecto intente otra vez")
# # # # # # # # # # # # # # #     intento=int(input("adivina el numero deñ 1 al 10: "))
# # # # # # # # # # # # # # # print(f"¡correcto! {numero_secreto} es el numero secreto")
# # # # # # # # # # # # # # contador=0
# # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # #     contador+=1
# # # # # # # # # # # # # # print(f"el bucle se ejecuto {contador} veces")
# # # # # # # # # # # # # acumulador=0
# # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # #     numero=int(input("ingresar un numero:"))
# # # # # # # # # # # # #     acumulador+=numero
# # # # # # # # # # # # # print(f"la suma total es :{acumulador}")
# # # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # # print(estudiantes[0])
# # # # # # # # # # # # print(estudiantes[1])
# # # # # # # # # # # # print(estudiantes[5])
# # # # # # # # # # #  estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # print(estudiantes[-1])
# # # # # # # # # # # print(estudiantes[-2])
# # # # # # # # # # # print(estudiantes[-5])
# # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # estudiantes.append("lissth")
# # # # # # # # # # # print(estudiantes)
# # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # estudiantes.insert(1,"dario")
# # # # # # # # # # # print(estudiantes)
# # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # estudiantes[1]="maria"
# # print(estudiantes)
# # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # estudiantes[1:4]=["maria","pedro","juan"]
# # # # # # # # # # # print(estudiantes)
# # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # estudiantes.remove("antonio")
# # # # # # # # # # # print(estudiantes)
# # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # estudiantes.pop(4)
# # # # # # # # # # # print(estudiantes)
# # # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # # estudiantes.sort()
# # # # # # # # # # # print(estudiantes)
# # # # # # # # # # estudiantes=["veronica","laura","antonio","julian","brayan","santiago"]
# # # # # # # # # # estudiantes.sort(reverse=True)
# # # # # # # # # # print(estudiantes)
# # # # # # # # # numeros=[]
# # # # # # # # # for i in range(5):
# # # # # # # # #     numero=int(input("ingrese un numero:"))
# # # # # # # # #     numeros.append(numero)
# # # # # # # # # print(f"la lista final es:{numeros}")
# # # # # # # # # persona={
# # # # # # # # #     "nombre":"ana",
# # # # # # # # #     "edad":20,
# # # # # # # # #     "ciudad":"bogota"
# # # # # # # # # }
# # # # # # # # # print(persona["nombre"])
# # # # # # # # # print(persona["edad"])
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # estudiante["nota"]=4.8
# # # # # # # # # print(estudiante)
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # estudiante["curso"]="programacion"
# # # # # # # # # print(estudiante)
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # del estudiante["edad"]
# # # # # # # # # print(estudiante)
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # estudiante.clear()
# # # # # # # # # print(estudiante)
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # for clave in estudiante:
# # # # # # # # #     print (clave)
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # for clave, valor in estudiante.items():
# # # # # # # # #     print (f"{clave}:{valor}")
# # # # # # # # # estudiante={"nombre":"laura","edad":20,"nota":4.5}
# # # # # # # # # for valor in estudiante.values():
# # # # # # # # #     print (valor)
# # #  frutas={"manzana","pera","banano"}
# # # # # # # # # print(frutas)
# # # # # # # numeros = {1,2,3,4,5}
# # # # # # # print(numeros)
# # # # # # colores={"rojo","azul"}
# # # # # # colores.add("verde")
# # # # # # print(colores)
# # # # # # colores={"rojo","azul","verde"}
# # # # # # colores.remove("azul")
# # # # # # print(colores)
# # # # # colores={"rojo","azul","verde"}
# # # # # colores.discard("rojo")
# # # # # print(colores)
# # # # # A={"rojo","verde","azul"}
# # # # # B={"amarillo","verde","negro"}
# # # # # union=A|B
# # # # # print(union)
# # # # # A={"rojo","verde","azul"}
# # # # # B={"amarillo","verde","negro"}
# # # # # union=A.union(B)
# # # # # print(union)
# # # # A={"rojo","verde","azul"}
# # # # B={"amarillo","verde","negro"}
# # # # inter=A&B
# # # # print(inter)
# # # # A={"rojo","verde","azul"}
# # # # B={"amarillo","verde","negro"}
# # # # inter=A.intersection(B)
# # # # print(inter)
# # # # A={"rojo","verde","azul"}
# # # # B={"amarillo","verde","negro"}
# # # # diferencia = A-B
# # # # print(diferencia)
# # # A={"rojo","verde","azul"}
# # # B={"amarillo","verde","negro"}
# # # diferencia= A.difference(B)
# # # print(diferencia)
# # # A={"rojo","verde","azul"}
# # # B={"amarillo","verde","negro"}
# # # dif_sim=A^B
# # # print(dif_sim)
# # A={"rojo","verde","azul"}
# # B={"amarillo","verde","negro"}
# # dif_sim=A.symmetric_difference(B)
# # print(dif_sim)
# # ARCHIVOS
# # archivo=open("ejemplo.txt","w")
# # archivo.write("mi nombre es\n")
# # archivo.write("laura fajardo\n")
# # archivo.close()
# # archivo=open("ejemplo.txt","a")
# # contenido=archivo.write("nueva linea agregada\n")
# # archivo.close()
# # archivo=open("ejemplo.txt","r")
# # contenido=archivo.read()
# # print(contenido)
# # archivo.close()
# # with open("notas.txt","a") as archivo:
# #     archivo.write("nueva linea agregada\n")
# # AGREGAR
# with open("estudiantes.txt","w") as ejemplo:
#      for i in range(3):
#          nombre=input("ingresa el nombre del estudiante:")
#          ejemplo.write(nombre + "\n")
# with open ("estudiantes.txt","r") as ejemplo:
#     print("\n lista de estudiantes guardados:" )
#     print(ejemplo.read())

# # BBASIO
# with open ("estudiante.txt","w") as archivo:
#     pass