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

from Environnement.pivot import Pivot
from Environnement.terrain import Terrain

class IrisIA(object):

    def __init__(self,color):
        self.ownDico = {}
        self.otherDico = {}
        self.color = color
        self.score = 0

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
