#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Alex Coninx
    ISIR - Sorbonne Universite / CNRS
    04/10/2019
""" 

import numpy as np
import sys

from morpion import GrilleMorpion, J1_X, J2_O
from ia_morpion import negamax
from ia_morpion import negamax_alpha_beta


taille_grille_defaut = 5 # Taille de la grille par défaut
n_victoire_defaut = 4 # Nombre de pions à aligner par défaut
profondeur_defaut = 3 # Profondeur de l'algo NegaMax par défaut

def gerer_coup_humain(grille,joueur):
	""" Affiche la grille, demande son coup au joueur (joueur 1 J1_X
	    ou joueur 2 J2_O), et joue si le coup est valide (redemande sinon)
	"""
	grille.afficher()
	print("Coup du joueur "+("1 (X)" if (joueur == J1_X) else "2 (O)")+" (humain) :")
	while(True): # Boucle jusqu'à avoir une case valide
		i = int(input("Ligne ?")) - 1 #-1 car les cases sont numérotées de 1 à N mais le tableau est indexé de 0 à N-1
		j = int(input("Colonne ?")) - 1
		if(grille.libre(i,j)): #Case valide
			grille.jouer(i,j,joueur)
			break
		else:
			print("Case inexistante ou déjà occupée !")

def gerer_coup_IA(grille, joueur, profondeur):
	print("Coup du joueur " + ("1 (X)" if (joueur == J1_X) else "2 (O)") + " (IA) :")

	#(alpha, pos, nbr_appels) = negamax(grille, joueur, profondeur) # NegaMax
	(alpha, position, nbr_appels) = negamax_alpha_beta(grille, joueur, profondeur, -np.inf, np.inf) # Negamax avec elagage
	print("Je joue  : (" + str(position[0] + 1) +"," ' ' + str(position[1] + 1) + ") avec un meilleur coup =  " + str(alpha))
	print("Nombre d'appels recursifs : " + str(nbr_appels))
	grille.jouer(position[0], position[1], joueur)
	grille.afficher()
	print("=====================")
""" Affiche la grille, lance l'algorithme NegaMax avec la
	    profondeur demandée pour calculer le coup du joueur
	    IA (joueur 1 J1_X ou joueur 2 J2_O) et joue
"""
def verifier_fin_partie(grille):
	""" Appelle evaluer() sur la grille, et si la partie est terminée
	    affiche le vainqueur (s'il y en a un) et renvoie True. Sinon,
	    renvoie False.
	"""
	valeur, fin = grille.evaluer(J1_X) # J1 par exemple
	print(" Valeur : ",valeur)
	if(fin): # Le jeu est fini
		if(valeur > 0):
			print("*** Victoire du joueur 1 (X) ! ***")
		elif(valeur < 0):
			print("*** Victoire du joueur 2 (O) ! ***")
		else:
			print("*** Egalité !***")
	return fin



def saisie_int_defaut(texte, defaut):
	""" Méthode utilitaire permettant de demander à l'utilisataire de saisir un entier,
	    qui prend une valeur par défaut si on ne rentre rien.
	"""
	text = input("%s (défaut : %d) ? " % (texte, defaut))
	return int(text) if text else defaut



def jeu1J():
	""" Lance une partie 1 joueurs. """
	taille = saisie_int_defaut("Taille de la grille",taille_grille_defaut)
	nvictoire = saisie_int_defaut("Nombres de pions à aligner pour gagner",n_victoire_defaut)
	profondeur = saisie_int_defaut("Profondeur algo NegaMax",profondeur_defaut)
	g = GrilleMorpion(taille, nvictoire)
	tour = 1
	while(True):
		print("=====================")
		print("Tour %d" % tour)
		print("=====================")
		#gerer_coup_IA(g,J1_X,profondeur)
		gerer_coup_humain(g, J1_X)
		if(verifier_fin_partie(g)):
			break
		#gerer_coup_humain(g,J2_O)
		gerer_coup_IA(g, J2_O, profondeur)
		tour += 1
		if(verifier_fin_partie(g)):
			break
	print("=====================")
	print("Partie terminée. Grille finale:")
	print("=====================")
	g.afficher()
	
	# TODO A programmer !

def jeu2J():
	""" Lance une partie 2 joueurs. """
	taille = saisie_int_defaut("Taille de la grille",4)
	nvictoire = saisie_int_defaut("Nombres de pions à aligner pour gagner",3)
	# Créer la grille
	g = GrilleMorpion(taille, nvictoire)
	tour = 1
	while(True):
		print("=====================")
		print("Tour %d" % tour)
		print("=====================")
		gerer_coup_humain(g, J1_X)
		if(verifier_fin_partie(g)):
			break
		gerer_coup_humain(g, J2_O)
		tour += 1
		if(verifier_fin_partie(g)):
			break
	print("Partie terminée. Grille finale:")
	g.afficher()

def jeuIA():
	""" Lance une partie IA vs IA """
	taille = saisie_int_defaut("Taille de la grille",taille_grille_defaut)
	nvictoire = saisie_int_defaut("Nombres de pions à aligner pour gagner",n_victoire_defaut)
	profondeur = saisie_int_defaut("Profondeur algo NegaMax",profondeur_defaut)
	g = GrilleMorpion(taille, nvictoire)
	tour = 1
	while(True):
		print("=====================")
		print("Tour %d" % tour)
		print("=====================")

		gerer_coup_IA(g,J1_X,profondeur)
		if(verifier_fin_partie(g)):
			break
		gerer_coup_IA(g, J2_O, profondeur)
		tour += 1
		if(verifier_fin_partie(g)):
			break
	print("=====================")
	print("Partie terminée. Grille finale:")
	print("=====================")
	g.afficher()

if(__name__ == "__main__"):
	if(len(sys.argv) > 1 and (sys.argv[1] == "--ia")):
		print("===* Morpion - jeu humain (X) contre IA (O) *===")
		jeu1J()
	elif (len(sys.argv) > 1 and (sys.argv[1] == "--iavsia")):
		print("===* Morpion - IA(X) contre IA (O) *===")
		jeuIA()
	else:
		print("===* Morpion - jeu 2 joueurs *===")
		jeu2J()
