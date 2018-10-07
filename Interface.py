########################################################
#                  POINT POINT GAME
#
# Catégorie        : Stratégie
# Auteur           : Gabeta Soro (Alchimiste des codes)
# Pseudo           : @lChiMi5tE_d0t_toRr€nt
# Compagnie        : EnighmaLab
# Date de création : 17/05/2017
# Scène            : Player vs Player
#
# contributeur     : sletort
########################################################

# Aims
from tkinter import *

from Environnement.terrain import Terrain
from Environnement.pivot import Pivot

def build_interface( fen, create_plateform, click_gauche ):
	#Paramètre Terrain -- space et r sont utilisés plus tard, ils devraient être différents ...
	space = 30
	r = 5
	Theight = 540
	Twidth = 630

	can = Canvas(fen, width =Twidth, height =Theight, \
					bg="light yellow", borderwidth=2, relief=SOLID )
	can.bind('<Button-1>', click_gauche )
	can.grid(row = 0, rowspan = 45)

	terrain = Terrain(Twidth,Theight,space,can)

	b1 = Button(fen,bg='#FAF8E9',relief=GROOVE, text='Commencer',width=15, command=create_plateform)
	b1.grid(row = 0,column = 1)

	b2 = Button(fen,bg='#FAF8E9',relief=GROOVE, text='Instructtion',width=15, command=create_plateform)
	b2.grid(row = 1,column = 1)

	info = Label(fen,bg='#6699CC', text='Joueur Bleu',width=15,pady=5,relief=GROOVE)
	info.grid(row = 13,column = 1)

	info2 = Label(fen,bg='#FF6666', text='Joueur Rouge',width=15,pady=5,relief=GROOVE)
	info2.grid(row = 15,column = 1)

	b3 = Button(fen,bg='#FAF8E9',relief=GROOVE, text='Quitter',width=15, command=fen.quit)
	b3.grid(row = 44,column = 1)

	role = Label(fen)
	role.grid(row = 44)

	chaine = Label(fen,fg='red')
	chaine.grid(row = 45)

	# je renvoie un dico d'objet pour le moment,
	#	mais le mieux serait d'y avoir accès à travers fen
	return {
		'info': info,
		'info2': info2,
		'terrain' : terrain,
		'chaine'  : chaine,
		'can' : can,
		'role': role,
		'space': space,
		'r': r,
	}


class Jeu():
	begin = False # j'ai du mal à comprendre cette variable

	def __init__( self, player1, player2, fn_iaTour=None ):
		self.__fen = Tk()
		self.__fen.title("Point point Game By EnighmaLab")

		self.__player1 = player1
		self.__player2 = player2
		self.__fn_iaTour = fn_iaTour # pas top, devrait être lié à player2

		#Classe qui gère les pivots(Vérifie que les points de même couleurs forment un carré)
		self.__pivot = Pivot()


		self.__d_objects = build_interface( self.__fen, \
							create_plateform=self.__début_de_jeu,
							click_gauche=self.__point )

		self.__current_p = self.__player1
		self.__d_points  = {}
	# __init__

	@property
	def current_player( self ):
		return self.__current_p

	@property
	def canvas( self ):
		return self.__d_objects['can']
	@property
	def space( self ):
		return self.__d_objects['space']
	@property
	def d_points( self ):
		return self.__d_points


	def run( self ):
		self.__fen.mainloop()

	def __début_de_jeu( self ):
		#Création de la plateform de jeu
		if( self.begin is False):
			d = 0
			# si 1er tour, le score est à 0.
			self.__d_objects['info'].configure(text = "Joueur Bleu  = 0" )
			self.__d_objects['info2'].configure(text = "Joueur Rouge = 0" )

			self.__d_objects['terrain'].horizontalLine()
			self.__d_objects['terrain'].verticalLine()

			self.begin = True
	# __début_de_jeu

	def __point( self, event ):
		terrain = self.__d_objects['terrain']
		chaine  = self.__d_objects['chaine']
		can     = self.__d_objects['can']

		if not terrain.overFlow(event.y,event.x) \
				or not terrain.checkRayon(event.y,event.x):
			return

		event.y = terrain.rang_twenthy(event.y)
		event.x = terrain.rang_twenthy(event.x)
		value = str(str(event.x)+'_'+str(event.y))

		if value in self.__d_points:
			chaine.configure(text = "Il y a déjà un point à ce emplacement")
			return

		r = self.__d_objects['r']
		self.__d_points[value] = self.__current_p.getColor()

		self.dessine_rond( event.x, event.y )
		self.makeCarre(event.x,event.y)

		if None is self.__fn_iaTour:
			self.change_joueur()
		else:
			self.__player2.setOtherDico(value, self.__current_p.getColor())
			self.__player2.updateRandomList(value)

			self.__current_p = self.__player2
			self.__fn_iaTour( self )
	# __point

	def change_joueur( self ):
		# next_color devrait être current_p.color
		chaine  = self.__d_objects['chaine']
		role    = self.__d_objects['role']

		if self.__current_p == self.__player1:
			self.__current_p = self.__player2
			next_color = "rouge"
		else:
			self.__current_p = self.__player1
			next_color = "bleu"

		chaine.configure(text = "")
		role.configure(text="Veuillez patienter!! Au tour du joueur "+next_color+" de jouer. ")

		return
	# change_joueur

	def makeCarre( self, x,y ):
		#Marquer un point en faisant un carré
		# space devrait être intégré à Pivot je pense, c'est un élément de l'interface, pas du jeu ...
		chaine  = self.__d_objects['chaine']
		can     = self.__d_objects['can']
		info    = self.__d_objects['info']
		info2   = self.__d_objects['info2']
		space   = self.__d_objects['space']

		win_a_point = False
		if self.__pivot.top_left( x,y,space, self.__d_points ):
			can.create_rectangle(x-space, y-space, x, y, fill=self.__current_p.getColor())
			win_a_point = True

		elif self.__pivot.top_right(x,y,space, self.__d_points ):
			can.create_rectangle(x, y-space, x+space, y, fill=self.__current_p.getColor())
			win_a_point = True

		elif self.__pivot.bottom_left(x,y,space, self.__d_points ):
			can.create_rectangle(x, y+space, x-space, y, fill=self.__current_p.getColor())
			win_a_point = True

		elif self.__pivot.bottom_right(x,y,space,self.__d_points ):
			can.create_rectangle(x, y, x+space, y+space, fill=self.__current_p.getColor())
			win_a_point = True

		if win_a_point:
			self.__current_p.setScore()
			info.configure(text = "Joueur Bleu  = " + str(self.__player1.getScore()))
			info2.configure(text = "Joueur Rouge = " + str(self.__player2.getScore()))
			chaine.configure(text = "Joli point")
	# makeCarre

	def dessine_rond( self, x,y ):
		r = self.__d_objects['r']
		color = self.__current_p.getColor()
		self.canvas.create_oval( x-r, y-r, x+r, y+r, \
					fill=color )
