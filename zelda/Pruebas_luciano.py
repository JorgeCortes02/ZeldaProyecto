import funciones.datos as d
import funciones.funciones as f

linia = ""
for i in d.localitzacions["castle"]:
    for j in i:
        linia += j
    linia += "\n"
print(linia)
f.vida_ganon()
linia = ""
for i in d.localitzacions["castle"]:
    for j in i:
        linia += j
    linia += "\n"
print(linia)

