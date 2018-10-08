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

import Interface

#Corps principal du programme
P1 = Player('blue')
P2 = Player('red')

jeu = Interface.Jeu( P1, P2 )
jeu.run()
