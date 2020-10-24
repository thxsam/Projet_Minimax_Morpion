import numpy as np
import sys

from morpion import GrilleMorpion, J1_X, J2_O
from ia_morpion import negamax

if (__name__ == "__main__"):
    taille = 4
    nvictoire = 3

    print(" Test scénario 1 : Victoire J1(X) en ligne")
    g1 = GrilleMorpion(taille, nvictoire)
    for i in range(g1.n_victoire):
        g1.jouer(1, i, J1_X)

    g1.afficher()
    if (g1.evaluer(J1_X) == (np.inf, True)):
        print("(J1X) Bonne heuristique et etat du jeu correct (1)")
    else:
        print("(J1X)Mauvaise heuristique ou etat du jeu incorrect (1)")

    if (g1.evaluer(J2_O) == (-np.inf, True)):
        print("(J20)Bonne heuristique et etat du jeu correct (1)")
    else :
        print("(J20)Mauvaise heuristique ou etat du jeu incorrect (1)")
        print(" Eval renvoit ", g1.evaluer(J2_O)[0], g1.evaluer(J2_O)[1])


    print(" Test scénario 1BIS : Victoire J2(O) en ligne")
    g1bis = GrilleMorpion(taille, nvictoire)
    for i in range(g1bis.n_victoire):
        g1bis.jouer(1, i, J2_O)

    g1bis.afficher()
    if (g1bis.evaluer(J1_X) == (-np.inf, True)):
        print("(J1X) Bonne heuristique et etat du jeu correct (1bis)")
    else:
        print("(J1X)Mauvaise heuristique ou etat du jeu incorrect (1bis)")
        print(" Eval renvoit ", g1bis.evaluer(J2_O)[0], g1bis.evaluer(J2_O)[1])

    if (g1bis.evaluer(J2_O) == (np.inf, True)):
        print("(J20)Bonne heuristique et etat du jeu correct (1bis)")
    else :
        print("(J20)Mauvaise heuristique ou etat du jeu incorrect (1bis)")
        print(" Eval renvoit ", g1bis.evaluer(J2_O)[0], g1bis.evaluer(J2_O)[1])


    print(" Test scénario 2 : Victoire J1(X) en colonne")
    g2 = GrilleMorpion(taille, nvictoire)
    for i in range(g1.n_victoire):
        g2.jouer(i, 1, J1_X)
    g2.afficher()
    if (g2.evaluer(J1_X) == (np.inf, True)):
        print("(J1X) Bonne heuristique et etat du jeu correct (2)")
    else:
        print("(J1X)Mauvaise heuristique ou etat du jeu incorrect (2)")

    if (g2.evaluer(J2_O) == (-np.inf, True)):
        print("(J20)Bonne heuristique et etat du jeu correct (2)")
    else:
        print("(J20)Mauvaise heuristique ou etat du jeu incorrect (2)")
        print(" Eval renvoit ", g2.evaluer(J2_O)[0],g2.evaluer(J2_O)[1])

    print(" Test scénario 2bis : Victoire J1(X) en colonne")
    g2bis = GrilleMorpion(taille, nvictoire)
    for i in range(g1.n_victoire):
        g2bis.jouer(i, 1, J2_O)
    g2bis.afficher()
    if (g2bis.evaluer(J1_X) == (-np.inf, True)):
        print("(J1X) Bonne heuristique et etat du jeu correct (2bis)")
    else:
        print("(J1X)Mauvaise heuristique ou etat du jeu incorrect (2bis)")

    if (g2bis.evaluer(J2_O) == (np.inf, True)):
        print("(J20)Bonne heuristique et etat du jeu correct (2bis)")
    else:
        print("(J20)Mauvaise heuristique ou etat du jeu incorrect (2)")
        print(" Eval renvoit ", g2bis.evaluer(J2_O)[0], g2bis.evaluer(J2_O)[1])


    print(" Test scénario 3 : Victoire J1(X) en diagonale")
    g3 = GrilleMorpion(taille, nvictoire)
    for i in range(g1.n_victoire):
        g3.jouer(i, i, J1_X)
    g3.afficher()
    if (g3.evaluer(J1_X) == (np.inf, True)):
        print("(J1X) Bonne heuristique et etat du jeu correct (3)")
    else:
        print("(J1X)Mauvaise heuristique ou etat du jeu incorrect (3)")

    if (g3.evaluer(J2_O) == (-np.inf, True)):
        print("(J20)Bonne heuristique et etat du jeu correct (3)")
    else:
        print("(J20)Mauvaise heuristique ou etat du jeu incorrect (3)")
        print(" Eval renvoit ", g3.evaluer(J3_O)[0], g3.evaluer(J3_O)[1])

    print(" Test scénario 4 : Victoire J2_0) en diagonale")
    g4 = GrilleMorpion(taille, nvictoire)
    for i in range(g1.n_victoire):
        g4.jouer(i, i, J2_O)
    g4.afficher()
    if (g4.evaluer(J1_X) == (-np.inf, True)):
        print("(J1X) Bonne heuristique et etat du jeu correct (4)")
    else:
        print("(J1X)Mauvaise heuristique ou etat du jeu incorrect (4)")

    if (g4.evaluer(J2_O) == (np.inf, True)):
        print("(J20)Bonne heuristique et etat du jeu correct (4)")
    else:
        print("(J20)Mauvaise heuristique ou etat du jeu incorrect (4)")
        print(" Eval renvoit ", g4.evaluer(J4_O)[0], g4.evaluer(J4_O)[1])