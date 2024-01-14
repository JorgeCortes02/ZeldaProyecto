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


'''while True:
    print(d.vidas)
    print(d.vidas_max)
    print(d.inventarioComida1)
    f.prompt()
    texto = input("Su: ")
    f.comer(texto)'''
linia = ""
for i in d.necluda:
    for j in i:
        linia += j
    linia += "\n"

print(linia)
    
print(d.necluda[10][39])