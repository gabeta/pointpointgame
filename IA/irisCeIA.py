########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 05/07/2017
# Module           : Intelligence Articielle
# Numéro IA        : Iris-CE12
# Niveau           : CE1/CE2
#
########################################################

from IA.IrisIA import IrisIA

class IrisCpIA(IrisIA):

    def __init__(self,color):
        IrisIA.__init__(self,color)

    def defense(self):

        defense_dico = self.defenseDico

        #Ranger le ditionnaire dans l'ordre decroissant en fonction de clés

        #Récupère le premier élement du dictionnaire

        #Création du dictionnaire final
        k = '30_30'
        array = k.split('_')
        x = int(array[0])
        y = int(array[1])
        final_dico = {}
        final_dico['x'] = x
        final_dico['y'] = y

        #Vidage du dictionnaire de defense

        #retour du dictionnaire final
        return final_dico


    def attack(self):
        attack_dico = self.attackDico

    def construire(self):
        pass
