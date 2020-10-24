#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Alex Coninx
    ISIR - Sorbonne Universite / CNRS
    05/10/2019
""" 

import numpy as np
import random
from morpion import GrilleMorpion, J1_X, J2_O

def negamax(grille,joueur, profondeur) -> object:
    """ Algo NegaMax. Prends en argument:
		    * Une grille de morpion
		    * Le joueur (J1_X ou J2_O) du point de vue duquel la position sera évaluée
		    * La profondeur d'évaluation (quand on arrive à 0, on utilise l'heuristique au lieu de descendre davantage)
		    Renvoie un tuple (max_val, meilleur_coup) où:
		    * meilleur_coup est un tuple (i,j) correspondant aux coordonnées du meilleur coup à jouer
		    * max_val est la valeur associée
    """
    nbr_appel = 1
    evaluation = grille.evaluer(joueur)

    if ((profondeur == 0) or evaluation[1]):  #eval[1] = True si la partie est terminée (victoire,defaite,nulle)
        return (evaluation[0], (0, 0), nbr_appel) #partie est terminée donc on renvoit (0,0) comme coup à jouer et eval[0] est l'heuristique de la grille
    else: #la partie est en cours
     alpha = -np.inf
     # On va mélanger les lignes et les colonnes afin de parcourir aleatoirement les noeuds enfants, sinon l'IA jouerait toujours la même chose...
     colonnes = list(range(grille.taille))
     lignes = list(range(grille.taille))
     random.shuffle(colonnes)
     random.shuffle(lignes)


     for i in lignes:
         for j in colonnes:
             if (grille.libre(i, j)):
                 if not ('meilleur_coup' in locals()): #On verifie si meilleur coup existe
                     meilleur_coup = (i, j) #ici meilleur coup n'existe pas donc on l'initialise
                 grille_clone = grille.clone()
                 grille_clone.jouer(i, j, joueur)
                 n = negamax(grille_clone, -joueur, profondeur - 1)
                 gamma = -n[0] #on recupère -n[0]= -alpha, opposé  du meilleur coup
                 nbr_appel_aval = n[2] #n[2] = la profondeur actuelle
                 nbr_appel = nbr_appel + nbr_appel_aval #on incremente pour compter le nb d'appels total
                 if (gamma > alpha):
                     alpha = gamma  # on stock gamma car c'est la plus grande valeur
                     meilleur_coup = (i, j)

    return (alpha, meilleur_coup, nbr_appel)

def negamax_alpha_beta(grille, joueur, profondeur, alpha, beta):
    """ Algo NegaMax_alpha_beta. Prends en argument:
        * Une grille de morpion
        * Le joueur (J1_X ou J2_O) du point de vue duquel la position sera évaluée
        * La profondeur d'évaluation (quand on arrive à 0, on utilise l'heuristique au lieu de descendre davantage)
        Renvoie un tuple (max_val, meilleur_coup nbr_appels) où:
        * meilleur_coup est un tuple (i,j) correspondant aux coordonnées du meilleur coup à jouer
        * max_val est la valeur associée
        * nbr_appels est le nombre d'appels recursifs de la fonction
    """
    nbr_appels = 1
    evaluation = grille.evaluer(joueur)

    if ((profondeur == 0) or evaluation[1]):
        return (evaluation[0], (0, 0), nbr_appels)
    else:
        alpha = -np.inf
        lignes = list(range(grille.taille))
        random.shuffle(lignes)
        colonnes = list(range(grille.taille))
        random.shuffle(colonnes)

        for i in lignes:
            for j in colonnes:
                if (grille.libre(i, j)):
                    if not ('meilleur_coup' in locals()):
                        meilleur_coup = (i, j)
                    g = grille.clone()
                    g.jouer(i, j, joueur)
                    n = negamax_alpha_beta(g, -joueur, profondeur - 1, -beta, -alpha)
                    gamma = -n[0]
                    nbr_appels_aval = n[2]
                    nbr_appels = nbr_appels + nbr_appels_aval
                    if (gamma > alpha):
                        meilleur_coup = (i, j)
                        alpha = gamma
                    if (beta <= alpha):
                        break
    return (alpha, meilleur_coup, nbr_appels)

