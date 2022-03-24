import sys, os


from initialisation import init, readExcel
from helpers import updateIndexEquipe
from postTraitement import simplePrint

""" Premier essai de code """


def main():
    """Initialisation"""
    arrayColleges = readExcel()
    nbEquipes = 2
    arrayEquipes, maxParEquipe = init(arrayColleges, nbEquipes)

    """Boucle de calcul"""
    # Pour chaque collège, je boucle sur les équipes pour dispatcher ses élèves
    for col in arrayColleges:
        currentIndexEquipe = 0
        while col.elevesRestants > 0:

            if currentIndexEquipe == 0:
                print("On est à l'équipe 0")
            equipe = arrayEquipes[currentIndexEquipe]

            # Si il reste de la place dans l'équipe, on peut la remplir
            if equipe.getNbEleves() + 1 < maxParEquipe:

                # Si on n'a plus que 3 élèves, il faut qu'ils restent ensemble
                if col.elevesRestants == 3:
                    # Si l'équipe a de la place pour 3 élèves, on peut les placer
                    if equipe.nbEleves + 3 <= maxParEquipe:
                        equipe.setEleves(col, 3)

                # Sinon, on place les élèves 2 par 2
                else:
                    equipe.setEleves(col, 2)

            # On passe à l'équipe suivante
            currentIndexEquipe = updateIndexEquipe(currentIndexEquipe, nbEquipes)

    """Affichage des résultats"""
    simplePrint(arrayEquipes, arrayColleges)

    """Vérification"""
    # Aucune équipe ne dépasse le max
    for equipe in arrayEquipes:
        assert equipe.getNbEleves() <= maxParEquipe
        assert (
            equipe.getNbEleves() <= maxParEquipe
        ), f"L'équipe {equipe.nom} dépasse le maximum {maxParEquipe} !"
    # Les élèves des collèges ont tous été placés
    for college in arrayColleges:
        placés = sum([value for value in college.repartition.values()])
        assert (
            placés == college.nbEleves
        ), f"Le collège {college.nom} n'a pas placé tous ses élèves ({placés}/{college.nbEleves}) !"


if __name__ == "__main__":
    main()
