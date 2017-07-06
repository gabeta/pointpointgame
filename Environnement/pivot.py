########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Compagnie        : EnighmaLab
# Date de création : 17/05/2017
# Module           : Pivot
#
########################################################
from random import randrange

class Pivot(object):

  width = 630
  height = 540

  def check_three_points(self,P,P2,P3,P4,point_dico,space):
      point = {}

      if(P2 in point_dico) | (P3 in point_dico) | (P4 in point_dico):
          return point
      else:
          coord = randrange(1,3)
          if(coord == 1):
              Pf = P2
          elif(coord == 2):
              Pf = P3
          else:
              Pf = P4

          array = Pf.split('_')
          xf = int(array[0])
          yf = int(array[1])
          point['x'] = xf
          point['y'] = yf

          if self.overFlow(xf,yf,space):
              return point
          else:
              return {}

  def check_two_points(self,P,P2,P3,P4,point_dico,space):
      point = {}
      if(P2 in point_dico):
          if (point_dico[P2] == point_dico[P]):
              if(P3 in point_dico) | (P4 in point_dico):
                return point
              else:
                  coord = randrange(1,2)
                  if(coord == 1):
                      final = P3
                  else:
                      final = P4
              array = final.split('_')
              xf = int(array[0])
              yf = int(array[1])
              point['x'] = xf
              point['y'] = yf

              if self.overFlow(xf,yf,space) :
                  return point
              else:
                  return {}

          else:
              return point
      elif(P3 in point_dico):
          if (point_dico[P3] == point_dico[P]):
              if(P2 in point_dico) | (P4 in point_dico):
                return point
              else:
                  coord = randrange(1,2)
                  if(coord == 1):
                      final = P2
                  else:
                      final = P4
              array = final.split('_')
              xf = int(array[0])
              yf = int(array[1])
              point['x'] = xf
              point['y'] = yf

              if self.overFlow(xf,yf,space) :
                  return point
              else:
                  return {}


          else:
              return point
      elif(P4 in point_dico):
          if (point_dico[P4] == point_dico[P]):
              if(P2 in point_dico) | (P3 in point_dico):
                return point
              else:
                  coord = randrange(1,2)
                  if(coord == 1):
                      final = P2
                  else:
                      final = P4
              array = final.split('_')
              xf = int(array[0])
              yf = int(array[1])
              point['x'] = xf
              point['y'] = yf

              if self.overFlow(xf,yf,space) :
                  return point
              else:
                  return {}


          else:
              return point
      else:
          return point

  def carre(self,P,P2,P3,P4,point_dico):
    if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
        if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
            return True

  #Vérification d'un carré en haut à gauche
  def top_left(self,x,y,space,point_dico):
    x2 = x - space
    y2 = y - space
    P = str(str(x)+'_'+str(y))
    P2 = str(str(x)+'_'+str(y2))
    P3 = str(str(x2)+'_'+str(y))
    P4 = str(str(x2)+'_'+str(y2))

    return self.carre(P,P2,P3,P4,point_dico)

  #Vérification d'un carré en haut à droite
  def top_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x2)+'_'+str(y))

      return self.carre(P,P2,P3,P4,point_dico)

  #Vérification d'un carré en bas à gauche
  def bottom_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x2)+'_'+str(y))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x)+'_'+str(y2))

      return self.carre(P,P2,P3,P4,point_dico)

  #Vérification d'un carré en bas à droit
  def bottom_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      return self.carre(P,P2,P3,P4,point_dico)

  def get_point_top_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))
      point = {}

      if(P2 in point_dico):
          return point
      else:
          if(P in point_dico) & (P3 in point_dico) & (P4 in point_dico):
              if(point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
                  point['x'] = x
                  point['y'] = y2
                  return point
              else:
                  return point
          else:
              return point

  def get_point_top_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x2)+'_'+str(y))
      point = {}

      if(P2 in point_dico):
          return point
      else:
          if(P in point_dico) & (P3 in point_dico) & (P4 in point_dico):
              if(point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
                  point['x'] = x
                  point['y'] = y2
                  return point
              else:
                  return point
          else:
              return point

  def get_point_bottom_right(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x2)+'_'+str(y))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x)+'_'+str(y2))
      point = {}

      if(P4 in point_dico):
          return point
      else:
          if(P in point_dico) & (P3 in point_dico) & (P2 in point_dico):
              if(point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P2]):
                  point['x'] = x
                  point['y'] = y2
                  return point
              else:
                  return point
          else:
              return point

  def get_point_bottom_left(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x2)+'_'+str(y))

      point = {}

      if(P2 in point_dico):
          return point
      else:
          if(P in point_dico) & (P3 in point_dico) & (P4 in point_dico):
              if(point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
                  point['x'] = x
                  point['y'] = y2
                  return point
              else:
                  return point
          else:
              return point

  def check_three_points_top_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      return self.check_three_points(P,P2,P3,P4,point_dico,space)

  def check_three_points_top_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x2)+'_'+str(y))

      return self.check_three_points(P,P2,P3,P4,point_dico,space)

  def check_three_points_bottom_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x2)+'_'+str(y))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x)+'_'+str(y2))

      return self.check_three_points(P,P2,P3,P4,point_dico,space)

  def check_three_points_bottom_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      return self.check_three_points(P,P2,P3,P4,point_dico,space)

  def check_two_points_top_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      return self.check_two_points(P,P2,P3,P4,point_dico,space)

  def check_two_points_top_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x2)+'_'+str(y))

      return self.check_two_points(P,P2,P3,P4,point_dico,space)

  def check_two_points_bottom_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x2)+'_'+str(y))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x)+'_'+str(y2))

      return self.check_two_points(P,P2,P3,P4,point_dico,space)

  def check_two_points_bottom_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y + space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      return self.check_two_points(P,P2,P3,P4,point_dico,space)

  #Vérifie si l'IA est dans la zone de jeu
  def overFlow(self,x,y,space):
      if(y <= (self.height - space)) & (y >= space):
          if(x <= (self.width - space)) & (x >= space):
              return True
          else:
              return False
      else:
          return False
