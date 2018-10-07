########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Pseudo           : @lChiMi5tE_d0t_toRr€nt
# Compagnie        : EnighmaLab
# Date de création : 26/06/2017
# Scène            : Player vs Iris-CP12
# Niveau de l'IA   : Elève CP1/CP2
#
########################################################

from tkinter import *
from random import randrange

from Environnement.player import Player
from IA.irisCpIA import IrisCpIA

import Interface


#Au tour de l'IA de jouer.
def IAtour( o_jeu ):
    '''o_jeu est un objet Jeu'''

    P2  = o_jeu.current_player
    can = o_jeu.canvas
    point_dico = o_jeu.d_points
    space = o_jeu.space

    if(len(P2.getOwnDico()) == 0):

        #Début du jeu faire un point aléatoire
        point = P2.randPoint(can,point_dico)
        x = point['x']
        y = point['y']

    else:

        #Vérification de l'Etat des lieux
        defense = P2.checkOtherDico(point_dico,space)
        attack = P2.checkOwnDico(point_dico,space)

        if(len(attack)):

            final_dico = P2.attack()
            x = final_dico['x']
            y = final_dico['y']
            o_jeu.dessine_rond( x, y )

        else:
            vue = randrange(1,20) % 2

            if( len(defense) & vue):
                final_dico = P2.defense()
                x = final_dico['x']
                y = final_dico['y']
                o_jeu.dessine_rond( x, y )
            else:
                #Vérification si il y a un possibilité de construire
                P2.checkOnePointDico(point_dico,space)
                P2.checkTwoPointDico(point_dico,space)

                if(P2.canBuild()):
                    if(len(P2.twoPointDico)):
                        point = P2.buildWithTwoPoint()
                    else:
                        point = P2.buildWithOnePoint()

                    x = point['x']
                    y = point['y']
                    o_jeu.dessine_rond( x, y )
                else:
                    point = P2.randPoint(can,point_dico)
                    x = point['x']
                    y = point['y']

    #On vide tous les dictionnaires de l'IA
    P2.clearDico()

    #Enregistrement des coordonnées dans le dictionnaire global.
    coord = str(str(x)+'_'+str(y))
    point_dico[coord] = P2.getColor()

    #Enregistrer les cordonnées de l'IA dans son dico
    P2.setOwnDico(coord)
    P2.updateRandomList(coord)

    #Tentative de faire un carré si possible
    o_jeu.makeCarre(x,y)

    #Donner la main à l'utilisateur
    o_jeu.change_joueur()
# IAtour


#Corps principale du programme
P1 = Player('blue')
P2 = IrisCpIA('red')

jeu = Interface.Jeu( P1, P2, fn_iaTour=IAtour )
jeu.run()
