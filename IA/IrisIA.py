########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 26/06/2017
# Module           : Intelligence Articielle
# Nom              : Iris
#
########################################################

from random import randrange

import time

from Environnement.pivot import Pivot
from Environnement.terrain import Terrain

class IrisIA(object):

    ownDico = {}
    otherDico = {}
    score = 0

    def __init__(self,color):
        self.color = color

    def checkIsFavorablePosition(self,dico):
        #Parcourt le dictionnaire
        for k in dico:
            #Exploder le K par les enderscorts
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])
            top = Pivot.get_point_top(x,y,Terrain.getSpace(),dico)

            #Vérifie si il y a une possibilité de marquer
            pass

    def checkOwnDico(self):
        if self.checkIsFavorablePosition():
            pass

    def checkOtherDico(self):
        if self.checkIsFavorablePosition():
            pass

    def randPoint(self,can,point_dico):

        r = 5
        xMod = 1
        yMod = 1
        boucle = True

        while boucle:


            while xMod:
                x = randrange(30, (630 - 30))
                xMod = x % 30

            while yMod:
                y = randrange(30, (540 - 30))
                yMod = y % 30

            point = str(str(x)+'_'+str(y))

            if point in point_dico:
                time.sleep(2)
                boucle = True
            else:
                boucle = False

        can.create_oval(x-r, y-r, x+r, y+r, fill=self.getColor())

        point = {}
        point['x'] = x
        point['y'] = y

        return point

    #Dictionnaire de point de l'IA. ce Dictionnaire permettra de connaitre tous les emplacements des points de l'IA.
    def getOwnDico(self):
        return self.ownDico

    #Modification du dictionnaire de l'IA
    def setOwnDico(self,coord):
        self.ownDico[coord] = self.getColor()

    #Dictionnaire de point du joueur. ce Dictionnaire permettra de connaitre tous les emplacements des points du joueur.
    def getOtherDico(self):
        return self.otherDico

    #Modification du dictionnaire du joueur
    def setOtherDico(self,coord,color):
        self.ownDico[coord] = color

    #Score de l'IA
    def getScore(self):
        return self.score

    #Modification du score de l'IA
    def setScore(self):
        return self.score + 1

    def getColor(self):
        return self.color
