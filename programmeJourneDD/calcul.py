import math as m
from modelisation import Match


def tournerAteliers(teams, parcours1, parcours2):

    # Initialisation
    teamsPartie1 = teams[: m.ceil(len(teams) / 2)]
    teamsPartie2 = teams[m.ceil(len(teams) / 2) :]

    assert "Jean Jaurès" in ",".join([team.nom for team in teamsPartie1])
    assert "Abeilles" not in [atelier.nom for atelier in parcours1]

    for teams, parcours in [(teamsPartie1, parcours1), (teamsPartie2, parcours2)]:

        avantJetaisA = {}
        for indexTeam, team in enumerate(teams):
            avantJetaisA[team.nom] = indexTeam % len(parcours)

        # On tourne
        for horaire in range(1, len(parcours) + 1):
            arrayMatches = [Match(atelier, horaire) for atelier in parcours]

            for indexTeam, team in enumerate(teams):
                nextIndexAtelier = (avantJetaisA[team.nom] + 1) % len(arrayMatches)
                avantJetaisA[team.nom] = nextIndexAtelier
                nouveauMatch = arrayMatches[nextIndexAtelier]
                nouveauMatch.team = team

                # On l'ajoute au planning de l'atelier et de la team
                team.addPlanning(nouveauMatch)
                nouveauMatch.atelier.addPlanning(nouveauMatch)
