import funciones.funciones as f
import funciones.datos as d
import random

#menu_inicial = f.menu_random()
#f.menu_principal(menu_inicial)

diccio = {"vegetable123456":{"nombre":"vegetable"}, "vegetable654321":{"nombre":"vegetable"}, "vegetable654328":{"nombre":"vegetable"}, "vegetable123457":{"nombre":"vegetable"}, "fish654321":{"nombre":"fish"}, "meat654328":{"nombre":"meat"}}


#while True:
#    for i in diccio:
#        print(diccio[i])
#    receta = input("What to do now?")
#    if receta[:4].lower() == "cook":
#        f.cocinar(receta, diccio)
#
#    else:
#        print("Invalid Option")

    
#while True:
#    add = True
#    santuarios = []
#
#    while add == True:
#        opc = input("Quieres abrir un santuario? (S/N) ")
#        if opc.lower() == "s":
#            lal = input("Cual quieres abrir? ")
#            santuarios.append(lal+"?")
#        
#        elif opc.lower() == "n":
#            add = False
#        
#        else:
#            print("Invalid option")
#
#    opc = input("What to do now? ")
#
#    if opc.lower() == "show map":
#          f.mostrar_mapa(santuarios)
#    
#    else:
#         print("Invalid action")


def funcion_en_funcion():
    a = "hola"
    print(a)
    
    
def funcion_normal(funcion):
    print("a")
    funcion


funcion_normal(funcion_en_funcion())



# Enemigo, vida y movimiento
# Atacar a Ganon, ya esta hecho que te tengas que poner en la posicion de al lado suyo para atacar, faltaria hacer que te haga daño y quitarle vida y tambien que se quiten los corazones que tiene despues del nombre en el mapa
# Terminar opcion menu consultas BBDD