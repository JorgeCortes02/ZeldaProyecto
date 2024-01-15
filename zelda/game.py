import funciones.funciones as f
import funciones.datos as d


cook = True
cesped = True
tree = False
fish = True
santuario = False
chest = False
enemic = False

# Habrá que cambiar esto por que se activen los objetos que tiene al lado

def game(): # Hay que mirar como se pondria para cuando eliges una partida guardada.
    exit = False
    while exit == False:
        exit = f.menu_principal()
        if exit == False:
            exit = True
            return True
        
        posicionplayer = d.dades["hyrule"]["position"]
        mapaActual = d.localitzacions["hyrule"]
        f.zorro_visivilidad() 
        final = False
        while final == False:
            f.limpiar_pantalla()
            
            if d.ganon["vida"] == 0: # Crear diccionario de ganon con sus vidas
                        f.limpiar_pantalla()
                        f.imprimirmapa_menu(d.diccionarioMenuPrincipal["zelda_saved"])
                        d.texto_prompt.append("It has been an exhausting fight, but with persistence, you have achieved it.")
                        f.prompt()
                        opc = input("What to do now? ")
                        while opc.lower() != "continue":
                            f.limpiar_pantalla()
                            f.imprimirmapa_menu(d.diccionarioMenuPrincipal["zelda_saved"])
                            d.texto_prompt.append("Invalid action")
                            f.prompt()
                            opc = input("What to do now? ")
                        
                        d.texto_prompt = []
                        d.ganon["vida"] = 9
                        return False
            
            elif d.jugador["vidas"] == 0:
                f.imprimirmapa_menu(d.diccionarioMenuPrincipal["link_death"])
                d.texto_prompt.append("Nice try, you died, game is over")
                f.prompt()
                opc = input("What to do now? ")
            
                while opc.lower() != "continue":
                    f.limpiar_pantalla()
                    f.imprimirmapa_menu(d.diccionarioMenuPrincipal["link_death"])
                    d.texto_prompt.append("Invalid action")
                    f.prompt()
                    opc = input("What to do now? ")
                
                d.texto_prompt = []
                d.jugador["vidas"] = 3
                return False
            
            mapaActual = f.obtenerMapa(mapaActual, posicionplayer)
            f.menuInferior(mapaActual)
            f.prompt()
            select = input("What to do now? ")
            d.texto_prompt.append(select)
            
            if mapaActual == d.localitzacions["hyrule"] or mapaActual == d.localitzacions["gerudo"] or mapaActual == d.localitzacions["death"] or mapaActual == d.localitzacions["necluda"]:
            
                if select[0:7].lower() == "go left" or select[0:8].lower() == "go right" or select[0:5].lower() == "go up" or select[0:7].lower() == "go down":
                    retorno = f.moverPersonaje(mapaActual, select, posicionplayer) 
                    posicionplayer = [retorno[1], retorno[2]]
                
                elif select[0:14].lower() == "show inventory":
                    if select.lower() == "show inventory food":
                        d.select = "show inventory food"
                    
                    elif select.lower() == "show inventory weapons":
                        d.select = "show inventory weapons"
                    
                    elif select.lower() == "show inventory main":
                        d.select = "show inventory main"
                    
                    else:
                        d.texto_prompt.append("Invalid action")
                
                elif select[0:8].lower() == "show map":
                    f.mostrar_mapa()
                
                elif select[0:3].lower() == "eat":
                    # Falta la funcion de comer 
                    print("a")
                
                elif select[0:11].lower() == "unequip the": # Hay que mirar por que cuando desequipo un arma sigue saliendo en el inventario.
                    d.texto_prompt.append(f.desequiparArma(select))
                    
                elif select[0:9].lower() == "equip the": # Me da error la funcion
                    f.equiparArma(select)
                
                elif select[0:4].lower() == "cook" and cook == True: 
                    f.cocinar(select, d.inventarioComida)
                    
                elif select.lower() == "attack" and enemic == True:
                    # Falta funcion de enemigo
                    print("a")
                
                elif select.lower() == "attack" and d.visibilidad_zorro == True:
                    f.zorro() # Falta quitarle vida al arma y añadir carne al inventario
                
                elif select.lower() == "attack" and tree == True:
                    f.arbol(d.jugador["arma_actual"]) # Falta acabar la funcion de arboles, da error con la vida
                    
                elif select.lower() == "attack" and cesped == True: # Lo mismo que cocinar
                    f.cesped()
                
                elif select.lower() == "fish" and fish == True:
                    f.agua() # Falta añadir al inventario el pez conseguido
                
                elif select.lower() == "open sanctuary" and santuario == True:
                    f.abrir_santuario() # Hay que crear un diccionario o lista con los santuarios y que cuando abres uno se ponga en True en el diccionario.
                    # Tambien hay que mirar que al mostrar el mapa de la región los santuarios abiertos se tiene que eliminar el ?, y igual con los del mapa jugable
                
                elif select[0:5].lower() == "go to": # en el pdf no pone nada, asi que a castle se puede ir desde cualquier sitio, y dentro de castle no se puede ir a otro sitio, tienes que atacar a ganon o escribir back y volver a la ultima region donde has estado.
                    retorno = f.cambiar_mapa(select, mapaActual)
                    mapaActual = retorno[0]
                    posicionplayer = retorno[1]
                    
                
                elif select[0:5].lower() == "go by":
                    # Falta terminar la funcion para del movimiento cercano
                    print("a")
                
                elif select.lower() == "open chest" and chest == True:
                    f.cofre() # Falta ver como hacemos lo de los cofres abiertos, que se reinicien y tal.
                    
                elif select[0:5].lower() == "cheat": # Falta terminar la funcion de trucos
                    f.trucos(select)
                
                else:
                    d.texto_prompt.append("Invalid action")
            
            else:
                if select[0:7].lower() == "go left" or select[0:8].lower() == "go right":
                    retorno = f.moverPersonajeGanon(mapaActual, select, posicionplayer)
                    posicionplayer = [retorno[1], retorno[2]]
                
                elif select.lower() == "back": 
                    d.texto_prompt.append("You are now in " + d.mapa_anterior) 
                    mapaActual = d.localitzacions[d.mapa_anterior]
                    posicionplayer = d.dades[d.mapa_anterior]["position"]
                
                elif select.lower() == "attack" and posicionplayer == [9,21]: # Falta funcion para atacar a ganon
                    aux = d.ganon["vida"]
                    d.ganon["vida"] = aux - 1 
                    f.frase_ganon()
                
                elif select[0:5].lower() == "cheat": # Falta funcion trucos
                    f.trucos(select)
                
                else:
                    d.texto_prompt.append("Invalid action")
                        
                              

while True:            
    terminar = game()
    
    if terminar == True:
        break