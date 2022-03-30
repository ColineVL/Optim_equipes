from .modelisation import Match


def tournerAteliers(nbTours, teams, arrayAteliers):

    # Initialisation
    nbAteliers = len(arrayAteliers)
    nbTeams = len(teams)
    assert nbTeams % 2 == 0

    # Un atelier est désactivé à chaque horaire si pas assez d'équipes
    desactiver = False
    if nbAteliers * 2 > nbTeams:
        desactiver = True

    avantJetaisA = {}
    nbDemarrer = nbAteliers
    if desactiver:
        nbDemarrer -= 1
    for indexEquipe, equipe in enumerate(teams):
        avantJetaisA[equipe.nom] = indexEquipe % nbDemarrer

    # On tourne
    for horaire in range(1, nbTours + 1):
        if desactiver:
            indexDesactive = horaire

        arrayMatches = [
            Match(atelier, horaire)
            for indexAtelier, atelier in enumerate(arrayAteliers)
            if (desactiver and indexDesactive != indexAtelier)
        ]

        for indexEquipe, equipe in enumerate(teams):
            avantLequipeEtaitA = avantJetaisA[equipe.nom]

            # La première moitié d'équipes tourne vers la droite
            # l'autre moitié vers la gauche
            if indexEquipe < nbTeams / 2:
                nextIndexAtelier = (avantLequipeEtaitA + 1) % len(arrayMatches)
            else:
                nextIndexAtelier = (avantLequipeEtaitA - 1) % len(arrayMatches)
            avantJetaisA[equipe.nom] = nextIndexAtelier

            nouveauMatch = arrayMatches[nextIndexAtelier]
            nouveauMatch.setTeam(equipe)
            equipe.addPlanning(nouveauMatch)

            # Si l'équipe fait partie des premières, on l'ajoute au planning de l'atelier
            if indexEquipe < nbTeams / 2:
                nouveauMatch.atelier.addPlanning(nouveauMatch)
