########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 17/05/2017
# Module           : Terrain
#
########################################################

class Terrain(object):

    def __init__(self,width,height,space,can):
        self.width = width
        self.height = height
        self.space = space
        self.can = can

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSpace(self):
        return self.space

    #Création de la ligne horizontale avec un espacement de 30
    def horizontalLine(self):
        d = 0
        while d < self.width :
            self.can.create_line(d, 0, d, self.height, fill ='cyan') #Création de la ligne horizontale avec un espacement de 30
            d = d + self.space

    #Création de la ligne verticale avec un espacement de 30
    def verticalLine(self):
        d = 0
        while d < self.height :
            self.can.create_line(0, d, self.width, d, fill ='cyan') #Création de la ligne verticale avec un espacement de 30
            d = d + self.space

    #Vérifie si l'utilisateur est dans la zone de jeu
    def overFlow(self,x,y):
        if(y <= (self.width - self.space)) & (y >= self.space):
            if(x <= (self.height - self.space)) & (x >= self.space):
                return True
            else:
                return False
        else:
            return False

    #Verifie la porté du point de l'utilisateur avec une marge de 2
    def checkRayon(self,x,y):
        Rx = x % self.space
        Ry = y % self.space

        if(Ry == 0) | (Ry == 1) | (Ry == 2) | (Ry == (self.space - 2)) | (Ry == (self.space - 1)):
            if(Rx == 0) | (Rx == 1) | (Rx == 2) | (Rx == (self.space - 2)) | (Rx == (self.space - 1)):
                return True
            else:
                return False
        else:
            return False

    #Arrondir au multiple le plus proche de 30
    def rang_twenthy(self,val):
        R = val % self.space

        if (R == 1):
            val = val - 1
        elif (R == (self.space - 1)):
            val = val +1
        elif (R == 2):
            val = val - 2
        elif (R == (self.space - 2)):
            val = val + 2

        return val
