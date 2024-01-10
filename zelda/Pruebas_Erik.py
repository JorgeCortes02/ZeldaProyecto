import funciones.funciones as f

#menu_inicial = f.menu_random()
#f.menu_principal(menu_inicial)

diccio = {"vegetable123456":{"nombre":"vegetable"}, "vegetable654321":{"nombre":"vegetable"}, "vegetable654328":{"nombre":"vegetable"}, "vegetable123457":{"nombre":"vegetable"}, "fish654321":{"nombre":"fish"}, "meat654328":{"nombre":"meat"}}


while True:
    for i in diccio:
        print(diccio[i])
    receta = input("")
    if receta[:4].lower() == "cook":
        f.cocinar(receta, diccio)
    
    else:
        print("Invalid Option")


