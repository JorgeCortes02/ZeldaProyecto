import funciones.funciones as f
import funciones.datos as d


cook = True
cesped = False
tree = False
fish = True
santuario = True
chest = True
enemic = True
# Habrá que cambiar esto por que se activen los objetos que tiene al lado

def game(): # Hay que mirar como se pondria para cuando eliges una partida guardada. 
    f.menu_principal()
    posicionplayer = d.dades["hyrule"]["position"]
    mapaActual = d.localitzacions["hyrule"]
    final = False
    while final == False:
        f.limpiar_pantalla()
        mapaActual = f.obtenerMapa(mapaActual, posicionplayer)
        f.menuInferior(mapaActual)
        f.prompt()
        select = input("What to do now? ")
        
        if mapaActual != d.localitzacions["castle"] or mapaActual != d.localitzacions["castle_win"]:
        
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
                    d.texto_prompt("Invalid action")
            
            elif select[0:8].lower() == "show map":
                f.mostrar_mapa()
            
            elif select[0:3].lower() == "eat":
                # Falta la funcion de comer que la hace Luciano
                print("a")
            
            elif select[0:11].lower() == "unequip the": # Hay que mirar por que cuando desequipo un arma sigue saliendo en el inventario.
                d.texto_prompt.append(f.desequiparArma(select))
                
            elif select[0:9].lower() == "equip the": # Me da error la funcion
                f.equiparArma(select)
            
            elif select[0:4].lower() == "cook" and cook == True: # Hay que mirar como detectar si se puede cocinar o atacar y esas cosas.
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
            
            elif select[0:5].lower() == "go to": # en el pdf no pone nada, asi que a castle se puede ir desde cualquier sitio, y dentro de castle no se puede ir a otro sitio, tienes que atacar a ganon.
                mapaActual = f.cambiar_mapa(select, mapaActual) # En gerudo hay A y en el pdf no sale nada sobre las A (supongo que son aguas)
            
            elif select[0:5].lower() == "go by":
                # Falta terminar la funcion para del movimiento cercano
                print("a")
            
            elif select.lower() == "open chest" and chest == True:
                f.abrir_cofre() # Falta ver como hacemos lo de los cofres abiertos, que se reinicien y tal.
                
            elif select[0:5].lower() == "cheat": # Falta hacer la funcion de trucos
                print("a")
            
            else:
                d.texto_prompt.append("Invalid action")
        
        else:
            if select[0:7].lower() == "go left" or select[0:7].lower() == "go right":
                f.moverPersonajeGanon(mapaActual, select, posicionplayer)
            
            elif select.lower() == "back": # Hay que hacer que cuando pongas back en el castillo vuelvas a la ultima localizacion donde has estado.
                print("a") # Variable para mapa anterior y con mi funcion
            
            elif select.lower() == "attack": # Falta funcion para atacar a ganon
                f.frase_ganon()
                if d.ganon["vida"] == 0: # Crear diccionario de ganon con sus vidas
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
                    
                    final = True
                    
                
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
                    
                    final = True # Y pot ultimo como hacer que cuando se acabe una partida vuelva al menu principal.
            
            elif select[0:5].lower() == "cheat": # Falta funcion trucos
                print("a")
            
            else:
                d.texto_prompt.append("Invalid action")
                    
                              
            
game()