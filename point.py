########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro
# Compagnie        : EnighmaLab
# Date de création : 17/05/2017
#
########################################################

from tkinter import *
from math import *

from player import Player

begin = False

P1 = Player('blue')
P2 = Player('red')
current_p = P1

space = 30
TWdHg = 540

point_dico = {}

#Crétation de la plateform de jeu
def create_plateform():

    if(begin is False):
        d = 0
        info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
        info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

        while d < TWdHg :
            can.create_line(d, 0, d, TWdHg, fill ='cyan') #Création de la ligne horizontale avec un espacement de 30
            can.create_line(0, d, TWdHg, d, fill ='cyan') #Création de la ligne verticale avec un espacement de 30
            d = d + 30

        global begin
        begin = True

#Vérifie si l'utilisateur est dans la zone de jeu
def overFlow(x,y):
    if(y <= (TWdHg - space)) & (y >= space):
        if(x <= (TWdHg - space)) & (x >= space):
            return True
        else:
            return False
    else:
        return False

#Verifie la porté du point de l'utilisateur avec une marge de 2
def checkRayon(x,y):
    Rx = x % space
    Ry = y % space

    if(Ry == 0) | (Ry == 1) | (Ry == 2) | (Ry == (space - 2)) | (Ry == (space - 1)):
        if(Rx == 0) | (Rx == 1) | (Rx == 2) | (Rx == (space - 2)) | (Rx == (space - 1)):
            return True
        else:
            return False
    else:
        return False

#Arrondir à la au multiple le plus proche de 30
def rang_twenthy(val):
    R = val % space

    if (R == 1):
        val = val - 1
    elif (R == (space - 1)):
        val = val +1
    elif (R == 2):
        val = val - 2
    elif (R == (space - 2)):
        val = val + 2

    return val

#Vérification d'un carré en haut à gauche
def top_left_pivot(x,y):
    x2 = x - space
    y2 = y - space
    P = str(str(x)+'_'+str(y))
    P2 = str(str(x)+'_'+str(y2))
    P3 = str(str(x2)+'_'+str(y))
    P4 = str(str(x2)+'_'+str(y2))

    if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
        if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
            return True

#Vérification d'un carré en haut à droite
def top_right_pivot(x,y):
    x2 = x + space
    y2 = y - space
    P = str(str(x)+'_'+str(y))
    P2 = str(str(x)+'_'+str(y2))
    P3 = str(str(x2)+'_'+str(y2))
    P4 = str(str(x2)+'_'+str(y))

    if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):

        if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):

            return True

#Vérification d'un carré en bas à gauche
def bottom_left_pivot(x,y):
    x2 = x - space
    y2 = y + space

    P = str(str(x)+'_'+str(y))
    P2 = str(str(x2)+'_'+str(y))
    P3 = str(str(x2)+'_'+str(y2))
    P4 = str(str(x)+'_'+str(y2))

    if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
        if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
            return True

#Vérification d'un carré en bas à gauche
def bottom_right_pivot(x,y):
    x2 = x + space
    x3 = x - space
    y2 = y + space

    P = str(str(x)+'_'+str(y))
    P2 = str(str(x)+'_'+str(y2))
    P3 = str(str(x2)+'_'+str(y))
    P4 = str(str(x2)+'_'+str(y2))

    if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
        if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
            return True

#Création du point
def point(event):

    if(begin):

        if(overFlow(event.y,event.x) & checkRayon(event.y,event.x)):

            event.y = rang_twenthy(event.y)
            event.x = rang_twenthy(event.x)
            value = str(str(event.x)+'_'+str(event.y))

            if(value in point_dico):

                chaine.configure(text = "Il y a déjà un point à ce emplacement")

            else:

                r = 5

                #chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
                #    ", Y =" + str(event.y))

                point_dico[value] = current_p.getColor()

                can.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill=current_p.getColor())

                if(top_left_pivot(event.x,event.y)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x-space, event.y-space, event.x, event.y, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(top_right_pivot(event.x,event.y)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x, event.y-space, event.x+space, event.y, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(bottom_left_pivot(event.x,event.y)):

                    if(current_p == P1):
                        P1.setScore()
                    else:
                        P2.setScore()

                    can.create_rectangle(event.x, event.y+space, event.x-space, event.y, fill=current_p.getColor())

                    info.configure(text = "Joueur Bleu  = " + str(P1.getScore()))
                    info2.configure(text = "Joueur Rouge = " + str(P2.getScore()))

                    chaine.configure(text = "Jolie point")

                if(bottom_right_pivot(event.x,event.y)):

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

can = Canvas(fen, width =TWdHg, height =TWdHg, bg="light yellow")
can.bind('<Button-1>', point)
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
