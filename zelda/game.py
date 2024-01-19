import funciones.funciones as f
import funciones.datos as d


cook = True
cesped = True
tree = False
fish = True
chest = False
enemic = False

# Habrá que cambiar esto por que se activen los objetos que tiene al lado

def game(): # Hay que mirar como se pondria para cuando eliges una partida guardada.
    exit = False 
    while exit == False: # Bucle para que cuando le des a exit en el menu salga del juego
        #exit = f.menu_principal() # Ejecutamos el menu principal, devuelve un booleano, si es falso es porque has pulsado exit
        #if exit == False: # Salir de la función
        #    exit = True
        #    return True
        
        posicionplayer = d.jugador["posicion"]
        mapaActual = d.localitzacions[d.jugador["mapa"]]
            
        f.zorro_visivilidad() # miramos visibilidad del zorro
        final = False 
        while final == False: # Bucle para la partida
            f.limpiar_pantalla()
            f.cofre_cerrar_sword()
            f.cofre_cerrar_shield()
            f.contador_arbol_mapa(mapaActual)
            f.contador_arbol(mapaActual)
            
            # Crear diccionario de ganon con sus vidas
            if d.ganon["vida"] == 0: # si la vida de ganon es 0, se muestra la pantalla de win
                d.win = True
                f.limpiar_pantalla()
                f.imprimirmapa_menu(d.diccionarioMenuPrincipal["zelda_saved"])
                d.texto_prompt.append("It has been an exhausting fight, but with persistence, you have achieved it.") # Se añade esta frase al prompt
                f.prompt()
                opc = input("What to do now? ")
                while opc.lower() != "continue": # Mientras no se escriba la opcion continue, no saldran de la pantalla de win
                    f.limpiar_pantalla()
                    f.imprimirmapa_menu(d.diccionarioMenuPrincipal["zelda_saved"])
                    d.texto_prompt.append("Invalid action")
                    f.prompt()
                    opc = input("What to do now? ")
                
                # Esto hay que camiarlo, y resetear todo
                d.texto_prompt = [] # Se reinicia el prompt
                d.ganon["vida"] = 9 # Se reinician las vidas de Ganon
                return False # Devolvemos falso para no terminar el bulce y que vuelva a aparecer el menu principal
            
            elif d.jugador["vidas"] == 0: # si la vida del jugador es 0, se muestra la pantalla de muerte
                f.imprimirmapa_menu(d.diccionarioMenuPrincipal["link_death"])
                d.texto_prompt.append("Nice try, you died, game is over") # Se añade al prompt esta frase
                f.prompt()
                opc = input("What to do now? ") 
            
                while opc.lower() != "continue": # Mientras no escriban la opcion continue, no saldra de esta pantalla
                    f.limpiar_pantalla()
                    f.imprimirmapa_menu(d.diccionarioMenuPrincipal["link_death"])
                    d.texto_prompt.append("Invalid action")
                    f.prompt()
                    opc = input("What to do now? ")
                
                # Esto hay que cambiarlo, y reiniciar todo (esto es para pruebas)
                d.texto_prompt = [] # Se reinicia el prompt
                d.jugador["vidas"] = 3 # Se reinician las vidas
                return False # Devolvemos falso para no terminar el bulce y que vuelva a aparecer el menu principal
            
            mapaActual = f.obtenerMapa(mapaActual) # Se imprime el mapa, y se deja al jugador en su posicion
            f.menuInferior() # se imprime el menu inferior
            f.prompt() # se imprime el prompt
            select = input("What to do now? ") # select de la accion a realizar
            d.texto_prompt.append(select) # se añade el la accion al prompt
            
            if d.jugador["mapa"] == "hyrule" or d.jugador["mapa"] == "gerudo" or d.jugador["mapa"] == "death" or d.jugador["mapa"] == "necluda": # si no estas en castillo, movimiento y acciones normales
            
                if select[0:7].lower() == "go left" or select[0:8].lower() == "go right" or select[0:5].lower() == "go up" or select[0:7].lower() == "go down": # mover personaje
                    retorno = f.moverPersonaje(mapaActual, select, posicionplayer) # llanmada a la funcion de mover el personaje
                    posicionplayer = [retorno[1], retorno[2]]
                    d.jugador["posicion"] = posicionplayer # nueva posicion del jugador
                
                # No me cambia de menu, hay que cambiar datos de prueba a los del diccionario
                elif select[0:14].lower() == "show inventary": # si se escribe show inventory
                    if select.lower() == "show inventary food": # se cambia al inventario de comida
                        d.select = "show inventory food"
                    
                    elif select.lower() == "show inventary weapons": # se cambia al inventario de armas
                        d.select = "show inventory weapons"
                    
                    elif select.lower() == "show inventary main": # se cambia al inventario principal
                        d.select = "show inventory main"
                    
                    elif select.lower() == "show inventary help": # se muestra la pantalla de help del menu
                        f.limpiar_pantalla()
                        f.imprimirmapa_menu(d.diccionarioMenuPrincipal["help_inventory"])
                        f.prompt()
                        opc = input("What to do now? ")
                        while opc.lower() != "back":
                            d.texto_prompt.append("Invalid option")
                            f.limpiar_pantalla()
                            f.imprimirmapa_menu(d.diccionarioMenuPrincipal["help_inventory"])
                            f.prompt()
                            opc = input("What to do now? ")
                        
                    
                    else: # opcion incorrecta se añade al prompt
                        d.texto_prompt.append("Invalid action")
                
                elif select[0:8].lower() == "show map": # Muestra el mapa de la region
                    f.mostrar_mapa()
                
                elif select[0:3].lower() == "eat": # Consumir comida
                    f.comer(select)
                
                elif select[0:11].lower() == "unequip the": # Desequipar arma
                    # Sigue saliendo en el inventario, y si no tienes espada o escudo equipado te tiene que dar un texto de error.
                    d.texto_prompt.append(f.desequiparArma(select))
                    
                elif select[0:9].lower() == "equip the": # Equipar arma
                    # Me da error la funcion cuando busca las armas disponibles
                    f.equiparArma(select)
                
                elif select[0:4].lower() == "cook":  # Cocinar comida, cuando estas al lado de una C
                    f.cocinar(select, d.inventarioComida, mapaActual)
                    
                elif select.lower() == "attack": # Atacar a un enemigo, cuando esta a tu lado
                    ejecutado = False
                    ejecutado = f.atacar(posicionplayer, mapaActual, "E")
                
                    if ejecutado == False:
                        ejecutado = f.atacar(posicionplayer, mapaActual, "F") # Falta quitarle vida al arma y añadir carne al inventario
                
                    if ejecutado == False:
                        ejecutado = f.atacar(posicionplayer, mapaActual, "T") # Falta acabar la funcion de arboles, da error con la vida
                    
                    if ejecutado == False:
                        ejecutado = f.atacar(posicionplayer, mapaActual, " ")
                
                elif select.lower() == "fish": # Pescar cuando estas al lado de una ~
                    f.agua(mapaActual) # Falta añadir al inventario el pez conseguido
                
                elif select.lower() == "open sanctuary": # Abrir un santuario, cuando estas al lado de un santuario 
                    f.abrir_santuario(posicionplayer, mapaActual) # Hay que crear un diccionario o lista con los santuarios y que cuando abres uno se ponga en True en el diccionario.
                
                elif select[0:5].lower() == "go to": # Cambiar de región
                    # en el pdf no pone nada, asi que a castle se puede ir desde cualquier sitio, y dentro de castle no se puede ir a otro sitio, tienes que atacar a ganon o escribir back y volver a la ultima region donde has estado.
                    retorno = f.cambiar_mapa(select, mapaActual, posicionplayer)
                    mapaActual = retorno[0]
                    posicionplayer = retorno[1]
                    
                
                elif select[0:5].lower() == "go by": # moverte al objeto indicado más cercano a donde estas
                    f.movimientoCercano(select, mapaActual)
                
                elif select.lower() == "open chest": # Abrir cofre, cuando estas al lado de una M o W
                    f.cofre(mapaActual) 
                    
                elif select[0:5].lower() == "cheat": # Trucos
                    # Falta terminar la funcion de trucos
                    print("a")
                
                else: # Opcion invalida, se añade al prompt
                    d.texto_prompt.append("Invalid action")
            
            else: # Si estas en el mapa del castillo, tienes movimientos limitados
                if select[0:7].lower() == "go left" or select[0:8].lower() == "go right": # Solo puedes moverte a derecha o izquierda
                    retorno = f.moverPersonajeGanon(mapaActual, select, posicionplayer)
                    posicionplayer = [retorno[1], retorno[2]] # Cambiar posicion a nueva despues del movimiento
                
                elif select.lower() == "back": # Volver a la ultima región, desde donde has viajado hasta el castillo
                    d.texto_prompt.append("You are now in " + d.mapa_anterior) # Se añade al prompt
                    mapaActual = d.localitzacions[d.mapa_anterior] # Se cambia el mapa
                    posicionplayer = d.dades[d.mapa_anterior]["position"] # Se cambia la posicion
                
                elif select.lower() == "attack" and posicionplayer == [9,21]: # Atacar a Ganon, cuando estas a su lado
                    # Falta funcion para atacar a ganon
                    aux = d.ganon["vida"]
                    d.ganon["vida"] = aux - 1 
                    f.frase_ganon()
                
                elif select[0:5].lower() == "cheat": # Trucos
                    # Falta terminar funcion trucos
                    print("a")
                
                else: # Opción invalida, se añade al prompt
                    d.texto_prompt.append("Invalid action")
                        
juego = True                         

while juego == True: # Mientras no se eliga la opción exit del menu principal           
    terminar = game() # Se ejecuta el juego
    
    if terminar == True: # Si la opcion elegida ha sido exit en el menu principal
        juego = False # Termina el bucle