########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 26/06/2017
# Module           : Intelligence Articielle
# Numéro IA        : Iris-CP12
# Niveau           : CP1/CP2
#
########################################################

from IA.IrisIA import IrisIA

class IrisCpIA(IrisIA):

    def __init__(self,color):
        IrisIA.__init__(self,color)

    def defense(self):

        defense_dico = self.defenseDico

        for k in defense_dico:
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])
            final_dico = {}
            final_dico['x'] = x
            final_dico['y'] = y

            return final_dico


    def attack(self):
        attack_dico = self.attackDico

    def construire(self):
        pass
