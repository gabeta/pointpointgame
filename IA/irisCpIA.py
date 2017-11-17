########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Pseudo           : @lChiMi5tE_d0t_toRr€nt
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
        return self.final_point(defense_dico)

    def attack(self):
        attack_dico = self.attackDico
        return self.final_point(attack_dico)

    def final_point(self,dico):
        #Renvoie du premier point d'une manière aléatoire
        for k in dico:
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])
            final_dico = {}
            final_dico['x'] = x
            final_dico['y'] = y

            return final_dico

    def buildWithOnePoint(self):
        onepointdico = self.onePointDico
        return self.final_point(onepointdico)

    def buildWithTwoPoint(self):
        twopointdico = self.twoPointDico
        return self.final_point(twopointdico)
