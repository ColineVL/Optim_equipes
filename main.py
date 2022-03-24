import sys, os
import pulp
import math

from initialisation import init
from helpers import updateIndexEquipe
from postTraitement import simplePrint

""" Premier essai de code """


def main():
    """Initialisation"""
    arrayColleges, arrayEquipes, nbEquipes, maxParEquipe = init()

    """Boucle de calcul"""
    # Pour chaque collège, je boucle sur les équipes pour dispatcher ses élèves
    for col in arrayColleges:
        studentsLeft = col.nbEleves
        currentIndexEquipe = 0
        while studentsLeft > 0:
            equipe = arrayEquipes[currentIndexEquipe]

            # Si il reste de la place dans l'équipe, on peut la remplir
            if equipe.getNbEleves() + 1 < maxParEquipe:

                # Si on n'a plus que 3 élèves, il faut qu'ils restent ensemble
                if studentsLeft == 3:
                    # Si l'équipe a de la place pour 3 élèves, on peut les placer
                    if equipe.nbEleves + 3 <= maxParEquipe:
                        equipe.setEleves(col, 3)
                        studentsLeft -= 3

                # Sinon, on place les élèves 2 par 2
                else:
                    equipe.setEleves(col, 2)
                    studentsLeft -= 2

            # On passe à l'équipe suivante
            currentIndexEquipe = updateIndexEquipe(currentIndexEquipe, nbEquipes)

    """Affichage des résultats"""
    simplePrint(arrayEquipes, arrayColleges)

    """Vérification"""
    # Aucune équipe ne dépasse le max
    for equipe in arrayEquipes:
        assert equipe.getNbEleves() <= maxParEquipe
    # Les élèves des collèges ont tous été placés
    for college in arrayColleges:
        assert (
            sum([value for value in college.repartition.values()]) == college.nbEleves
        )


if __name__ == "__main__":
    main()
