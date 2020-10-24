——————————————————————
————————TP– Minimax ———————
——————————————————————
AUTEUR : Samuel Bakhshaei ROB5 et Alexandre Coninx

AVANCEMENT
- NegaMax ainsi que l’Elagage Alpha-Beta qui permet de réduire de manière considérable le nombre d’appels récursifs ont été implémenté
- Le support des diagonales (bonus) a été implémenté

COMMANDES
- Lancement du jeu en mode 2 joueurs :        python3 jeu.py
- Lancement du jeu en mode 1 joueur vs IA :   python3 jeu.py —ia
- Lancement du jeu en mode IA vs IA :         python3 jeu.py —iavsia

OBSERVATIONS
l’IA implémentée à un très bon comportement, mais si la profondeur est trop faible on peut avoit des incohérences.
En effet l'heuristique est assez grossière donc en profondeur faible, l'IA peut prendre des mauvaises décisions.
Avec une profondeur élevée on obtient un jeu à peu près optimal, mais cela est coûteux en temps de calcul.
Par exemple, en lançant leu jeu en mode IA vs IA, avec une grille 3x3 et une profondeur de 7,
on obtient alors un jeu optimal et la partie se termine tout le temps en égalité. Néanmoins le temps de calcul est assez élevé.
En conclusion, il faut donc trouver un bon compromis entre la performance de notre IA (lié à sa profondeur) et le temps de calcul nécessaire.


