"""Module jeu.py : génération de grille, coups du joueur, score et boucle de jeu."""


def generer_grille_complete():
    """Crée une grille de Sudoku pleine et valide, différente à chaque partie."""
    pass


def retirer_cases(grille, nb):
    """Renvoie une copie de la grille avec nb cases remises à 0."""
    pass


def choisir_difficulte(niveau):
    """Renvoie le nombre de cases à retirer selon le niveau choisi."""
    pass


def poser_chiffre(grille, fixes, ligne, col, n):
    """Place n si le coup est permis. Renvoie (True/False, message)."""
    pass


def donner_indice(grille, solution):
    """Renvoie (ligne, col, valeur) d'une case vide, ou None."""
    pass


def formater_temps(secondes):
    """Transforme un nombre de secondes en texte 'MM:SS'."""
    pass


def calculer_score(temps, erreurs, niveau):
    """Calcule le score final (jamais négatif)."""
    pass


def enregistrer_score(nom, score, fichier):
    """Ajoute une ligne nom/score à la fin du fichier des scores."""
    pass


def afficher_meilleurs_scores(fichier, nb=5):
    """Affiche le classement des meilleurs scores."""
    pass


def jouer(grille, solution):
    """Boucle de jeu : menu, coups, indices, fin de partie."""
    pass