import funciones.funciones as f

mapa_inicio = [["*"," ","M","a","p"," "," ","*","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
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
        ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]]


hyrule = [["*"," ","H","y","r","u","l","e"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","O","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","~","O","O","O","O","~","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"," "," "," ","~","~","~","~","~","~","*"],
        ["*"," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","*"],
        ["*"," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","9"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","0"," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," ","!"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," ","E","1"," "," "," "," "," "," "," "," ","S","1","?"," "," "," "," "," "," "," "," "," "," "," "," ","T"," ","M"," "," "," ","F"," "," "," "," "," ","*"],
        ["*","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"]]

position_hyrule = [8,11]

gerudo = [["*"," ","G","e","r","u","d","o"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
          ["*", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", "O", "O", "O", "O", "O", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", "4", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "*"],
          ["*", " ", " ", "E", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "E", "2", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", "A", "A", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", "T", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", "A", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "*"],
          ["*", " ", "!", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", " ", "A", "A", "A", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "*"]]

position_gerudo = [9,2]

necluda = [["*"," ","N","e","c","l","u","d","a"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
          ["*", " ", "!", " ", " ", " ", " ", " ", " ", " ", "E", "1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", "*"],
          ["*", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "*"],
          ["*", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "E", "2", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", "5", "~", "~", "~", "~", "~", "*"],
          ["*", " ", " ", " ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " ", "T", "9", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "T", "6", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", "6", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"],
          ["*", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "*"]
          ]

position_necluda = [1,2]

death = [["*"," ","D","e","a","t","h"," ","M","o","u","n","t","a","i","n"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*", " ", "*"],
        ["*"," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","F"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","~","~"," "," ","S","2","?"," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," ","*"],
        ["*"," ","~","~","~"," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","O","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," ","O","O"," "," "," "," ","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," ","~","~","~"," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," ","M"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*"," ","!"," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","3","?"," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
        ["*" * 21]]

position_death = [9,2]

castle = [["* ", "Castle  ", "* "*25],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "G", "a", "n", "o", "n", " ", "♥", "♥", "♥", "♥", "♥", "♥", "♥", "♥", " ", " ", "*"],
          ["*", " ", " ", " ", " ", "-", "-", " ", "O", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "/", " ", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", ">", " ", " ", "v", "-", "v", "-", "v", "-", "v", " ", " ", " ", "|", ">", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ",", " ", " ", " ", ",", " ", " ", "/", "_", "\\", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", "/", "_", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "\\", "_", "/", "|", " ", " ", "|", " ", "|", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "(", "q", " ", "p", ")", ",", "-", "|", " ", "|", " ", "|", " ", "|", " ", "_", " ", "|", " ", "|", " ", "|", " ", "|", "'", "-", ".", "_", " ", " ", "|", "\\", " ", " ", " ", " ", "*"],
          ["*", "O", "T", "!", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\\", "_", "/", "_", "(", "/", "|", " ", "|", " ", " ", " ", " ", "|", "#", "|", " ", " ", " ", " ", "|", " ", "|", " ", ")", " ", " ", "'", "-", "/", "/", " ", " ", " ", " ", "*"],
          ["*", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "*"],
          ["* " * 30]]

position_castle = [9,3]

castle_win = [["* ", "Castle  ", "* "*25],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", "-", "-", " ", "O", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", "/", " ", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", ">", " ", " ", "v", "-", "v", "-", "v", "-", "v", " ", " ", " ", "|", ">", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "/", "_", "\\", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", "/", "_", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", "|", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", "|", " ", "|", " ", "|", " ", "_", " ", "|", " ", "|", " ", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", "O", "T", "!", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", "|", "#", "|", " ", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
          ["*", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "*"],
          ["* " * 30]]

position_castle_win = [9,3]

mapas_diccionario = {"hyrule":{"mapa":hyrule, "posicion": position_hyrule},"gerudo":{"mapa":gerudo, "posicion":position_gerudo},"necluda":{"mapa":necluda, "posicion": position_necluda},"death":{"mapa":death, "posicion":position_death},"castle":{"mapa":castle,"posicion":position_castle},"castle_win":{"mapa":castle_win,"posicion":position_castle_win}} #Diccionario de los mapas y sus posiciones

position_castle_win = [9,3]

vidas = 3
vidas_max = 10
arma_actual = ""
escudo_actual = ""

inventario1 = f.mostrarInventario()



inventarioArmas = {}
inventarioComida = {}



principal1 = [["* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                  &&         *"],
              ["*                                                                  &&         *"],
              ["*                                                               ##OOO         *"],
              ["*                                                              ###OOOO        *"],
              ["*  Zelda, Breath of the Wild                                   ###OOO \\      *"],
              ["*                                                                |@@@| \\     *"],
              ["*                                                                |   |  \\    *"],
              ["*                                                                =   ==       *"],
              ["*                                                             %%%%%%%%%%%%    *"],
              ["*                                                          %%%%%%%%%%%%%%%    *"],
              ["* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *"]]

principal2 = [["* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                  &&         *"],
              ["*                                                                 oo &        *"],
              ["*                                                         $       -- &##      *"],
              ["*                                                         $$     <<OO####     *"],
              ["*  Zelda, Breath of the Wild                               $$  //OOO####      *"],
              ["*                                                           $$// OO#####      *"],
              ["*                                                            **   OOO###      *"],
              ["*                                                             &   @@@@\\      *"],
              ["*                                                                 Q  Q        *"],
              ["*                                                                 Q  Q        *"],
              ["* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *"]]

principal3 = [["* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
              ["*                                                                  &&         *"],
              ["*                                                                 ####        *"],
              ["*                                                                \" || \"     *"],
              ["*                                                             @@@@@@@@@@@@    *"],
              ["*  Zelda, Breath of the Wild                                 @     ||@@@      *"],
              ["*                                                                  |@@@       *"],
              ["*                                                                 @@@         *"],
              ["*                                                               @@@||     @   *"],
              ["*                                                            @@@@@@@@@@@@@    *"],
              ["*                                                                  ||         *"],
              ["* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *"]]


help_main = [["* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
             ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

new_game = [["* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
            ["* Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

about_main = [["* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
              ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

help_new_game = [["* Help, new game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
                 ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

help_saved_games = [["* Help, saved game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
                    ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

legend = [["* Legend  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
          ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

name = "link" #funcion pàra que no se queje plot

plot = [["* Plot  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["*  Now history is repeating itself, and Princess Zelda has been captured by   *"],
        ["*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.    *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        [f"*  But a young man named {name} has just awakened and".ljust(78)+"*"],
        ["*  must reclaim the Guardians to defeat Ganon and save Hyrule.                *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

help_inventory = [["* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
                  ["* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

zelda_saved = [["* Zelda saved * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
               ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],]

link_death = [["* Link death  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
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
              ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],]

texto_prompt = ["","","","","","","","",""]

#---------------Inventario y pesonaje----------------------
espada = True
mapa = hyrule
vida_espada_madera = 5
vida_escudo_madera = 5
vida_enemigo = 5
nombre = "Link"
posicion_enemigo = [0,0]
#enemigo ={"posicion"=posicion_enemigo,"mapa":mapa,"vida":vida_enemigo}
#-Esto solo lo hecho porque no se donde esta los usos de las cosas ya luego lo modificamos

#---------------Interaciones con los objetos del mapa----------------------

vida_arbol = 4 
#arbol = {"posicion":posicion,"mapa":mapa,"vida":vida_arbol}

pesca = False #Sirve para saber si ya has conseguido u pez o no
#agua = {"posicion":posicion,"mapa":mapa,"pesca":pesca}

visibilidad_zorro = False #Saber si el zorro lo ves o no
#zorro = {"posicion":posicion,"mapa":mapa,"visibilidad":visibilidad_zorro}

puerta_santuario = False #Saber si el santuario esta abierto o no
#santuario = {"posicion":posicion,"mapa":mapa,"puerta":puerta_santuario}

cofre_abierto = False
#cofre = {"posicion":posicion,"map":map,"cofre":cofre_abierto}