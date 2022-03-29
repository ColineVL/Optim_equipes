from initialisation import init, readExcel
from postTraitement import writeResultsInExcel

""" 
Répartir des élèves dans des équipes. 
Pas d'élève seul dans une équipe, sans camarades de son établissement.
Pas trop d'écart entre les équipes en termes de nombre d'élèves.
"""


def calcul(arrayColleges, arrayEquipes, maxParEquipe, nbEquipes):
    testBlocage = 0
    # Pour chaque collège, je boucle sur les équipes pour dispatcher ses élèves
    currentIndexEquipe = 0
    for col in arrayColleges:
        while col.elevesRestants > 0:
            equipe = arrayEquipes[currentIndexEquipe]

            # Si il reste de la place dans l'équipe, on peut la remplir
            if equipe.getPlacesRestantes(maxParEquipe) >= 2:

                # Si l'équipe n'a plus de place que pour 3 élèves, il faut qu'on remplisse !
                if equipe.getPlacesRestantes(maxParEquipe) == 3:
                    # Si il reste 2 élèves, ça marche pas puisqu'on va laisser une place vide dans l'équipe
                    # Si il en reste 3, on met tout !
                    # Si il en reste 4, ça marche pas puisqu'on va en laisser un tout seul
                    # Si il en reste 5 et plus, c'est bon
                    if col.elevesRestants == 3 or col.elevesRestants >= 5:
                        equipe.setEleves(col, 3)
                    elif col.elevesRestants == 2 or col.elevesRestants == 4:
                        # Cas particulier :
                        # Dans cette équipe il ne reste que 3 places, et ce collège n'a que deux ou quatre élèves.
                        # J'autorise à les placer là si on ne peut pas les mettre ailleurs.
                        # On fait un tour de boucle, si on repasse ici avec toujours ce même collège,
                        # C'est qu'on n'a pas réussi à mettre les gamins nul part. Donc on les met ici.
                        if testBlocage == 0:
                            testBlocage = f"{col.nom}{equipe.nom}"
                        else:
                            # Je compare
                            if testBlocage == f"{col.nom}{equipe.nom}":
                                # On a fait le fameux tour de boucle, donc c'est ok je les ajoute
                                equipe.setEleves(col, 2)
                                testBlocage = 0

                # Si on n'a plus que 3 élèves, il faut qu'ils restent ensemble
                elif col.elevesRestants == 3:
                    # Si l'équipe a de la place pour 3 élèves, on peut les placer
                    # Attention, s'il ne reste que 4 places, ça ne marche pas !
                    if (
                        equipe.getPlacesRestantes(maxParEquipe) == 3
                        or equipe.getPlacesRestantes(maxParEquipe) >= 5
                    ):
                        equipe.setEleves(col, 3)

                # Sinon, on place les élèves 2 par 2
                else:
                    equipe.setEleves(col, 2)

            # On passe à l'équipe suivante
            currentIndexEquipe = (currentIndexEquipe + 1) % nbEquipes


def main():
    """Initialisation"""
    arrayColleges = readExcel(option="lycée")
    nbEquipes = 16
    arrayEquipes, maxParEquipe = init(arrayColleges, nbEquipes)

    """Boucle de calcul"""
    calcul(arrayColleges, arrayEquipes, maxParEquipe, nbEquipes)

    """Affichage des résultats"""
    writeResultsInExcel(arrayEquipes, arrayColleges)

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
