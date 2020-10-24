#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Alex Coninx
    ISIR - Sorbonne Universite / CNRS
    04/10/2019
"""

import numpy as np
import copy

J1_X = 1 # Les coups du joueur 1 ("X") sont codés par 1
J2_O = -1 # Les coups du joueur 2 ("O") sont codés par -1
EMPTY = 0 # Cases vide

class GrilleMorpion:
	def __init__(self, taille, n_victoire):
		""" Crée une grille de morpion d'une taille donnée. n_victoire est le nombre de pions à aligner pour gagner"""
		self.taille = taille # Coté de la grille
		self.n_victoire = n_victoire
		if(n_victoire > taille):
			raise(RuntimeError("Grid size is %d but players must align %d positions - nobody can win !" % (taille, n_victoire)))
		self.grille = np.zeros((taille,taille),dtype=np.int8) # Initialise la grille vide

	def afficher(self):
		""" Affiche la grille en console."""
		print("    ", end='')
		for i in range(self.taille):
			print("%d " % (i+1), end='')
		print("")
		print("   ╔" + "═╤"*(self.taille-1) + "═╗")
		for i in range(self.taille):
			print("%2d ║" % (i+1), end='')
			for j in range(self.taille):
				if(self.grille[i,j] == J1_X):
					print("X", end='')
				elif(self.grille[i,j] == J2_O):
					print("O", end='')
				elif(self.grille[i,j] == EMPTY):
					print(" ", end='')
				else:
					raise(RuntimeError("Unknown value %d at location (%d, %d) of a game grid" % (self.grille[i,j], i, j)))
				if(j < self.taille-1):
					print("│", end='')
			print("║")
			if(i < self.taille-1):
				print("   ╟" + "─┼"*(self.taille-1) + "─╢")
		print("   ╚" + "═╧"*(self.taille-1) + "═╝")

	def libre(self, ligne, col):
		""" Renvoie True si la case (ligne, colonne) est une case valide et libre, False sinon."""
		if(ligne >= 0 and col >= 0 and ligne < self.taille and col < self.taille): # Case valide de la grille
			return (self.grille[ligne,col] == 0) # Renvoie vraie si la case est libre, faux sinon
		else:
			return False # hors de la grille

	def jouer(self, ligne, col, joueur):
		""" Joue un coup du sur la case (ligne, colonne). Joueur doit être J1_X ou J2_O"""
		if(self.grille[ligne,col] != 0): # On vérifie que la case existe et est libre
			raise(RuntimeError("Tried to play %d at nonempty or inexistant location (%d, %d) of a game grid" % (joueur, ligne, col)))
		else:
			self.grille[ligne,col] = joueur # Jouer

	def evaluer(self,joueur):
                """ Evalue la position du point de vue de (joueur). Renvoie un tuple (valeur, fin_partie) où :
		    valeur vaut (voir sujet):
		    * np.inf si la partie est terminée en victoire pour joueur
		    * -np.inf si la partie est terminée en défaite pour joueur
		    * 0 si la partie est terminée en match nul
		    * Et si la partie n'est pas terminée :
		      * (taille du plus grand alignement de pions de joueur) si cette taille est supérieure à celle de l'adversaire
		      * -(taille du plus grand alignement de pions de l'adversaire) si cette taille est supérieure à la nôtre l'adversaire
		      * 0 si on a autant de pions que l'adversaire
		    fin_partie vaut True si la partie est finie (par la victoire ou un match nul), False sinon
		"""
                nvictoire = self.n_victoire
                valeur =0
                fin_partie = False

                compteurLv = 0              #compteur courant de "1" en ligne
                compteurCv=[0]*self.taille  #compteur courant de "1" en colonne
                compteurLd = 0              #compteur courant de "-1" en ligne
                compteurCd=[0]*self.taille  #compteur courant de "-1" en colonne

                maxcompteurLv = 0 # max de chacun des compteurs précédents
                maxcompteurCv=[0]*self.taille
                maxcompteurLd = 0
                maxcompteurCd=[0]*self.taille


                for i in range(self.taille):
                    compteurLv = 0
                    compteurLd = 0
                    for j in range(self.taille):


                        if self.grille[i,j] == 1:
                            # Gestion compteur en ligne
                            compteurLv +=1
                            compteurLd=0
                            if compteurLv > maxcompteurLv:
                                maxcompteurLv = compteurLv

                            # Gestion compteur en colonne
                            compteurCv[j]+=1
                            compteurCd[j]=0
                            if compteurCv[j] > maxcompteurCv[j]:
                                maxcompteurCv[j] = compteurCv[j]

                        if self.grille[i,j] == -1:
                            # Gestion compteur en ligne
                            compteurLd +=1
                            compteurLv=0
                            if compteurLd > maxcompteurLd:
                                maxcompteurLd = compteurLd
                             # Gestion compteur en colonne
                            compteurCd[j]+=1
                            compteurCv[j]=0
                            if compteurCd[j] > maxcompteurCd[j]:
                                maxcompteurCd[j] = compteurCd[j]

                        if self.grille[i,j] == 0:
                            # Gestion compteur en ligne
                            compteurLv = 0
                            compteurLd = 0
                            compteurCd[j]=0
                            compteurCv[j] = 0



                #Gestion des diagonales
                #compteur de "1" et "-1" pour les diagonales partant de GAUCHE
                compteurdg = self.clone() #compteur "1"
                compteurdg2 = self.clone()#compteur "-1"

                for i in range(1,self.taille):
                        for j in range(1,self.taille):

                            if compteurdg.grille[i-1, j-1] >= 1 and compteurdg.grille[i, j] == 1:
                                compteurdg.grille[i, j] = compteurdg.grille[i-1, j-1] + 1

                            if compteurdg2.grille[i-1, j-1] <= -1 and compteurdg2.grille[i, j] == -1:
                                compteurdg2.grille[i, j] = compteurdg2.grille[i-1, j-1] - 1

                # compteur de "1" et "-1" pour les diagonales partant de DROITE
                compteurdd = self.clone() # compteur"1"
                compteurdd2 = self.clone() # compteur"-1"
                for i in range(1,self.taille):
                    for j in range(0,self.taille-1):
                        if compteurdd.grille[i -1, j +1] >= 1 and compteurdd.grille[i, j] == 1: #On etudie la diagonale
                            compteurdd.grille[i, j] = compteurdd.grille[i -1, j +1] + 1

                        if compteurdd2.grille[i -1, j +1] <= -1 and compteurdd2.grille[i, j] == -1:
                            compteurdd2.grille[i, j] = compteurdd2.grille[i -1, j +1] -1

                # Maximum des tableaux afin de comptabiliser les deux diagonales
                maxcompteurdg = compteurdg.grille.max()
                maxcompteurdd = compteurdd.grille.max()

                maxcompteurdg2 = -compteurdg2.grille.min()#on récupère la plus petite valeur , ici négative , et on prend son opposé
                maxcompteurdd2= -compteurdd2.grille.min()#idem on récupère la plus petite valeur (négative) du tableau
                # Maximum de "1" = croix sur les diagonales
                maxcompteurDv = max(maxcompteurdg,maxcompteurdd)
                # Maximum de "-1" = rond sur les diagonales
                maxcompteurDd = max(maxcompteurdg2, maxcompteurdd2)

                #print("Compteur colonne X",maxcompteurCv)
                #print("Compteur ligne X",maxcompteurLv)
                #print("Compteur colonne O",maxcompteurCd)
                #print("Compteur ligne O",maxcompteurLd)
                #print("Compteur diag X gauche",compteurdg.grille)
                #print("Compteur diag X droite", compteurdd.grille)
                #print("Compteur diag O droite",compteurdd2.grille)

                #Cas ou la partie est terminée

                #1) Scénario 1 : J1_X gagne
                if (maxcompteurLv > nvictoire-1) or (max(maxcompteurCv) > nvictoire-1) or (maxcompteurDv > nvictoire-1):
                    if joueur == J1_X:
                        valeur = np.inf
                        fin_partie = True
                    else:
                        valeur = -np.inf
                        fin_partie = True
                    return (valeur, fin_partie)

                #2)Scénario 2 : J1_0 gagne
                if (maxcompteurLd > nvictoire - 1) or (max(maxcompteurCd) > nvictoire - 1) or (maxcompteurDd > nvictoire - 1):
                    if joueur == J2_O:
                        valeur = np.inf
                        fin_partie = True
                    else:
                        valeur = -np.inf
                        fin_partie = True
                    return (valeur, fin_partie)
                #3)Cas ou la grille est plein : match nul
                if self.pleine() == True:
                    valeur=0
                    fin_partie = True
                    return (valeur, fin_partie)

                #Cas ou la partie n'est pas terminée
                else:
                    valeurv= max(max(maxcompteurCv),maxcompteurLv,maxcompteurDv)
                    valeurd= max(max(maxcompteurCd),maxcompteurLd,maxcompteurDd)
                    if valeurv>valeurd:
                            valeur = valeurv
                            fin_partie = False
                    if valeurv == valeurd:
                            valeur = 0
                            fin_partie = False
                    if valeurd > valeurv:
                            valeur = -valeurd
                            fin_partie = False
                    #print("valeur",valeur)
                    return (valeur, fin_partie)



	def pleine(self):
		""" Renvoie True si la grille est pleine. (Si la grille est pleine et que personne n'a gagné, égalité.)"""
		return (0 not in self.grille)

	def clone(self):
		"""Renvoie une copie de la grille."""
		return copy.deepcopy(self)
