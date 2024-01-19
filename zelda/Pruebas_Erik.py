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



# Inventario de comida, salta error
# Equipar y desequipar, (puede ser que lo este utilizando mal)
# Cocinar, falta detectar si estas en una C para poder cocinar
# Atacar, cuando no tienes espada salta error (al atacar arbol, zorro y enemigo, cesped va bien) (Y cuando tienes espada tambien falla)
# Fish, lo mismo que cocinar falta detectar el agua
# Cambiar de mapa, cuando abres un santuario y cambias de mapa salta un error
# Movimiento cercano, la x no aparece en la nueva posicion y no se borra la posicion anterior
# Abrir cofre, no cambia la M por una W
# Atacar a Ganon, ya esta hecho que te tengas que poner en la posicion de al lado suyo para atacar, faltaria hacer que te haga daño y quitarle vida y tambien que se quiten los corazones que tiene despues del nombre en el mapa
# Terminar conexión BBDD