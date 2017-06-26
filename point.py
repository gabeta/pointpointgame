########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 17/05/2017
# Scène            : Player vs Player
#
########################################################

from tkinter import *

from Environnement.player import Player
from Environnement.pivot import Pivot
from Environnement.terrain import Terrain


begin = False

#Paramètre Joueur
P1 = Player('blue')
P2 = Player('red')
current_p = P1

#Classe qui gère les pivot(Vérifie que les points de même couleurs forment un carré)
Pivot = Pivot()

#Paramètre du terrain
Twidth = 630
Theight = 540
space = 30

#Dictionnaire des points
point_dico = {}

#Crétation de la plateform de jeu
def create_plateform():


    if(begin is False):
        d = 0
        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        terrain.horizontalLine()
        terrain.verticalLine()

        global begin
        begin = True

#Création du point
def point(event):

    if(begin):

        if(terrain.overFlow(event.y,event.x) & terrain.checkRayon(event.y,event.x)):

            event.y = terrain.rang_twenthy(event.y)
            event.x = terrain.rang_twenthy(event.x)
            value = str(str(event.x)+'_'+str(event.y))

            if(value in point_dico):

                chaine.configure(text = "Il y a déjà un point à ce emplacement")

            else:

                r = 5

                point_dico[value] = current_p.getColor()

                can.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill=current_p.getColor())

                if(Pivot.top_left(event.x,event.y,space,point_dico)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x-space, event.y-space, event.x, event.y, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(Pivot.top_right(event.x,event.y,space,point_dico)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x, event.y-space, event.x+space, event.y, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(Pivot.bottom_left(event.x,event.y,space,point_dico)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x, event.y+space, event.x-space, event.y, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(Pivot.bottom_right(event.x,event.y,space,point_dico)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x, event.y, event.x+space, event.y+space, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(current_p == P1):
                    global current_p
                    current_p = P2
                    next_color = "rouge"
                else:
                    global current_p
                    current_p = P1
                    next_color = "bleu"

                chaine.configure(text = "")
                role.configure(text="Au tour du joueur "+next_color+" de jouer. ")
                load.configure(text ="Veuillez patienter!!")

#Corps principale du programme
fen = Tk()
fen.title("Point point Game By EnighmaLab")

can = Canvas(fen, width =Twidth, height =Theight, bg="light yellow")
can.bind('<Button-1>', point)
can.pack()

terrain = Terrain(Twidth,Theight,space,can)

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
