import funciones.funciones as f


#Atributos jugador

jugador = {"nombre": "" ,"posicion" : [3,9], "arma_actual": " ", "escudo_actual" : " ", "vidas_max": 3, "vidas" : 3 }

inventarioArmas = {"Wood Shield998" :{"nombre" :"Arma", "usos": 4}, "Wood Shield98" :{"nombre" :"Arma", "usos": 4}}
inventarioComida = {"Vegetables" : 0, "Fish" : 0, "Meat" : 0, "Salads" : 0, "Pescatarian" : 0, "Roasted" : 0 }
dict_tipos = {"Shield" : {"total": 0}, "Wood Shield" : {"total": 0}, "Sword" : {"total": 0}, "Wood Swort" : {"total": 0}, "Vegetables" :{"total": 0}, "Fish" :{"total": 0}, "Meat" :{"total": 0}, "Salads" :{"total": 0}, "Pescatarian" : {"total": 0}, "Roasted": {"total": 0} }

select = "show inventory main"

#Localizaciones y datos
localitzacions = {
    "death" : [["*"," ","D","e","a","t","h"," ","M","o","u","n","t","a","i","n"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*", " ", "*"],
        ["*"," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","F"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","~","~"," "," ","S","2","?"," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," ","*"],
        ["*"," ","~","~","~"," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","O","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," ","O","O"," "," "," "," ","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," ","~","~","~"," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," ","M"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","X"," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","3","?"," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"]], 
        
        "mapa_inicio" : [["*"," ","M","a","p"," "," ","*","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
        ["*"," "," ","H","y","r","u","l","e"," "," "," "," "," "," "," ","S","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","D","e","a","t","h"," ","m","o","u","n","t","a","i","n"," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","2","?"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," ","S","1","?"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","3","?"," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","C","a","s","t","l","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","0"," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","4"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","5"," "," ","*"],
        ["*"," "," ","G","e","r","u","d","o"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","6","?"," "," "," "," "," "," ","N","e","c","l","u","d","a"," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]],

        "hyrule" : [["*"," ","H","y","r","u","l","e"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","O","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","~","O","O","O","O","~","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"," "," "," ","~","~","~","~","~","~","*"],
        ["*"," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","*"],
        ["*"," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","9"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","0"," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," ","E","1"," "," "," "," "," "," "," "," ","S","1","?"," "," "," "," "," "," "," "," "," "," "," "," ","T"," ","M"," "," "," ","F"," "," "," "," "," ","*"],
        ["*","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"]],

        "gerudo" : [["*"," ","G","e","r","u","d","o"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
          ["*", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", "O", "O", "O", "O", "O", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", "4", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "*"],
          ["*", " ", " ", "E", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "E", "2", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", "A", "A", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", "T", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", "A", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "*"],
          ["*", " ", "X", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "*"]],

        "necluda" : [["*"," ","N","e","c","l","u","d","a"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
          ["*", " ", "X", " ", " ", " ", " ", " ", " ", " ", "E", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", "*"],
          ["*", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "*"],
          ["*", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "E", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", "5", "~", "~", "~", "~", "~", "*"],
          ["*", " ", " ", " ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", "6", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"]
          ],

        "castle" : [["* ", "Castle  ", "* "*25],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "G", "a", "n", "o", "n", " ", "♥", "♥", "♥", "♥", "♥", "♥", "♥", "♥", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", "-", "-", " ", "O", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "/", " ", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", ">", " ", " ", "v", "-", "v", "-", "v", "-", "v", " ", " ", " ", "|", ">", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ",", " ", " ", " ", ",", " ", " ", "/", "_", "\\", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", "/", "_", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "\\", "_", "/", "|", " ", " ", "|", " ", "|", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "(", "q", " ", "p", ")", ",", "-", "|", " ", "|", " ", "|", " ", "|", " ", "_", " ", "|", " ", "|", " ", "|", " ", "|", "'", "-", ".", "_", " ", " ", "|", "\\", " ", " ", " ", " ", "*"],
          ["*", "O", "T", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\\", "_", "/", "_", "(", "/", "|", " ", "|", " ", " ", " ", " ", "|", "#", "|", " ", " ", " ", " ", "|", " ", "|", " ", ")", " ", " ", "'", "-", "/", "/", " ", " ", " ", " ", "*"],
          ["*", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "*"]
          ],

        
        "castle_win" : [["* ", "Castle  ", "* "*25],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", "-", "-", " ", "O", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "/", " ", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", ">", " ", " ", "v", "-", "v", "-", "v", "-", "v", " ", " ", " ", "|", ">", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "/", "_", "\\", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", "/", "_", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", "|", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", "|", " ", "|", " ", "|", " ", "_", " ", "|", " ", "|", " ", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", "O", "T", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", "|", "#", "|", " ", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "*"],
          ]
}


dades = { "death" : {"arboles" : [(8,20), (9,19), (10,19)], "position_death" : (9,2) },
         "hyrule" : {"position" : (8,11)},
         "gerudo" : {"position" : (9,2)},
         "necluda" : {"position" : (1,2)},
         "castle" : {"position" : (9,3)}
}


frases_ganon = ["Ganon is powerful, are you sure you can defeat him?", "Ganon's strength is supernatural, Zelda fought with bravery.", "To Ganon, you are like a fly, find a weak spot and attack.", "Ganon will not surrender easily.", "Ganon has fought great battles, is an expert fighter.", "Link, transform your fears into strengths.", "Keep it up, Link, Ganon can't hold out much longer.", "Link, history repeats itself, Ganon can be defeated.", "Think of all the warriors who have tried before.", "You fight for the weaker ones, Link, persevere."]


mapa_anterior = ""


#mapaActual = f.obtenerMapa(localitzacions["death"], jugador["posicion"])
diccionarioMenuPrincipal = {
    
  "principal1" : [["* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                  &&         *"],
              ["*                                                                  &&         *"],
              ["*                                                               ##OOO         *"],
              ["*                                                              ###OOOO        *"],
              ["*  Zelda, Breath of the Wild                                   ###OOO \\       *"],
              ["*                                                                |@@@| \\      *"],
              ["*                                                                |   |  \\     *"],
              ["*                                                                =   ==       *"],
              ["*                                                             %%%%%%%%%%%%    *"],
              ["*                                                          %%%%%%%%%%%%%%%    *"],
              ["* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *"]],

  "principal2" : [["* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                  &&         *"],
              ["*                                                                 oo &        *"],
              ["*                                                         $       -- &##      *"],
              ["*                                                         $$     <<OO####     *"],
              ["*  Zelda, Breath of the Wild                               $$  //OOO####      *"],
              ["*                                                           $$// OO#####      *"],
              ["*                                                            **   OOO###      *"],
              ["*                                                             &   @@@@\\       *"],
              ["*                                                                 Q  Q        *"],
              ["*                                                                 Q  Q        *"],
              ["* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *"]],

  "principal3" : [["* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
                ["*                                                                  &&         *"],
                ["*                                                                 ####        *"],
                ["*                                                                \" || \"       *"],
                ["*                                                             @@@@@@@@@@@@    *"],
                ["*  Zelda, Breath of the Wild                                 @     ||@@@      *"],
                ["*                                                                  |@@@       *"],
                ["*                                                                 @@@         *"],
                ["*                                                               @@@||     @   *"],
                ["*                                                            @@@@@@@@@@@@@    *"],
                ["*                                                                  ||         *"],
                ["* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *"]],

  "help_main" : [["* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
             ["*                                                                             *"],
             ["*                                                                             *"],
             ["*       Type 'continue' to continue a saved game                              *"],
             ["*       Type 'new game' to start a new game                                   *"],
             ["*       Type 'about' to see information about the game                        *"],
             ["*       Type 'exit' to exit the game                                          *"],
             ["*                                                                             *"],
             ["*                                                                             *"],
             ["*       Type 'back' now to go back to the 'Main menu'                         *"],
             ["*                                                                             *"],
             ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],

  "new_game" : [["* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
            ["*                                                                             *"],
            ["*                                                                             *"],
            ["*                                                                             *"],
            ["*                                                                             *"],
            ["*       Set your name ?                                                       *"],
            ["*                                                                             *"],
            ["*                                                                             *"],
            ["*                                                                             *"],
            ["*       Type 'back' now to go back to the 'Main menu'                         *"],
            ["*                                                                             *"],
            ["* Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],


  "about_main" : [["* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                             *"],
              ["*       Game developed by 'Team 4,                                            *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*             Jorge Cortés                                                    *"],
              ["*             Luciano Poyanco                                                 *"],
              ["*             Erik Rojas                                                      *"],
              ["*                                                                             *"],
              ["*       Type 'back' now to go back to the 'Main menu'                         *"],
              ["*                                                                             *"],
              ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],
  

  "help_new_game" : [["* Help, new game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
                 ["*                                                                             *"],
                 ["*                                                                             *"],
                 ["*       When asked, type your name and press enter                            *"],
                 ["*       if 'Link' is fine for you, just press enter                           *"],
                 ["*                                                                             *"],
                 ["*       Name must be between 3 and 10 characters long and only                *"],
                 ["*       letters, numbers and spaces are allowed                               *"],
                 ["*                                                                             *"],
                 ["*       Type 'back' now to go back to the 'Set your name'                     *"],
                 ["*                                                                             *"],
                 ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],

  "help_saved_games" : [["* Help, saved game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
                    ["*                                                                             *"],
                    ["*                                                                             *"],
                    ["*       Type 'play X' to continue playing the game 'X'                        *"],
                    ["*       Type 'erase X' to erase the game 'X'                                  *"],
                    ["*       Type 'back' now to go back to the main menu                           *"],
                    ["*                                                                             *"],
                    ["*                                                                             *"],
                    ["*                                                                             *"],
                    ["*       Type 'back' now to go back to the 'Main menu'                         *"],
                    ["*                                                                             *"],
                    ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],

  "legend" : [["* Legend  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
          ["*    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah  *"],
          ["*    tribe. The Sheikah were a tribe of warriors who protected the Triforce,  *"],
          ["*    a sacred relic that granted wishes.                                      *"],
          ["*                                                                             *"],
          ["*    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began   *"],
          ["*    to rule Hyrule with an iron fist.                                        *"],
          ["*                                                                             *"],
          ["*    The princess, with the help of a heroic young man, managed to defeat     *"],
          ["*    Ganondorf and recover the Triforce.                                      *"],
          ["*                                                                             *"],
          ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],

  "plot" : [["* Plot  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["*  Now history is repeating itself, and Princess Zelda has been captured by   *"],
        ["*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.    *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["*  But a young man named {} has just awakened and".ljust(78)+"*"],
        ["*  must reclaim the Guardians to defeat Ganon and save Hyrule.                *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],

  "help_inventory" : [["* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
                  ["*       Type 'show inventory main' to show the main inventory                 *"],
                  ["*            (main, weapons, Food)                                            *"],
                  ["*       Type 'eat X' to eat X, where X is a Food item                         *"],
                  ["*       Type 'Cook X' to Cook X, where X is a Food item                       *"],
                  ["*       Type 'equip X' to equip X, where X is a weapon                        *"],
                  ["*       Type 'unequip X' to unequip X, where X is a weapon                    *"],
                  ["*       Type 'back' now to go back to the 'Game'                              *"],
                  ["*                                                                             *"],
                  ["*                                                                             *"],
                  ["*                                                                             *"],
                  ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],

  "zelda_saved" : [["* Zelda saved * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
               ["*                                                                             *"],
               ["*                                                                             *"],
               ["*                                                                             *"],
               ["*                                                                             *"],
               ["*    Congratulations, Link has saved Princess Zelda.                          *"],
               ["*    Thanks for playing!                                                      *"],
               ["*                                                                             *"],
               ["*                                                                             *"],
               ["*                                                                             *"],
               ["*                                                                             *"],
               ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]],
  

  "link_death" : [["* Link death  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*    Game Over.                                                               *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["*                                                                             *"],
              ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]
}

texto_prompt = []


pesca = False #Sirve para saber si ya has conseguido u pez o no
#agua = {"posicion":posicion,"mapa":mapa,"pesca":pesca}

visibilidad_zorro = False #Saber si el zorro lo ves o no
#zorro = {"posicion":posicion,"mapa":mapa,"visibilidad":visibilidad_zorro,"forma":"F"}

puerta_santuario = False #Saber si el santuario esta abierto o no
#santuario = {"posicion":posicion,"mapa":mapa,"puerta":puerta_santuario,"forma":"S1"}

cofre_abierto = False
#cofre = {"posicion":posicion,"map":map,"cofre":cofre_abierto,"forma":"M"}

win = False # Saber cuando has ganado, para que cuando entres a castle no salga Ganon

ganon = {"vida":9}


