########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Pseudo           : @lChiMi5tE_d0t_toRr€nt
# Compagnie        : EnighmaLab
# Date de création : 26/06/2017
# Module           : Intelligence Articielle
# Nom              : Iris
#
########################################################

import random
import time

from Environnement.pivot import Pivot

pivot = Pivot()

class IrisIA(object):

    ownDico = {}
    otherDico = {}
    score = 0
    attackDico = {}
    defenseDico = {}
    onePointDico = {}
    twoPointDico = {}
    randomList = []
    randomListX = []
    randomListY = []

#540
#630
    def __init__(self,color):
        self.color = color
        self.makeRandomList()

    def makeRandomList(self):
        x = 30
        while x<630 :
            y = 30
            while y<540 :
                coord = str(str(x)+'_'+str(y))
                self.randomList.append(coord)
                y = y + 30

            x = x + 30


    def updateRandomList(self,coord):
        self.randomList.remove(coord)


    def buildDico(self,dico,point_dico,space,attack):
        #Parcourt le dictionnaire
        for k in dico:
            #Exploder le K par les enderscorts
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])

            top_left = pivot.get_point_top_left(x,y,space,point_dico)
            top_right = pivot.get_point_top_right(x,y,space,point_dico)
            bottom_left = pivot.get_point_bottom_left(x,y,space,point_dico)
            bottom_right = pivot.get_point_bottom_right(x,y,space,point_dico)

            self.makeBatlleDico(top_left,attack)
            self.makeBatlleDico(top_right,attack)
            self.makeBatlleDico(bottom_right,attack)
            self.makeBatlleDico(bottom_left,attack)

    def makeBatlleDico(self,dico,attack):
        if(len(dico)):
            point = str(str(dico['x'])+'_'+str(dico['y']))
            if(attack):
                if point in self.attackDico:
                    self.attackDico[point] = self.attackDico[point] + 1
                else:
                    self.attackDico[point] = 1
            else:
                if point in self.defenseDico:
                    self.defenseDico[point] = self.defenseDico[point] + 1
                else:
                    self.defenseDico[point] = 1

    def checkOwnDico(self,dico,space):
        if(len(self.attackDico) == 0):
            self.buildDico(self.ownDico,dico,space,True)
        return self.attackDico

    def checkOtherDico(self,dico,space):
        if(len(self.defenseDico) == 0):
            self.buildDico(self.otherDico,dico,space,False)
        return self.defenseDico

    def clearDico(self):
        self.attackDico.clear()
        self.defenseDico.clear()
        self.onePointDico.clear()
        self.twoPointDico.clear()

    def checkOnePointDico(self,point_dico,space):
        #Parcourt le dictionnaire
        for k in self.ownDico:
            #Exploder le K par les enderscorts
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])

            top_left = pivot.check_three_points_top_left(x,y,space,point_dico)
            top_right = pivot.check_three_points_top_right(x,y,space,point_dico)
            bottom_left = pivot.check_three_points_bottom_left(x,y,space,point_dico)
            bottom_right = pivot.check_three_points_bottom_right(x,y,space,point_dico)

            self.makeBuildDico(top_left,True)
            self.makeBuildDico(top_right,True)
            self.makeBuildDico(bottom_left,True)
            self.makeBuildDico(bottom_right,True)

    def checkTwoPointDico(self,point_dico,space):
        #Parcourt le dictionnaire
        for k in self.ownDico:
            #Exploder le K par les enderscorts
            array = k.split('_')
            x = int(array[0])
            y = int(array[1])

            top_left = pivot.check_two_points_top_left(x,y,space,point_dico)
            top_right = pivot.check_two_points_top_right(x,y,space,point_dico)
            bottom_left = pivot.check_two_points_bottom_left(x,y,space,point_dico)
            bottom_right = pivot.check_two_points_bottom_right(x,y,space,point_dico)

            self.makeBuildDico(top_left,False)
            self.makeBuildDico(top_right,False)
            self.makeBuildDico(bottom_left,False)
            self.makeBuildDico(bottom_right,False)

    def makeBuildDico(self,dico,one_point):
        if(len(dico)):
            point = str(str(dico['x'])+'_'+str(dico['y']))
            if(one_point):
                if point in self.onePointDico:
                    self.onePointDico[point] = self.onePointDico[point] + 1
                else:
                    self.onePointDico[point] = 1
            else:
                if point in self.twoPointDico:
                    self.twoPointDico[point] = self.twoPointDico[point] + 1
                else:
                    self.twoPointDico[point] = 1

    def canBuild(self):
        if len(self.onePointDico) | len(self.twoPointDico):
            return True
        else:
            return False

    def randPoint(self,can,point_dico):

        r = 5

        secure_random = random.SystemRandom()
        coord = secure_random.choice(self.randomList)
        array = coord.split('_')
        x = int(array[0])
        y = int(array[1])

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
        self.otherDico[coord] = color

    #Score de l'IA
    def getScore(self):
        return self.score

    #Modification du score de l'IA
    def setScore(self):
        self.score = self.score + 1

    def getColor(self):
        return self.color
