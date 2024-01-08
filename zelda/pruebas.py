hyrule = ""
texto = ""
contador = 0
for m in marco:
        if contador == 0 or contador == 2:
            hyrule += m+marco2[0]+"\n"
            contador += 1
        else:
            for linia in mapa:
                hyrule += m[0]
                for zona in linia:
                    hyrule += zona
                hyrule += m[1]+" "+texto.center(17)+" "+marco2[1]+"\n"
            contador += 1
print(hyrule)




