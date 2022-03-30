from .modelisation import Match


def tournerAteliers(nbTours, teams, arrayAteliers):

    # Initialisation
    nbAteliers = len(arrayAteliers)
    nbTeams = len(teams)
    assert nbTeams % 2 == 0

    avantJetaisA = {}
    for indexEquipe, equipe in enumerate(teams):
        avantJetaisA[equipe.nom] = indexEquipe % nbAteliers

    # On tourne
    for horaire in range(1, nbTours + 1):
        arrayMatches = [Match(atelier, horaire) for atelier in arrayAteliers]

        for indexEquipe, equipe in enumerate(teams):
            avantLequipeEtaitA = avantJetaisA[equipe.nom]

            # La première moitié d'équipes tourne vers la droite
            # l'autre moitié vers la gauche
            if indexEquipe < nbTeams / 2:
                nextIndexAtelier = (avantLequipeEtaitA + 1) % nbAteliers
            else:
                nextIndexAtelier = (avantLequipeEtaitA - 1) % nbAteliers
            avantJetaisA[equipe.nom] = nextIndexAtelier

            nouveauMatch = arrayMatches[nextIndexAtelier]
            nouveauMatch.setTeam(equipe)
            equipe.addPlanning(nouveauMatch)

            # Si l'équipe fait partie des premières, on l'ajoute au planning de l'atelier
            if indexEquipe < nbTeams / 2:
                nouveauMatch.atelier.addPlanning(nouveauMatch)
