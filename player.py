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
