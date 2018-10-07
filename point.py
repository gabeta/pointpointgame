########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Pseudo           : @lChiMi5tE_d0t_toRr€nt
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

    global begin

    if(begin is False):
        d = 0
        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        terrain.horizontalLine()
        terrain.verticalLine()

        begin = True

#Marquer un point en faisant un carré
def makeCarre(x,y):

    if(Pivot.top_left(x,y,space,point_dico)):

        if(current_p == P1):
            P1.setScore()
        else:
            P2.setScore()

        can.create_rectangle(x-space, y-space, x, y, fill=current_p.getColor())

        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        chaine.configure(text = "Jolie point")

    if(Pivot.top_right(x,y,space,point_dico)):

        if(current_p == P1):
            P1.setScore()
        else:
            P2.setScore()

        can.create_rectangle(x, y-space, x+space, y, fill=current_p.getColor())

        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        chaine.configure(text = "Jolie point")

    if(Pivot.bottom_left(x,y,space,point_dico)):

        if(current_p == P1):
            P1.setScore()
        else:
            P2.setScore()

        can.create_rectangle(x, y+space, x-space, y, fill=current_p.getColor())

        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        chaine.configure(text = "Jolie point")

    if(Pivot.bottom_right(x,y,space,point_dico)):

        if(current_p == P1):
            P1.setScore()
        else:
            P2.setScore()

        can.create_rectangle(x, y, x+space, y+space, fill=current_p.getColor())

        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        chaine.configure(text = "Jolie point")

#Création du point
def point(event):

    global current_p

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

                makeCarre(event.x,event.y)

                if(current_p == P1):
                    current_p = P2
                    next_color = "rouge"
                else:
                    current_p = P1
                    next_color = "bleu"

                chaine.configure(text = "")
                role.configure(text="Veuillez patienter!! Au tour du joueur "+next_color+" de jouer. ")



#Corps principale du programme
fen = Tk()
fen.title("Point point Game By EnighmaLab")

can = Canvas(fen, width =Twidth, height =Theight, bg="light yellow",borderwidth=2,relief=SOLID)
can.bind('<Button-1>', point)
can.grid(row = 0, rowspan = 45)

terrain = Terrain(Twidth,Theight,space,can)

b1 = Button(fen,bg='#FAF8E9',relief=GROOVE, text='Commencer',width=15, command=create_plateform)
b1.grid(row = 0,column = 1)

b2 = Button(fen,bg='#FAF8E9',relief=GROOVE, text='Instructtion',width=15, command=create_plateform)
b2.grid(row = 1,column = 1)

info = Label(fen,bg='#6699CC', text='Joueur Bleu',width=15,pady=5,relief=GROOVE)
info.grid(row = 13,column = 1)

info2 = Label(fen,bg='#FF6666', text='Joueur Rouge',width=15,pady=5,relief=GROOVE)
info2.grid(row = 15,column = 1)

b3 = Button(fen,bg='#FAF8E9',relief=GROOVE, text='Quitter',width=15, command=fen.quit)
b3.grid(row = 44,column = 1)

role = Label(fen)
role.grid(row = 44)

chaine = Label(fen,fg='red')
chaine.grid(row = 45)



fen.mainloop()
