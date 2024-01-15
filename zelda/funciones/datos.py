import funciones.funciones as f




objetos_gerudo = {" ":{"funciones":f.cesped},
                  "F":{"posicion":[8,47],"visibilidad":visibilidad_zorro,"funcion":f.zorro}, 
                  "C":{"posicion":[4,15],"funcion":f.cocinar},
                  "T":{"lista":[[8,5],[2,29],[2,30],[2,31],[3,31],[3,32]],"vida":[4,4,4,4,4,4],"contador":[0,0,0,0,0,0],"funcion":f.arbol},
                  "~":{"posicion":[[8,57],[8,56],[9,55],[9,54],[10,53],[10,52],[10,51]],"pesca":pesca,"funcion":f.agua},
                  "S4":{"posicion":[[3,45],[3,46]],"puerta":False,"funcion":f.abrir_santuario},
                  "M":{"posicion":[[9,7],[1,52]],"abierto":[False,False],"cierre":f.cofre_cerrar_sword,"funcion":f.cofre}, #-Falta la funcion de cerrar los cofres
                  "E":{"posicion":[[[4,3],[4,4]],[[6,38],[6,39]]],"vidas":[5,5],"funcion":f.enemigos}}

objetos_death = {" ":{"funciones":f.cesped},
                  "F":{"posicion":[2,30],"visibilidad":visibilidad_zorro,"funcion":f.zorro}, 
                  "C":{"posicion":[9,6],"funcion":f.cocinar},
                  "T":{"lista":[[7,19],[8,18],[9,18]],"vida":[4,4,4],"contador":[0,0,0],"funcion":f.arbol},
                  "~":{"posicion":[[3,2],[3,3],[4,2],[4,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],
                                   [6,8],[6,9],[6,10],[7,7],[7,6],[7,5],[6,4],[6,3],[6,2]],"pesca":pesca,"funcion":f.agua},
                  "S2":{"posicion":[[3,6],[3,7]],"puerta":False,"funcion":f.abrir_santuario},
                  "S3":{"posicion":[[9,49],[9,50]],"puerta":False,"funcion":f.abrir_santuario},
                  "M":{"posicion":[[8,36]],"abierto":[False,False],"cierre":f.cofre_cerrar_shield,"funcion":f.cofre}, #-Falta la funcion de cerrar los cofres
                  "E":{"posicion":[[[4,13],[4,14]],[[3,51],[3,52]]],"vidas":[5,5],"funcion":f.enemigos}}

objetos_necluda = {" ":{"funciones":f.cesped},
                  "F":{"posicion":[7,6],"visibilidad":visibilidad_zorro,"funcion":f.zorro}, 
                  "C":{"posicion":[3,19],"funcion":f.cocinar},
                  "T":{"lista":[[6,15],[7,14],[8,15],[2,37],[2,38],[3,36],[3,35]],"vida":[4,4,4,4,4,4,4],"contador":[0,0,0,0,0,0,0],"funcion":f.arbol},
                  "~":{"posicion":[[8,1],[8,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[10,9],[10,10],
                                   [10,11],[10,12],[3,57],[3,56],[3,55],[3,54],[3,53],[4,52],[4,51],
                                   [4,50],[4,49],[5,51],[7,50],[7,49],[7,48],[8,51],[9,50],[9,49],
                                   [9,48],[9,47],[9,46],[9,45],[10,44],[10,43],[10,42],[10,41],[10,40]],"pesca":pesca,"funcion":f.agua},
                  "S5":{"posicion":[[6,50],[6,51]],"puerta":False,"funcion":f.abrir_santuario},
                  "S6":{"posicion":[[9,33],[9,34]],"puerta":False,"funcion":f.abrir_santuario},
                  "M":{"posicion":[[1,22],[9,23],[2,51]],"abierto":[False,False,False],"cierre":f.cofre_cerrar_shield,"funcion":f.cofre}, #-Falta la funcion de cerrar los cofres
                  "E":{"posicion":[[[2,10],[2,11]],[[6,38],[6,39]]],"vidas":[5,5],"funcion":f.enemigos}}

objetos_hyrule = {" ":{"funciones":f.cesped},
                  "F":{"posicion":[9,50],"visibilidad":visibilidad_zorro,"funcion":f.zorro}, 
                  "C":{"posicion":[3,17],"funcion":f.cocinar},
                  "T":{"lista":[[4,6],[8,46],[9,44]],"vida":[4,4,4],"contador":[0,0,0],"funcion":f.arbol},
                  "~":{"posicion":[[1,37],[2,37],[2,38],[2,39],[2,40],[2,41],[2,42],[3,43],[3,44],[3,45],
                                   [3,46],[3,47],[3,48],[2,49],[3,52],[3,53],[3,54],[4,55],[4,56],[4,57]],"pesca":pesca,"funcion":f.agua},
                  "S0":{"posicion":[[6,42],[6,43]],"puerta":False,"funcion":f.abrir_santuario},
                  "S1":{"posicion":[[10,29],[10,30]],"puerta":False,"funcion":f.abrir_santuario},
                  "M":{"posicion":[[9,46]],"abierto":[False],"cierre":f.cofre_cerrar_sword,"funcion":f.cofre}, #-Falta la funcion de cerrar los cofres
                  "E":{"posicion":[[[9,21],[9,22]],[[5,36],[5,35]]],"vidas":[5,5],"funcion":f.enemigos}}
























