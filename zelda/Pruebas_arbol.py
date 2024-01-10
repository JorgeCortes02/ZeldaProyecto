import funciones.datos as d
import funciones.funciones as f



espada = False
while True:
    print(d.vida_arbol)
    atacar = input("Escribe: ")
    if atacar == "espada":
        espada = True
    else:
        espada = False
    f.arbol(atacar,espada)