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

class Pivot(object):

  #Vérification d'un carré en haut à gauche
  def top_left(self,x,y,space,point_dico):
    x2 = x - space
    y2 = y - space
    P = str(str(x)+'_'+str(y))
    P2 = str(str(x)+'_'+str(y2))
    P3 = str(str(x2)+'_'+str(y))
    P4 = str(str(x2)+'_'+str(y2))

    if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
        if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
            return True

  #Vérification d'un carré en haut à droite
  def top_right(self,x,y,space,point_dico):
      x2 = x + space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x2)+'_'+str(y))

      if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):

          if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):

              return True

  #Vérification d'un carré en bas à gauche
  def bottom_left(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y + space

      P = str(str(x)+'_'+str(y))
      P2 = str(str(x2)+'_'+str(y))
      P3 = str(str(x2)+'_'+str(y2))
      P4 = str(str(x)+'_'+str(y2))

      if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
          if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
              return True

  #Vérification d'un carré en bas à gauche
  def bottom_right(self,x,y,space,point_dico):
      x2 = x + space
      x3 = x - space
      y2 = y + space

      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      if(P2 in point_dico) & (P3 in point_dico) & (P4 in point_dico):
          if(point_dico[P] == point_dico[P2]) & (point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
              return True


  def get_point_top(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      if(P2 in point_dico):
          return False
      else:
          if(P in point_dico) & (P3 in point_dico) & (P4 in point_dico):
              if(point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
                  return {x,y2}


  def get_point_right(self,x,y,space,point_dico):
      x2 = x - space
      y2 = y - space
      P = str(str(x)+'_'+str(y))
      P2 = str(str(x)+'_'+str(y2))
      P3 = str(str(x2)+'_'+str(y))
      P4 = str(str(x2)+'_'+str(y2))

      if(P2 in point_dico):
          return False
      else:
          if(P in point_dico) & (P3 in point_dico) & (P4 in point_dico):
              if(point_dico[P] == point_dico[P3]) & (point_dico[P] == point_dico[P4]):
                  return {x,y2}


  def get_point_top_left(self):
      pass

  def get_point_top_rigth(self):
      pass

  def get_point_bottom(self):
      pass

  def get_point_left(self):
      pass

  def get_point_bottom_left(self):
      pass

  def get_point_bottom_right(self):
      pass



