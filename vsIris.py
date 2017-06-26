########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 26/06/2017
# Scène            : Player vs Iris
#
########################################################

from tkinter import *

from Environnement.player import Player
from IA.irisCpIA import IrisCpIA
from Environnement.pivot import Pivot


begin = False

#Paramètre Joueur
P1 = Player('blue')
P2 = IrisCpIA('red')
current_p = P1

#Classe qui gère les pivot
Pivot = Pivot()

#Paramètre Terrain
space = 30
Theight = 540
Twidth = 630

#Dictionnaire des points
point_dico = {}

#Crétation de la plateform de jeu
def create_plateform():

    if(begin is False):
        d = 0
        #info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        #info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        horizontalLine()
        verticalLine()

        global begin
        begin = True

#Création de la ligne horizontale avec un espacement de 30
def horizontalLine():
    d = 0
    while d < Twidth :
        can.create_line(d, 0, d, Theight, fill ='cyan') #Création de la ligne horizontale avec un espacement de 30
        #can.create_line(0, d, TWdHg, d, fill ='cyan') #Création de la ligne verticale avec un espacement de 30
        d = d + space

#Création de la ligne verticale avec un espacement de 30
def verticalLine():
    d = 0
    while d < Theight :
        #can.create_line(d, 0, d, Theight, fill ='cyan') #Création de la ligne horizontale avec un espacement de 30
        can.create_line(0, d, Twidth, d, fill ='cyan') #Création de la ligne verticale avec un espacement de 30
        d = d + space


#Corps principale du programme
fen = Tk()
fen.title("Point point Game By EnighmaLab")

can = Canvas(fen, width =Twidth, height =Theight, bg="light yellow")
#can.bind('<Button-1>', point)
can.pack()

b1 = Button(fen, text='Commencer', command=create_plateform)
b1.pack()

role = Label(fen)
role.pack()

load = Label(fen)
load.pack()

chaine = Label(fen)
chaine.pack()

info = Label(fen)
info.pack()

info2 = Label(fen)
info2.pack()

fen.mainloop()
