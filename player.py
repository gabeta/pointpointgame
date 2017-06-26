########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 17/05/2017
# Module           : Joueur
#
########################################################

class Player(object):

    def __init__(self,color=''):
        self.color = color
        self.score = 0

    def getColor(self):
        return self.color

    def getScore(self):
        return self.score

    def setScore(self):
        self.score = self.score + 1
