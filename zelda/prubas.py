import funciones.datos as d  
def equiparArma(Select):

    if len(d.inventarioArmas )== 0:

        print("No hay armas en el inventario")

    if Select.find("Wood Shield") != -1:

        if Select[Select.find("Wood Shield"): ]:

            Select = Select[Select.find("Wood Shield"): ]
    
    elif Select.find("Shield") != -1 and Select.find("Wood") == -1:

        if Select[Select.find("Shield"): ] :

             Select = Select[Select.find("Shield"): ]

    elif Select.find("Wood Sword") != -1:

        if Select[Select.find("Wood Sword"): ]:

            Select = Select[Select.find("Wood Shield"): ]

     
    elif Select.find("Sword") != -1 and Select.find("Wood") == -1:

        if Select[Select.find("Sword"): ] :

             Select = Select[Select.find("Shield"): ]
    
    lista_dict = list(d.inventarioArmas.keys())
    

    if len(lista_dict)== 0:

        print ("No dispones de este arma en tu inventario.")

    for i in range(len(lista_dict)):
        for j in range(0, len(lista_dict)-i-1):
            if lista_dict[j]["usos"] > lista_dict[j+1]["usos"]:
                lista_dict[j]["usos"], lista_dict[j+1]["usos"] = lista_dict[j+1]["usos"], lista_dict[j]["usos"]

    if "Shield" in lista_dict[0]:

        d.jugador["escudo_actual"] = lista_dict[0]
    
    elif "Sword" in lista_dict[0]:

        d.jugador["arma_actual"] = lista_dict[0]
      
        
            
