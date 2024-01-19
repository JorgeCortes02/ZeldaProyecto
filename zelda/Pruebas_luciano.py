import funciones.datos as d
import funciones.funciones as f

linia = ""
for i in d.localitzacions["hyrule"]:
    for j in i:
        linia += j
    linia += "\n"
print(linia)
f.abrir_santuario()
f.prompt()
'''print(d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][0][0]][d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][0][1]+2])
d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][0][0]][d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][0][1]+2] = " "
print(d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][0][0]][d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][0][1]+2])'''
linia = ""
for i in d.localitzacions["hyrule"]:
    for j in i:
        linia += j
    linia += "\n"
print(linia)
f.prompt()
    
'''print(d.localitzacions["hyrule"][5][9])'''

'''for j in range(len(d.objetos["objetos_hyrule"]["T"]["lista"])):
    print(j)'''

for i in range(len(d.dades[d.jugador["mapa"]]["T"]["lista"])):
    print(i)

'''f.movimientoCercano("Go to S0")
f.obtenerMapa(d.localitzacions["hyrule"],d.jugador["posicion"])
f.prompt()'''