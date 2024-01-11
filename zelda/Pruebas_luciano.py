import funciones.datos as d
import funciones.funciones as f



#espada = False #prubas arbol
#while True:
#    f.prom()
#    atacar = input("Escribe: ")
#    if atacar == "espada":
#        espada = True
#    else:
#        espada = False
#    f.arbol(espada)


while True:
    print(d.vidas)
    print(d.vidas_max)
    print(d.inventarioComida1)
    f.prompt()
    texto = input("Su: ")
    f.comer(texto)